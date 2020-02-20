$("#menu-toggle").click(function(e) {
  	e.preventDefault();
  	$("#wrapper").toggleClass("toggled");
});
var fichier = document.getElementById('fichier');
var join = document.getElementById('joindre');
if (join.checked) {
	fichier.style.display = "block";
}
window.addEventListener("click", function() {
	if (join.checked) {
		fichier.style.display = "block";
	}
	else if (!join.checked) {
		fichier.style.display = "none";
	}
}, false);