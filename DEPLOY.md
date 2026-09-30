# Site de teste. Kit NR-01 Blindado

Endereço: https://siteteste.edxcautomacao.com.br
Stack no Portainer: `siteteste-kit-nr01` (arquivo `docker-compose.yml` deste repositório).
Imagem: `ghcr.io/eduardodxcosta/siteteste-kit-nr01` (privada; o Portainer usa o registro ghcr.io cadastrado com token de leitura).

## Atualizar o site depois de mudar a página

1. `py -3 sincronizar.py` (copia a página de `meus-produtos/kit-nr01-blindado/entregas/paginas/` para `site/`)
2. `git add -A` e `git commit -m "chore(site): atualizar pagina"`, depois `git push`
3. Esperar a Action ficar verde no GitHub
4. Portainer, Stacks, `siteteste-kit-nr01`, "Pull and redeploy" (ou trocar `IMAGE_TAG` pelo `sha-xxxxxxx` do commit)

## Observações

- Endereço de teste: todas as páginas levam "noindex" (meta robots, cabeçalho X-Robots-Tag e robots.txt).
- O botão de compra continua sem link até existir o checkout.
