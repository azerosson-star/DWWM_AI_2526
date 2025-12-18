# 1. Utiliser une image alpine de Node.js
FROM node:25-alpine

# 2. Créer le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# 3. Copier les fichiers de dépendances
COPY package*.json ./

# 4. Installer les dépendances
RUN npm install

# 5. Copier le reste du code source
COPY . .

# 6. Créer le dossier 'uploads' au cas où il n'existe pas
RUN mkdir -p public/data/uploads

# 7. Exposer le port utilisé par le serveur
EXPOSE 3001

# 8. Lancer l'application
CMD [ "node", "server.js" ]