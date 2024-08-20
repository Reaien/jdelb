document.addEventListener('DOMContentLoaded', function() {
    const rutInputs = document.querySelectorAll('.run');
    rutInputs.forEach(rutInput => {
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

            // Validación del rango de RUT
            let numericRut = parseInt(rut.replace(/\./g, ''), 10); // Convertir a número sin puntos
            if (numericRut < 22000000 || numericRut > 23600000) {
                event.target.setCustomValidity("El RUT debe estar entre 22.000.000 y 23.600.000.");
            } else {
                event.target.setCustomValidity(""); // Borrar mensaje si es válido
            }
        });
    });
});