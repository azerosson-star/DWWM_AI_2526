let angle = 0;
/*document.getElementById('cercle').onclick = function() {
    angle +=180;
    this.style.transform = `rotate(${angle}deg)`;
}*/

const shape = document.getElementById('cercle');
/*shape.addEventListener("mouseover", () => {
    angle +=180;
    shape.style.transform = `rotate(${angle}deg)`;
});*/

shape.addEventListener("mouseover", function() {
    angle +=180;
    this.style.transform = `rotate(${angle}deg)`;
});