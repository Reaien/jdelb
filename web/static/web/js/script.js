//fx para verificar si un elemento está en el area visible de la pantalla


// Configuración del Intersection Observer
const opcionesObserver = {
    root: null,
    rootMargin: '0px',
    threshold: 0.02 // Umbral del 50%
};

//fx para manejar el desplazamiento y activar la animación

function manejarEntradas(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const elemento = entry.target;
            if (elemento.id === 'pais_chile') {
                elemento.classList.add('fade-in');
            }else if(elemento.id === 'cuequeros'){
                elemento.classList.add('fade-in-right')
            }
            observer.unobserve(entry.target);
        }
    });
}

const observer = new IntersectionObserver(manejarEntradas, opcionesObserver);

const idChile = document.getElementById('pais_chile');
const idPareja = document.getElementById('cuequeros');
observer.observe(idChile);
observer.observe(idPareja);
//end observer pareja

//script animación rut
document.addEventListener('DOMContentLoaded', function() {
    const rutInput = document.getElementById('rut');
    if (rutInput) {
        rutInput.addEventListener('input', function (event) {
            let rut = event.target.value.replace(/\D/g, ''); // Elimina todos los caracteres que no sean dígitos
            let formattedRut = '';

            if (rut.length > 1) {
                formattedRut = rut.slice(-1); // Extrae el dígito verificador
                rut = rut.slice(0, -1); // Elimina el dígito verificador del RUT
            }

            if (rut.length > 3) {
                formattedRut = rut.slice(-3) + '-' + formattedRut;
                rut = rut.slice(0, -3);
            }

            while (rut.length > 3) {
                formattedRut = rut.slice(-3) + '.' + formattedRut;
                rut = rut.slice(0, -3);
            }

            if (rut.length > 0) {
                formattedRut = rut + '.' + formattedRut;
            }

            event.target.value = formattedRut;
        });
    }

});


document.addEventListener('DOMContentLoaded', function() {
    const regionSelect = document.getElementById('region_inscripcion');
    const comunaSelect = document.getElementById('comuna_inscripcion');

    regionSelect.addEventListener('change', function() {
        const regionId = this.value;
        if (regionId) {
            fetch(`/comunas/${regionId}/`)
                .then(response => response.json())
                .then(data => {
                    // Limpiar el select de comunas
                    comunaSelect.innerHTML = '<option value="">Selecciona una comuna</option>';
                    // Añadir las opciones recibidas
                    data.forEach(comuna => {
                        const option = document.createElement('option');
                        option.value = comuna.id;
                        option.textContent = comuna.nombre;
                        comunaSelect.appendChild(option);
                    });
                });
        } else {
            // Si no se selecciona ninguna región, limpiar el select de comunas
            comunaSelect.innerHTML = '<option value="">Selecciona una comuna</option>';
        }
    });
});