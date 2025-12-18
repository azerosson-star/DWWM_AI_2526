import * as THREE from 'three';

// --- 1. CONFIGURATION DE LA SCÈNE ---
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x050505);
scene.fog = new THREE.Fog(0x050505, 20, 150); // Brouillard pour accentuer la perspective

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// --- 2. DÉFINITION DE LA ROUTE LARGE (50 UNITÉS) ---
const rayonInterieur = 30;
const largeurRoute = 50;
const rayonExterieur = rayonInterieur + largeurRoute;
const rayonMilieu = rayonInterieur + (largeurRoute / 2); // 55

// Sol (Herbe/Terre)
const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(1000, 1000),
    new THREE.MeshBasicMaterial({ color: 0x111111 })
);
ground.rotation.x = -Math.PI / 2;
scene.add(ground);

// La Route Goudronnée
const trackGeo = new THREE.RingGeometry(rayonInterieur, rayonExterieur, 128);
const trackMat = new THREE.MeshBasicMaterial({ color: 0x222222, side: THREE.DoubleSide });
const track = new THREE.Mesh(trackGeo, trackMat);
track.rotation.x = -Math.PI / 2;
track.position.y = 0.01;
scene.add(track);

// Ligne Centrale Jaune
const lineGeo = new THREE.RingGeometry(rayonMilieu - 0.2, rayonMilieu + 0.2, 128);
const lineMat = new THREE.MeshBasicMaterial({ color: 0xffcc00, side: THREE.DoubleSide });
const line = new THREE.Mesh(lineGeo, lineMat);
line.rotation.x = -Math.PI / 2;
line.position.y = 0.02;
scene.add(line);

// Vibreurs Extérieurs (Rouge et Blanc)
const borderGeo = new THREE.RingGeometry(rayonExterieur, rayonExterieur + 1.5, 128);
const borderMat = new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide });
const border = new THREE.Mesh(borderGeo, borderMat);
border.rotation.x = -Math.PI / 2;
border.position.y = 0.015;
scene.add(border);

// --- 3. LA VOITURE DU JOUEUR ---
const carGroup = new THREE.Group();
const carBody = new THREE.Mesh(
    new THREE.BoxGeometry(1.5, 0.6, 2.5),
    new THREE.MeshBasicMaterial({ color: 0xff0000 })
);
const carRoof = new THREE.Mesh(
    new THREE.BoxGeometry(1.2, 0.5, 1.2),
    new THREE.MeshBasicMaterial({ color: 0xffffff })
);
carRoof.position.y = 0.5;
carGroup.add(carBody, carRoof);

// Positionner au départ sur le milieu de la route
carGroup.position.set(rayonMilieu, 0.3, 0);
scene.add(carGroup);

// --- 4. SYSTÈME DE CONDUITE ---
const keys = { ArrowUp: false, ArrowDown: false, ArrowLeft: false, ArrowRight: false };
window.onkeydown = (e) => keys[e.code] = true;
window.onkeyup = (e) => keys[e.code] = false;

let velocity = 0;
let rotation = 0;
const friction = 0.98;
const acceleration = 0.015;

function updatePhysics() {
    // Accélération et Freinage
    if (keys.ArrowUp) velocity += acceleration;
    if (keys.ArrowDown) velocity -= acceleration;
    
    velocity *= friction;

    // Direction (proportionnelle à la vitesse)
    if (Math.abs(velocity) > 0.01) {
        const turnSpeed = 0.04;
        if (keys.ArrowLeft) rotation += turnSpeed * (velocity * 1.2);
        if (keys.ArrowRight) rotation -= turnSpeed * (velocity * 1.2);
    }

    // Mise à jour position
    carGroup.rotation.y = rotation;
    carGroup.position.x += Math.sin(rotation) * velocity;
    carGroup.position.z += Math.cos(rotation) * velocity;

    // --- 5. PERSPECTIVE FUYANTE (CAMERA) ---
    // On place la caméra derrière et au dessus
    const offset = new THREE.Vector3(0, 3, -8); // 8 unités derrière, 3 de haut
    const actualOffset = offset.applyMatrix4(carGroup.matrixWorld);

    camera.position.lerp(actualOffset, 0.1); // Interpolation pour la fluidité
    
    // La caméra regarde loin devant la voiture
    const lookTarget = new THREE.Vector3(
        carGroup.position.x + Math.sin(rotation) * 20,
        1,
        carGroup.position.z + Math.cos(rotation) * 20
    );
    camera.lookAt(lookTarget);

    // Affichage vitesse (optionnel)
    const speedKm = Math.round(Math.abs(velocity * 450));
    const speedElement = document.getElementById('speedDisplay');
    if(speedElement) speedElement.innerText = speedKm.toString().padStart(3, '0');
}

// --- 6. BOUCLE DE RENDU ---
function animate() {
    requestAnimationFrame(animate);