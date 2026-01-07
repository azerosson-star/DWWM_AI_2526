const prenoms = ["bob", "Stuart", "Kevin", "Otto", "liloo"];
const firstname  = document.getElementById("firstname");
const size = document.getElementById("size");

// Afficher le premier prénom d'un tableau 
firstname.innerHTML = prenoms[4];

// Afficher la taille du tableau
size.innerHTML = prenoms.length;