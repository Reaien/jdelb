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

//animacion region 

//const cardDelegado = document.getElementById('cardDelegado');
//const regiones = document.getElementsByClassName('region');

//for (let index = 0; index < regiones.length; index++) {
//    regiones[index].addEventListener('mouseover', function(){
//        cardDelegado.style.display= 'block';
//        idPareja.style.display= 'none';
//    });
//    regiones[index].addEventListener('mouseout', function(){
//        cardDelegado.style.display= 'none';
//        idPareja.style.display= 'block';
//    });
//}

