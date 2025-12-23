# Nginx_Php_Node-Demo

 Nginx Php Node.js

docker-compose up

Ouvrir un autre terminal
docker ps
97aa15ff39ab   nginx_php_node-demo-nginx    "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:8888->80/tcp    nginx_php_node-demo-nginx-1

docker exec -it 97 bash

bash-5.1# ls
bash-5.1# cd etc/nginx/conf.d
bash-5.1# ls
default.conf
bash-5.1# nano default.conf // voir le code dans le fichier
bash-5.1# /usr/sbin/nginx -s reload
