"use strict";

class voiture {
    constructor(marque, modele, annee) {
        this.marque = marque;
        this.model = modele;
        this.annee = annee;
    }

    description(){
        return "la voiture est " + this.marque + ' ' + this.model + ' ' + this.annee;
    }
}

const renault = new voiture('renault', 'r5', '1985');
const car = document.getElementById("car");
car.innerHTML = renault.description();
