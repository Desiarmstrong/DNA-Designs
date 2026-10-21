from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []
        self.assets = []
        self.forms = []
        self.buttons = []
        self.images = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id"):
            assert d["id"] not in self.ids, f"Duplicate id: {d['id']}"
            self.ids.add(d["id"])
        if tag == "a" and "href" in d: self.hrefs.append(d["href"])
        if tag in ("img","script") and d.get("src"): self.assets.append(d["src"])
        if tag == "link" and d.get("href"): self.assets.append(d["href"])
        if tag == "form": self.forms.append(d)
        if tag == "button": self.buttons.append(d)
        if tag == "img": self.images.append(d)

def validate(filename):
    page = Page()
    page.feed((ROOT / filename).read_text(encoding="utf-8"))
    for href in page.hrefs:
        if href.startswith("#"):
            assert href[1:] in page.ids, f"{filename}: broken anchor {href}"
    for asset in page.assets:
        if asset.startswith(("https:", "http:", "//", "data:")): continue
        target = unquote(asset.split("?",1)[0].split("#",1)[0]).lstrip("/")
        assert (ROOT / target).is_file(), f"{filename}: missing asset {asset}"
    for img in page.images: assert "alt" in img, f"{filename}: image needs alt"
    return page

home = validate("index.html")
thanks = validate("thank-you.html")
assert len(home.forms) == 1
form = home.forms[0]
assert form.get("name") == "contact" and "data-netlify" in form
assert form.get("method","").upper() == "POST"
assert form.get("action") == "/thank-you.html"
assert any(b.get("class") == "menu-toggle" and b.get("aria-expanded") == "false" for b in home.buttons)
assert (ROOT / "robots.txt").is_file() and (ROOT / "sitemap.xml").is_file()
print("PASS: local assets, anchor links, image alt text, Netlify form contract, navigation, SEO files")
