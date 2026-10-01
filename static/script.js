document.addEventListener("DOMContentLoaded", function () {

    const formulario = document.getElementById("formulario");

    if (formulario) {
        formulario.addEventListener("submit", function (evento) {
            evento.preventDefault();

            alert("Gracias por contactar a Café Aroma.");

            formulario.reset();
        });
    }

});
