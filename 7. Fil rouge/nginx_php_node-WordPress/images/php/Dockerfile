FROM php:8.3-fpm
# Extensions PHP nécessaires à WordPress
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Configuration permissions
WORKDIR /var/www/html