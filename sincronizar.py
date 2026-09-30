# -*- coding: utf-8 -*-
"""
Copia a versão atual da página de vendas do Kit NR-01 Blindado para este
projeto de deploy (site de teste em siteteste.edxcautomacao.com.br).

Origem: D:/severino/meus-produtos/kit-nr01-blindado/entregas/paginas/
Ajustes aplicados só na cópia publicada:
  - vendas-kit-nr01-blindado.html vira index.html
  - aviso "não indexar" (robots noindex) em todas as páginas, porque é endereço de teste
  - og:image e og:url com endereço completo, para a prévia aparecer no WhatsApp

Uso: py -3 sincronizar.py   (depois: git add, commit e push para gerar a imagem nova)
"""
import re
import shutil
from pathlib import Path

DOMINIO = "https://siteteste.edxcautomacao.com.br"
ORIGEM = Path("D:/severino/meus-produtos/kit-nr01-blindado/entregas/paginas")
DESTINO = Path(__file__).resolve().parent / "site"

PAGINAS = {
    "vendas-kit-nr01-blindado.html": "index.html",
    "termos-de-uso.html": "termos-de-uso.html",
    "politica-de-privacidade.html": "politica-de-privacidade.html",
}
IMAGENS = [
    "furadeira-protocolo.webp",
    "kit-cartaz-canal.webp",
    "kit-guia-apuracao.webp",
    "kit-manual-canal.webp",
    "kit-planilha-resultado.webp",
    "og-kit-nr01-blindado.png",
]
NOINDEX = '<meta name="robots" content="noindex, nofollow">'


def ajustar(html: str, arquivo_destino: str) -> str:
    if not re.search(r'<meta name="robots"', html, flags=re.I):
        html = re.sub(r"(<meta charset=[^>]*>)", r"\1\n" + NOINDEX, html, count=1, flags=re.I)
    html = html.replace('content="assets/og-kit-nr01-blindado.png"',
                        f'content="{DOMINIO}/assets/og-kit-nr01-blindado.png"')
    if arquivo_destino == "index.html" and 'property="og:url"' not in html:
        html = html.replace('<meta property="og:type"',
                            f'<meta property="og:url" content="{DOMINIO}/">\n<meta property="og:type"', 1)
    return html


def main() -> None:
    if DESTINO.exists():
        shutil.rmtree(DESTINO)
    (DESTINO / "assets").mkdir(parents=True)
    for origem, destino in PAGINAS.items():
        html = (ORIGEM / origem).read_text(encoding="utf-8")
        (DESTINO / destino).write_text(ajustar(html, destino), encoding="utf-8")
    for nome in IMAGENS:
        shutil.copy2(ORIGEM / "assets" / nome, DESTINO / "assets" / nome)
    (DESTINO / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    print(f"Página copiada para {DESTINO}")


if __name__ == "__main__":
    main()
