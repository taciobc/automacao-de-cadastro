from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Lista de enigmas e dicas
enigmas_com_dicas = [
    {"palavra": "python", "dica": "Uma cobra não venenosa, mas muito poderosa na programação."},
    {"palavra": "javascript", "dica": "A linguagem de script amplamente utilizada para desenvolvimento web."},
    {"palavra": "html", "dica": "A linguagem de marcação fundamental para criar páginas web."},
    {"palavra": "css", "dica": "Utilizado para estilizar documentos HTML."},
    {"palavra": "web", "dica": "O ambiente onde navegamos e acessamos informações online."},
    {"palavra": "futebol", "dica": "Esporte mundialmente popular jogado com uma bola entre duas equipes."},
    {"palavra": "política", "dica": "Processo de tomada de decisões para uma comunidade."},
    {"palavra": "geografia", "dica": "Estudo da Terra e seus fenômenos naturais e humanos."},
    {"palavra": "cidade", "dica": "Assentamento urbano com uma população significativa."},
    {"palavra": "tecnologia", "dica": "Conjunto de conhecimentos e técnicas para produzir, modificar e utilizar objetos e serviços."},
    {"palavra": "filme", "dica": "Obra cinematográfica, geralmente com uma história dramática ou fictícia."},
    {"palavra": "anime", "dica": "Estilo de animação japonesa com características distintas."},
    {"palavra": "novela", "dica": "Narrativa longa e ficcional, geralmente transmitida na televisão."},
    {"palavra": "economia", "dica": "Estudo de como a sociedade utiliza seus recursos escassos para produzir bens e serviços."},
    {"palavra": "elefante", "dica": "O maior animal terrestre, conhecido por suas grandes orelhas e tromba."},
    {"palavra": "democracia", "dica": "Sistema de governo onde o poder é exercido pelo povo."},
    {"palavra": "espionagem", "dica": "Atividade de obter informações secretas de maneira não autorizada."},
    {"palavra": "astronomia", "dica": "Estudo dos corpos celestes, como estrelas, planetas e galáxias."},
    {"palavra": "biodiversidade", "dica": "Variedade de vida na Terra, incluindo diferentes espécies de plantas, animais e microrganismos."},
    {"palavra": "literatura", "dica": "Expressão artística por meio da escrita, incluindo romances, poesia e ensaios."},
    {"palavra": "energia renovável", "dica": "Fonte de energia que é obtida de recursos naturais, como solar, eólica e hidrelétrica."},
    {"palavra": "pintura", "dica": "Forma de arte visual que utiliza pigmentos para criar obras em superfícies como tela ou papel."},
    {"palavra": "vírus", "dica": "Agente infeccioso microscópico que se reproduz dentro de células de organismos hospedeiros."},
    {"palavra": "mitologia", "dica": "Conjunto de histórias e crenças que fazem parte da tradição de uma cultura."},
    {"palavra": "culinária", "dica": "Arte de cozinhar e preparar alimentos de maneira criativa."},
    {"palavra": "sustentabilidade", "dica": "Prática de utilizar recursos de forma que atenda às necessidades presentes sem comprometer as futuras gerações."},
    {"palavra": "sociologia", "dica": "Estudo científico da sociedade, seus padrões, instituições e processos sociais."},
    {"palavra": "biologia", "dica": "Ciência que estuda os seres vivos e seus processos vitais."},
    {"palavra": "filosofia", "dica": "Busca do entendimento fundamental da natureza, conhecimento, valores e existência."},
    {"palavra": "teatro", "dica": "Forma de arte que utiliza atores para representar uma história diante de uma audiência."},
    {"palavra": "história", "dica": "Registro e estudo de eventos passados, incluindo suas causas e consequências."},
    {"palavra": "genética", "dica": "Estudo dos genes, hereditariedade e variação nos organismos."},
    {"palavra": "psicologia", "dica": "Ciência que estuda o comportamento e os processos mentais dos seres humanos."},
    {"palavra": "avião", "dica": "Veículo mais pesado que o ar, dotado de asas e motores, capaz de voar."},
    {"palavra": "inovação", "dica": "Introdução de algo novo ou diferente que traz melhorias ou avanços."},
    {"palavra": "química", "dica": "Ciência que estuda a composição, estrutura, propriedades e transformações da matéria."},
    {"palavra": "equidade", "dica": "Princípio de justiça que busca tratar todos de maneira justa e imparcial."},
    {"palavra": "pandemia", "dica": "Doença que afeta uma ampla área geográfica e afeta uma proporção excepcionalmente alta de população."},
    {"palavra": "energia nuclear", "dica": "Energia liberada durante processos nucleares, como fissão ou fusão de átomos."},
    {"palavra": "algoritmo",
     "dica": "Sequência de passos ou regras definidas para realizar uma tarefa ou resolver um problema."},
    {"palavra": "fotografia", "dica": "Arte de capturar imagens usando luz e outros meios."},
    {"palavra": "astronauta", "dica": "Profissional treinado para viajar e realizar atividades no espaço."},
    {"palavra": "patrimônio cultural",
     "dica": "Bens materiais e imateriais que representam a herança cultural de uma sociedade."},
    {"palavra": "empatia", "dica": "Capacidade de compreender e compartilhar os sentimentos de outra pessoa."},
    {"palavra": "nanotecnologia",
     "dica": "Manipulação de materiais em escala nanométrica para criar novos produtos e tecnologias."},
    {"palavra": "energia solar", "dica": "Geração de eletricidade usando a luz do sol por meio de painéis solares."},
    {"palavra": "engenharia genética",
     "dica": "Manipulação dos genes de organismos para obter características desejadas."},
    {"palavra": "inteligência artificial",
     "dica": "Desenvolvimento de sistemas capazes de realizar tarefas que normalmente requerem inteligência humana."},
    {"palavra": "mente humana",
     "dica": "Conjunto complexo de processos mentais, incluindo pensamento, memória e emoções."},
    {"palavra": "paleontologia", "dica": "Estudo dos fósseis e da vida pré-histórica."},
    {"palavra": "energia eólica",
     "dica": "Geração de eletricidade usando a força do vento por meio de turbinas eólicas."},
    {"palavra": "teoria da relatividade",
     "dica": "Teoria desenvolvida por Albert Einstein que descreve a relação entre espaço e tempo."},
    {"palavra": "arte abstrata",
     "dica": "Forma de expressão artística que não tenta representar a realidade de maneira objetiva."},
    {"palavra": "coronavírus", "dica": "Família de vírus que pode causar infecções respiratórias em seres humanos e animais."},
    {"palavra": "energia hidrelétrica", "dica": "Geração de eletricidade a partir da energia cinética da água em movimento."},
    {"palavra": "alimentação saudável", "dica": "Prática de escolher alimentos nutritivos para manter uma boa saúde."},
    {"palavra": "tecnologia blockchain", "dica": "Sistema descentralizado de registro de transações usado em criptomoedas."},
    {"palavra": "inteligência emocional", "dica": "Habilidade de reconhecer, compreender e gerenciar as próprias emoções e as dos outros."},
    {"palavra": "engajamento cívico", "dica": "Participação ativa dos cidadãos na vida política e social de sua comunidade."},
    {"palavra": "efeito estufa", "dica": "Fenômeno natural que retém parte do calor do Sol na atmosfera da Terra."},
    {"palavra": "realidade virtual", "dica": "Ambiente simulado por computador que proporciona uma experiência imersiva."},
    {"palavra": "células-tronco", "dica": "Células com a capacidade de se diferenciar em diversos tipos celulares no organismo."},
    {"palavra": "dívida pública", "dica": "Quantidade de dinheiro que um governo deve a credores, geralmente representada por títulos."},
    {"palavra": "teoria da evolução", "dica": "Ideia científica que explica o processo pelo qual as espécies mudam ao longo do tempo."},
    {"palavra": "engenharia civil", "dica": "Campo da engenharia que lida com design, construção e manutenção de infraestruturas."},
    {"palavra": "empatia", "dica": "Capacidade de se colocar no lugar de outra pessoa e entender seus sentimentos."},
    {"palavra": "comércio justo", "dica": "Modelo de comércio que busca garantir condições justas e equitativas para produtores."},
    {"palavra": "teoria das cordas", "dica": "Modelo teórico na física que sugere que as partículas fundamentais são cordas vibrantes."},
    {"palavra": "efeito placebo", "dica": "Melhoria percebida em uma condição médica devido à crença de que um tratamento é eficaz."},
    {"palavra": "inteligência artificial ética", "dica": "Desenvolvimento de IA com considerações éticas para garantir decisões justas e seguras."},
    {"palavra": "teoria do caos", "dica": "Campo da matemática que estuda sistemas complexos e seu comportamento imprevisível."},
    {"palavra": "tecnologia 5G", "dica": "Geração avançada de redes móveis com maior velocidade e capacidade de conexão."},
    {"palavra": "desenvolvimento sustentável", "dica": "Abordagem que busca atender às necessidades atuais sem comprometer as futuras gerações."},
    {"palavra": "neurociência", "dica": "Estudo do sistema nervoso, incluindo o cérebro, nervos e outras estruturas."},
    {"palavra": "teoria do Big Bang", "dica": "Modelo cosmológico que descreve a origem do universo a partir de uma explosão inicial."},
    {"palavra": "cultura pop", "dica": "Elementos culturais predominantes na sociedade, como música, filmes e moda."},
    {"palavra": "energia geotérmica", "dica": "Geração de energia a partir do calor interno da Terra."},
    {"palavra": "nebulosa", "dica": "Massa de gás e poeira no espaço, frequentemente o local de formação de estrelas."},
    {"palavra": "mindfulness", "dica": "Prática de estar consciente e presente no momento atual."},
    {"palavra": "alimentação orgânica", "dica": "Produção de alimentos sem o uso de pesticidas e fertilizantes sintéticos."},
    {"palavra": "economia circular", "dica": "Modelo econômico que visa minimizar resíduos e promover a reutilização de recursos."},
]

# Inicializa o enigma atual e a pontuação do jogador
enigma_atual = {}
enigma_resolvido = []
pontuacao = 0

def inicializar_enigma():
    global enigma_atual, enigma_resolvido
    enigma_atual = random.choice(enigmas_com_dicas)
    enigma_resolvido = ["_"] * len(enigma_atual['palavra'])

@app.route('/')
def index():
    global pontuacao
    inicializar_enigma()
    pontuacao = 0
    return render_template('index.html', enigma=" ".join(enigma_resolvido), dica=enigma_atual['dica'], pontuacao=pontuacao)

@app.route('/verificar_palpite', methods=['POST'])
def verificar_palpite():
    global enigma_resolvido, pontuacao

    palpite = request.form['palpite'].lower()

    if palpite == enigma_atual['palavra']:
        feedback = "Parabéns! Você acertou!"
        pontuacao += 1  # Aumenta a pontuação
        inicializar_enigma()
    else:
        feedback = "Ops! Tente novamente."

    return jsonify({'feedback': feedback, 'enigma': " ".join(enigma_resolvido), 'dica': enigma_atual['dica'], 'pontuacao': pontuacao})

if __name__ == '__main__':
    app.run(debug=True)
