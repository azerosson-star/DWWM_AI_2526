"use strict";
class Forme {
    constructor(nom) {
        this.nom = nom;
    }
    getNom() {
        return this.nom;
    }
}
class Cercle extends Forme {
    constructor(nom, rayon) {
        super(nom);
        this.rayon = rayon;
    }
    calculerSurface() {
        return Math.PI * this.rayon * this.rayon;
    }
}
class Rectangle extends Forme {
    constructor(nom, longueur, largeur) {
        super(nom);
        this.longueur = longueur;
        this.largeur = largeur;
    }
    calculerSurface() {
        return this.longueur * this.largeur;
    }
}
function creerEtAfficherForme(nomForme, dimensions, conteneurId) {
    let forme;
    if (nomForme === "cercle") {
        forme = new Cercle(nomForme, dimensions[0]);
    }
    else if (nomForme === "rectangle") {
        forme = new Rectangle(nomForme, dimensions[0], dimensions[1]);
    }
    else {
        throw new Error(`Forme non reconnue : ${nomForme}`);
    }
    const element = document.getElementById(conteneurId);
    if (element) {
        element.innerHTML = `
      Forme créée: ${forme.getNom()} <br>
      Surface: ${forme.calculerSurface()}
    `;
    }
    else {
        console.error(`Élément avec l'id "${conteneurId}" introuvable.`);
    }
}

function creerForme() {
  const nomForme = document.getElementById("nomForme").value;
  const dimensions = [];
  if (nomForme === "cercle") {
    dimensions.push(parseFloat(document.getElementById("rayon").value));
  } else if (nomForme === "rectangle") {
    dimensions.push(parseFloat(document.getElementById("longueur").value));
    dimensions.push(parseFloat(document.getElementById("largeur").value));
  }

  creerEtAfficherForme(nomForme, dimensions, "resultat");
}