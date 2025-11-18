class Personne {
  // Attributs (données)
  constructor(nom, prenom, age) {
    this._nom = nom; // Attribut privé (nom encapsulé)
    this.prenom = prenom; // Attribut public
    this._age = age; // Attribut privé (âge encapsulé)
  }

  // Méthodes (comportements)
  getNomComplet() {
    return `${this.prenom} ${this._nom}`; // Accès à l'attribut privé via la méthode
  }

  setNom(nouveauNom) {
    this._nom = nouveauNom; // Modification de l'attribut privé via la méthode
  }

  getNom() {
    return this._nom; // Accès à l'attribut privé via la méthode getter
  }

  get agerecupere() { // Getter pour l'attribut age (lecture seule)
    return this._age;
  }

  getAge() {
    return this._age;
  }

  anniversaire() {
    this._age++; // Modification de l'attribut privé
    return `${this.getNomComplet()} a maintenant ${this.agerecupere} ans.`;
  }
}

// Fonction pour créer une personne et l'afficher dans le conteneur spécifié
function creerPersonne(nom, prenom, age, conteneurId) {
  const personne = new Personne(nom, prenom, age);
  const element = document.getElementById(conteneurId);
  element.innerHTML = `Personne créée: ${personne.getNom()}<br /> Anniversaire : ${personne.anniversaire()}`;
}

// Exemples d'utilisation des fonctions
function creerPersonne1() {
  creerPersonne("Dupont", "Jean", 20, "personne1");
}

function creerPersonne2() {
  creerPersonne("Martin", "Pierre", 35, "personne2");
}
