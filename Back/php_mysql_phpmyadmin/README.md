# Docker-Demo
 Docker
 
cd php_mysql_phpmyadmin
docker compose up

#PhpMyAdmin
root
root_password

Volume mysqldata pointe sur le dossier du disque dur './db_server/mysql-phpmyadmin/data'
volumes:
            - mysqldata:/var/lib/mysql

Le fichier Dockerfile est utilisé par le service php.

Le dossier source-site du disque dur contient le site Web.
volumes:
        - ./source_site:/var/www/html/


Icone Troubleshoot dans Docker Desktop
Clean / Purge data

# déziper l'archive data.zip
