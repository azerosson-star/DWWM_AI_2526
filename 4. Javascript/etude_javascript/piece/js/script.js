// On demande au navigateur d'attendre que tout le HTML soit bien chargé et analysé 
// avant d'exécuter le code à l'intérieur des accolades.

document.addEventListener('DOMContentLoaded', () => {
    // On cherche dans la page l'élément qui possède l'ID "cercle" 
    // et on le stocke dans une variable nommée 'cercle' pour pouvoir le manipuler.
    const cercle = document.getElementById('cercle');

    // On crée une variable servant de "mémoire" (un interrupteur). 
    // Au début, elle est à 'false' car le cercle n'a pas encore tourné.
    let tourne = false;

    // On dit au navigateur de surveiller si l'utilisateur clique sur l'élément 'cercle'.
    cercle.addEventListener('click', () => {

        // À chaque clic, on inverse la valeur de 'tourne'. 
        // Si c'était 'false' (0°), ça devient 'true' (180°), et vice-versa.

        tourne = !tourne;

        // On modifie directement le CSS de l'élément (propriété 'transform').
        // C'est un test "ternaire" (si / alors / sinon) :
        // - Si 'tourne' est vrai (true), on applique 'rotateY(180deg)'.
        // - Sinon (:), on applique 'rotateY(0deg)'.
        cercle.style.transform = tourne ? 'rotateY(180deg)' : 'rotateY(0deg)';
        });
});