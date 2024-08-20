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


document.addEventListener('DOMContentLoaded', function() {
    const fonoInput = document.getElementById('fono_bailarina');
    if (fonoInput) {
        fonoInput.addEventListener('input', function(event) {
            let value = event.target.value.replace(/\D/g, ''); // Elimina todos los caracteres no numéricos
            if (value.length > 9) {
                value = value.slice(0, 9); // Limita a 9 dígitos
            }
            event.target.value = value;
            event.target.setCustomValidity(value.length === 9 ? "" : "Debe tener exactamente 9 dígitos");
        });
    }
});