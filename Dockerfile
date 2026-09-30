FROM nginx:1.27-alpine

RUN rm -rf /usr/share/nginx/html/* /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf

# Conteúdo gerado por sincronizar.py a partir da página em meus-produtos
COPY site /usr/share/nginx/html

EXPOSE 80
# Sem HEALTHCHECK de propósito: no Swarm ele causa loop silencioso (ver skill portainer-vps-deploy, lição 11)
