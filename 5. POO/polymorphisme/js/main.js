class Personne {
  constructor(nom, prenom, age) {
    this.nom = nom;
    this.prenom = prenom;
    this.age = age;
  }

  getNomComplet() {
    return `${this.prenom} ${this.nom}`;
  }

  anniversaire() {
    this.age++;
  }
}

class Etudiant extends Personne {
  constructor(nom, prenom, age, etude) {
    super(nom, prenom, age);
    this.etude = etude;
  }

  getNomComplet() { // Surcharge de la méthode getNomComplet
    return super.getNomComplet() + ` - Etudiant en ${this.etude}`;
  }
}

// Fonction pour créer une personne et l'afficher dans une alerte
function creerPersonne() {
  const nom = document.getElementById("nom").value;
  const prenom = document.getElementById("prenom").value;
  const age = parseInt(document.getElementById("age").value);
  const personne = new Personne(nom, prenom, age);
  alert(`Personne créée: ${personne.getNomComplet()} (âge: ${personne.age})`);
}

// Fonction pour créer un étudiant et l'afficher dans une alerte
function creerEtudiant() {
  const nom = document.getElementById("nom").value;
  const prenom = document.getElementById("prenom").value;
  const age = parseInt(document.getElementById("age").value);
  const etude = document.getElementById("etude").value;
  const etudiant = new Etudiant(nom, prenom, age, etude);
  alert(`Etudiant créé: ${etudiant.getNomComplet()} (âge: ${etudiant.age})`);
}

// Fonction pour afficher les informations d'une personne dans une alerte
function afficherPersonne() {
  const nom = document.getElementById("nom").value;
  const prenom = document.getElementById("prenom").value;
  const age = parseInt(document.getElementById("age").value);
  const personne = new Personne(nom, prenom, age);
  alert(`Informations personne: ${personne.getNomComplet()} (âge: ${personne.age})`);
}

// Fonction pour afficher les informations d'un étudiant dans une alerte
function afficherEtudiant() {
  const nom = document.getElementById("nom").value;
  const prenom = document.getElementById("prenom").value;
  const age = parseInt(document.getElementById("age").value);
  const etude = document.getElementById("etude").value;
  const etudiant = new Etudiant(nom, prenom, age, etude);
  alert(`Informations étudiant: ${etudiant.getNomComplet()} (âge: ${etudiant.age})`);
}