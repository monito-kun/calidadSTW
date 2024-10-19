document.getElementById('calcular').addEventListener('click', function() {
    const personas = document.getElementById('personas').value;
    const dias = document.getElementById('dias').value;
    
    if (personas > 0 && dias > 0) {
        const co2PorPersonaPorDia = 2.5; // kg
        const totalCO2 = personas * dias * co2PorPersonaPorDia;
        document.getElementById('resultado').innerText = `Total CO2 emitido: ${totalCO2} kg`;
    } else {
        document.getElementById('resultado').innerText = 'Por favor, ingresa valores válidos.';
    }
});
