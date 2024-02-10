document.addEventListener('DOMContentLoaded', function() {
    function actualizarResultados() {
        fetch(window.location.href, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest' // Agrega una cabecera para indicar una solicitud AJAX
            }
        })
        .then(response => response.json())
        .then(data => {
            var tablaResultados = document.getElementById('tabla-resultados');
            tablaResultados.innerHTML = '';

            data.resultados_votos.forEach(resultado => {
                var fila = `<div class="row">`;
                fila += `<div class="col-md-12 text-center"><h5 name="region_nombre" class="titulo-region-votacion-resultados fw-bold">${resultado.nombreRegion}</h5></div>`;
                fila += `<div class="d-flex justify-content-start">`;
                fila += `<div class="col-md-4 col-xl-5 ps-0 pe-0 text-center"><img class="rounded-4 img-fluid w-75 border border-5" src="${resultado.fotoCompetidora}" alt="competidora"><p class="fw-bold mt-1 nombre-competidor-resultados">${resultado.nombreCompletoCompetidora}</p></div>`;
                fila += `<div class="col-md-4 col-xl-5 ps-0 pe-0 text-center"><img class="rounded-4 img-fluid w-75 border border-5" src="${resultado.fotoCompetidor}" alt="competidor"><p class="fw-bold mt-1 nombre-competidor-resultados">${resultado.nombreCompletoCompetidor}</p></div>`;
                fila += `<div class="col-md-3 col-xl-3 d-flex justify-content-center align-items-center"><p class="fw-bold mt-1 nombre-competidor-resultados">Votos: ${resultado.votos}</p></div>`;
                fila += `</div></div>`;

                tablaResultados.innerHTML += fila;
            });
        });
    }

    // Actualizar los resultados cada 10 segundos
    setInterval(actualizarResultados, 10000);

    // Actualizar los resultados al cargar la página
    actualizarResultados();
});