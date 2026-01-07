import express from 'express';
import multer  from 'multer';
import path from 'path';
import fs from 'fs';
import cors from 'cors';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3001; // On harmonise sur le port 3001

app.use(cors());
// Sert les fichiers statiques (JS, CSS) depuis le dossier 'public'
// INDISPENSABLE : Pour servir le dossier contenant main.js
// Si main.js est dans un dossier nommé "js", créez un dossier "public" et mettez "js" dedans.
app.use(express.static('public'));

// Chemin absolu vers le dossier d'upload
const uploadPath = path.join(__dirname, 'public', 'data', 'uploads');

// Création récursive du dossier s'il n'existe pas
if (!fs.existsSync(uploadPath)) {
    fs.mkdirSync(uploadPath, { recursive: true });
}

// Configuration du stockage Multer
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, uploadPath); // Utilisation du chemin absolu
    },
    filename: function (req, file, cb) {
        const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
        cb(null, file.fieldname + '-' + uniqueSuffix + path.extname(file.originalname));
    }
});

const fileFilter = (req, file, cb) => {
    const allowedTypes = [
        'application/pdf', 
        'application/msword', 
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'image/jpeg', 
        'image/png'
    ];
    if (allowedTypes.includes(file.mimetype)) {
        cb(null, true);
    } else {
        cb(new Error('Format non supporté !'), false);
    }
}

const upload = multer({ 
    storage: storage,
    fileFilter: fileFilter,
    limits: { fileSize: 5 * 1024 * 1024 } // Limite à 5 Mo
});

// Route pour servir le template HTML
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Route d'upload - Le nom 'uploaded_file' doit correspondre au frontend
app.post('/upload', upload.single('uploaded_file'), (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: 'Aucun fichier reçu par le serveur.' });
    }
    console.log(`Fichier sauvegardé dans : ${req.file.path}`);
    res.status(200).json({ message : 'Fichier uploadé avec succès !' });
}, (error, req, res, next) => {
    // Gestion des erreurs Multer (ex: fichier trop gros ou mauvais format)
    res.status(400).json({ error: error.message });
});

app.listen(PORT, () => {
    console.log(`Serveur lancé sur http://localhost:${PORT}`);
});