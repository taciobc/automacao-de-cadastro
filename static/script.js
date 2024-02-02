// Elementos HTML
const enigmaElement = document.getElementById("enigma");
const palpiteElement = document.getElementById("palpite");
const feedbackElement = document.getElementById("feedback");
const dicaElement = document.getElementById("dica");

// Atualiza o enigma na interface
function atualizarEnigma(enigma) {
    enigmaElement.textContent = enigma;
}

// Atualiza a dica na interface
function atualizarDica(dica) {
    dicaElement.textContent = "Dica: " + dica;
}

// Verifica o palpite no servidor
function verificarPalpite() {
    const palpite = palpiteElement.value.toLowerCase();

    fetch('/verificar_palpite', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'palpite': palpite,
        }),
    })
    .then(response => response.json())
    .then(data => {
        feedbackElement.textContent = data.feedback;
        atualizarEnigma(data.enigma);
        atualizarDica(data.dica);
    });
}

// Inicialização
atualizarEnigma("_ _ _ _ _");
atualizarDica("");
