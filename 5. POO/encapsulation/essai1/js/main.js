class Personne {
    // Attributs (données)
    constructor(nom, prenom, age) {
      this.nom = nom;
      this.prenom = prenom;
      this.age = age;
    }
  
    // Méthodes (comportements)
    getNomComplet() {
      return `${this.prenom} ${this.nom}`;
    }
  
    anniversaire() {
      return `${++this.age}`;
    }
  }
  
// Fonction pour créer une personne et l'afficher dans le conteneur spécifié
function creerPersonne(nom, prenom, age, conteneurId) {
  const personne = new Personne(nom, prenom, age);
  const element = document.getElementById(conteneurId);
  element.innerHTML = `Personne créée: ${personne.getNomComplet()} (âge: ${personne.age}) Anniversaire : ${personne.anniversaire()}`;
}

// Fonctions pour afficher les informations d'une personne dans son conteneur
function afficherPersonne(conteneurId) {
  const element = document.getElementById(conteneurId);
  element.innerHTML = `Informations de la personne:`; // Effacer le contenu précédent
}


// Exemples d'utilisation des fonctions
function creerPersonne1() {
  creerPersonne("Dupont", "Jean", 20, "personne1");
}

function creerPersonne2() {
  creerPersonne("Martin", "Pierre", 35, "personne2");
}
