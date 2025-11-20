require('dotenv').config();
const http = require('http');
const fs = require('fs');
const path = require('path');

const port = process.env.PORT || 3000;

function getContentType(ext) {
    switch (ext.toLowerCase()) {
        case '.html': return 'text/html';
        case '.css': return 'text/css';
        case '.js': return 'application/javascript';
        case '.json': return 'application/json';
        case '.png': return 'image/png';
        case '.jpg':
        case '.jpeg': return 'image/jpeg';
        case '.gif': return 'image/gif';
        case '.svg': return 'image/svg+xml';
        default: return 'application/octet-stream';
    }
}

function serveFile(filePath, res) {
    fs.readFile(filePath, (err, data) => {
        if (err) {
            res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
            return res.end('404 - Fichier introuvable');
        }
        res.writeHead(200, { 'Content-Type': getContentType(path.extname(filePath)) });
        res.end(data);
    });
}

const server = http.createServer((req, res) => {
    const urlPath = decodeURIComponent(req.url.split('?')[0]);

    // Route racine -> pages/home.html
    if (urlPath === '/' || urlPath === '/home') {
        const htmlPath = path.join(__dirname, 'pages', 'home.html');
        return serveFile(htmlPath, res);
    }

    // Route racine -> pages/contact.html
    if (urlPath === '/' || urlPath === '/contact') {
        const htmlPath = path.join(__dirname, 'pages', 'contact.html');
        return serveFile(htmlPath, res);
    }    

    // Try to resolve the requested path in several locations:
    // 1) If it already starts with /public, serve from project public folder
    // 2) Try public/<urlPath>
    // 3) Try pages/<urlPath>
    // 4) Try root-relative
    let candidate = null;

    if (urlPath.startsWith('/public/')) {
        candidate = path.join(__dirname, urlPath);
        if (fs.existsSync(candidate)) return serveFile(candidate, res);
    }

    const tryPublic = path.join(__dirname, 'public', urlPath);
    const tryPages = path.join(__dirname, 'pages', urlPath);
    const tryRoot = path.join(__dirname, urlPath);

    if (fs.existsSync(tryPublic)) candidate = tryPublic;
    else if (fs.existsSync(tryPages)) candidate = tryPages;
    else if (fs.existsSync(tryRoot)) candidate = tryRoot;
    else {
        // convenience: map '/style.css' -> 'public/css/style.css', '/js/main.js' -> 'public/js/main.js'
        if (urlPath.startsWith('/')) {
            const basename = urlPath.slice(1);
            const altCss = path.join(__dirname, 'public', 'css', basename);
            const altJs = path.join(__dirname, 'public', 'js', basename);
            const altAssets = path.join(__dirname, 'public', 'assets', basename);
            if (fs.existsSync(altCss)) candidate = altCss;
            else if (fs.existsSync(altJs)) candidate = altJs;
            else if (fs.existsSync(altAssets)) candidate = altAssets;
        }
    }

    if (candidate) return serveFile(candidate, res);

    // Not found
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('404 - Not Found');
});

server.listen(port, () => {
    console.log(`Le serveur a été lancé sur http://localhost:${port}`);
});