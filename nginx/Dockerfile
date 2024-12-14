FROM ubuntu:latest

RUN apt-get update && apt-get install -y procps
RUN apt-get update && apt-get install -y dos2unix
RUN mkdir -p /home/app/staticfiles
RUN apt-get update && apt-get install -y nginx openssl nginx-extras
RUN mkdir /etc/nginx/ssl

COPY ./tools/nginx_start.sh /var/www

RUN dos2unix /var/www/nginx_start.sh

RUN chmod +x /var/www/nginx_start.sh
RUN mkdir -p /run/nginx

ENTRYPOINT ["var/www/nginx_start.sh"]

EXPOSE 443

CMD ["service", "nginx", "restart"]
CMD ["nginx", "-g", "daemon off;"]