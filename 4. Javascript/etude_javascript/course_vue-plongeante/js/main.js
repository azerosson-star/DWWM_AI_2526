// Enregistrement du plugin
gsap.registerPlugin(MotionPathPlugin);

const btn = document.getElementById('startBtn');
const winnerText = document.getElementById('winner');

btn.addEventListener('click', () => {
    winnerText.innerText = "La course est lancée !";
    const cars = [
        { id: "#car1", name: "Éclair" },
        { id: "#car2", name: "Turbo" }
    ];

    cars.forEach(carData => {
        // Timeline individuelle pour chaque voiture
        const tl = gsap.timeline({
            onComplete: () => announceWinner(carData.name)
        });

        const baseDuration = Math.random() * 3 + 4; // Entre 4 et 7 secondes

        tl.to(carData.id, {
            duration: baseDuration,
            ease: "none",
            motionPath: {
                path: "#route",
                autoRotate: true,
                align: "#route",
                alignOrigin: [0.5, 0.5]
            }
        });

        // AJOUT DES OBSTACLES : On ralentit la timeline à des moments précis
        // On insère un ralentissement à 30% du parcours (le premier cône)
        tl.to(tl, { timeScale: 0.2, duration: 0.4 }, baseDuration * 0.2); // Freinage
        tl.to(tl, { timeScale: 1, duration: 0.6 }, baseDuration * 0.3);   // Accélération après l'obstacle
    });
});

let finished = false;
function announceWinner(name) {
    if (!finished) {
        finished = true;
        winnerText.innerText = `🏆 VICTOIRE DE : ${name} !`;
        setTimeout(() => { finished = false; }, 4000);
    }
}