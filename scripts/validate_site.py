from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
errors = []
references = 0


def check_reference(source, value):
    global references
    if not value:
        errors.append(f"{source.name}: referência vazia")
        return
    if "\\" in value or re.match(r"^[A-Za-z]:", value):
        errors.append(f"{source.name}: caminho de computador local: {value}")
        return
    url = urlsplit(value)
    if url.scheme or url.netloc or not url.path:
        return
    if url.path.startswith("/"):
        errors.append(f"{source.name}: use caminho relativo ao site: {value}")
        return
    target = (source.parent / unquote(url.path)).resolve()
    references += 1
    if not target.is_relative_to(ROOT) or not target.is_file():
        errors.append(f"{source.name}: arquivo local não encontrado: {value}")


class PageParser(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.has_title = False
        self.has_html = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.has_title |= tag == "title"
        self.has_html |= tag == "html" and bool(attrs.get("lang"))
        if tag == "img" and not attrs.get("src"):
            errors.append(f"{self.source.name}: imagem sem src")
        for attr in ("src", "href", "action"):
            if attr in attrs:
                check_reference(self.source, attrs[attr])
        if tag == "input" and attrs.get("type") == "password" and attrs.get("name"):
            errors.append(f"{self.source.name}: senha demonstrativa não deve ser enviada")


pages = sorted(ROOT.glob("*.html"))
required = ["index.html", "site.html", "sobre.html"] + [
    f"resenha{number}.html" for number in range(1, 11)
]
for name in required:
    if not (ROOT / name).is_file():
        errors.append(f"Página obrigatória ausente: {name}")

for page in pages:
    text = page.read_text(encoding="utf-8")
    parser = PageParser(page)
    parser.feed(text)
    parser.close()
    if not parser.has_title or not parser.has_html:
        errors.append(f"{page.name}: faltam título ou idioma do documento")

for stylesheet in ROOT.glob("*.css"):
    for match in re.finditer(r"url\(\s*['\"]?([^)'\"]+)['\"]?\s*\)", stylesheet.read_text(encoding="utf-8")):
        check_reference(stylesheet, match.group(1).strip())

if errors:
    print("Falha na verificação do site:\n" + "\n".join(errors))
    sys.exit(1)

print(f"Validação concluída: {len(pages)} páginas e {references} referências locais verificadas.")
