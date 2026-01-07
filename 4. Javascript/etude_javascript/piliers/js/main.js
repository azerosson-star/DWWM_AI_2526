//1. On récupère les éléments h1 Button
const bouton = document.getElementById("monButton");
const compteur = document.getElementById("compteur");
const reset = document.getElementById("reset");
let compte = 0;

//2. On écoute le clic
bouton.addEventListener('click', () => {
    //3. On incrémente le compteur
    compte++;
    compteur.textContent = compte;
});

reset.addEventListener('click', () => {
    //4. On réinitialise le compteur
    compte=0;
    compteur.textContent = compte;
});