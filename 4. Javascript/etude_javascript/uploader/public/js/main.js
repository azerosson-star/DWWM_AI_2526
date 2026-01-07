async function uploadFile() {
    const fileInput = document.getElementById("pdfupload");
    const status = document.getElementById("status"); // Variable correcte

    // Vérification de la sélection d'un fichier
    if (!fileInput.files || fileInput.files.length === 0) {
        status.innerText = "Veuillez d'abord choisir un fichier.";
        status.style.color = "orange";
        return;
    }
    
    const file = fileInput.files[0];
    const formData = new FormData();

    // IMPORTANT : 'uploaded_file' doit être identique au nom utilisé dans upload.single() côté serveur
    formData.append('uploaded_file', file);

    status.innerText = "Envoi en cours...";
    status.style.color = "blue";

    try {
        const response = await fetch('http://localhost:3001/upload', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            status.innerText = "Succès ! " + result.message;
            status.style.color = "green";
            fileInput.value = ""; // Réinitialise l'input après succès
        } else {
            status.innerText = "Erreur : " + (result.error || "Problème lors de l'upload.");
            status.style.color = "red";
        }
    } catch(error) {
        status.innerText = "Erreur : Impossible de contacter le serveur.";
        status.style.color = "red";
        console.error("Détails de l'erreur:", error);
    }
}

// Ajoutez l'écouteur d'événement pour que le bouton fonctionne
document.getElementById("uploadFile").addEventListener("click", uploadFile);