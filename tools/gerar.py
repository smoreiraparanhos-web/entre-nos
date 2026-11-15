#!/usr/bin/env python3
"""Gera as páginas estáticas do Entre Nós (cabeçalho e rodapé compartilhados)."""
import json, sys, html
from pathlib import Path

RAIZ = Path(sys.argv[1])
HOJE = "2026-11-15"

CATEGORIAS = {
    "ansiedade": "Ansiedade",
    "depressao": "Depressão",
    "solidao": "Solidão",
    "luto": "Luto",
    "relacionamentos": "Relacionamentos",
    "autoestima": "Autoestima",
    "esgotamento": "Esgotamento emocional",
    "autoconhecimento": "Autoconhecimento",
    "cotidiano": "Saúde emocional no cotidiano",
}

F = {
    "oms_ansiedade": {"nome": "Organização Mundial da Saúde (OMS). Anxiety disorders — ficha informativa.", "url": "https://www.who.int/news-room/fact-sheets/detail/anxiety-disorders"},
    "oms_depressao": {"nome": "Organização Mundial da Saúde (OMS). Depressive disorder (depression) — ficha informativa.", "url": "https://www.who.int/news-room/fact-sheets/detail/depression"},
    "oms_saude_mental": {"nome": "Organização Mundial da Saúde (OMS). Mental health: strengthening our response — ficha informativa.", "url": "https://www.who.int/news-room/fact-sheets/detail/mental-health-strengthening-our-response"},
    "oms_burnout": {"nome": "Organização Mundial da Saúde (OMS). Burn-out an “occupational phenomenon”: International Classification of Diseases (2019).", "url": "https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases"},
    "oms_conexao": {"nome": "Organização Mundial da Saúde (OMS). Commission on Social Connection.", "url": "https://www.who.int/groups/commission-on-social-connection"},
    "oms_suicidio": {"nome": "Organização Mundial da Saúde (OMS). Suicide — ficha informativa.", "url": "https://www.who.int/news-room/fact-sheets/detail/suicide"},
    "ms_depressao": {"nome": "Ministério da Saúde. Depressão — Saúde de A a Z.", "url": "https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/d/depressao"},
    "ms_saude_mental": {"nome": "Ministério da Saúde. Saúde mental — Saúde de A a Z.", "url": "https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/s/saude-mental"},
    "cvv": {"nome": "Centro de Valorização da Vida (CVV).", "url": "https://cvv.org.br/"},
}

def artigo(slug, titulo, categoria, leitura, intro, secoes, fontes):
    return {"slug": slug, "titulo": titulo, "categoria": categoria, "leitura": leitura, "intro": intro,
            "autoria": "Equipe Entre Nós", "publicado": HOJE, "revisado": None, "revisor": None,
            "secoes": [{"titulo": t, "blocos": b} for t, b in secoes], "fontes": [F[k] for k in fontes]}

ARTIGOS = [
artigo("o-que-e-ansiedade", "O que é ansiedade e como ela pode se manifestar?", "ansiedade", 4,
 "A ansiedade faz parte da experiência humana. Entender como ela aparece no corpo, nos pensamentos e no comportamento ajuda a reconhecer quando ela pede mais atenção.",
 [(None, [
   "Sentir ansiedade antes de uma prova, de uma conversa difícil ou de uma mudança importante é uma reação esperada. Ela prepara o corpo para lidar com algo percebido como desafio ou ameaça, e costuma diminuir quando a situação passa.",
   "A ansiedade passa a merecer mais cuidado quando é intensa, dura muito tempo, aparece sem um motivo claro ou atrapalha o trabalho, os estudos, o sono e os relacionamentos."]),
  ("Como ela pode se manifestar", [
   "A ansiedade não é igual para todo mundo. Segundo a Organização Mundial da Saúde, ela pode envolver sinais como:",
   ["No corpo: coração acelerado, tensão muscular, tremores, suor, falta de ar, desconforto no estômago e dificuldade para dormir.",
    "Nos pensamentos: preocupação excessiva e difícil de controlar, sensação de que algo ruim vai acontecer, dificuldade de concentração.",
    "No comportamento: irritabilidade, inquietação e a tendência de evitar situações que despertam medo."],
   "Ter alguns desses sinais em um momento de pressão não significa ter um transtorno de ansiedade. Essa avaliação só pode ser feita por um profissional, que considera a intensidade, a duração e o impacto na vida da pessoa."]),
  ("Quando procurar ajuda", [
   "Vale conversar com um profissional de saúde quando a ansiedade se repete por semanas, quando você passa a evitar atividades de que precisa ou gosta, ou quando os sintomas físicos assustam.",
   "Os transtornos de ansiedade estão entre as condições de saúde mental mais comuns no mundo e existem tratamentos com eficácia reconhecida, como a psicoterapia e, em alguns casos, medicação prescrita por médico. Procurar ajuda não é exagero: é uma forma de cuidado."])],
 ["oms_ansiedade", "ms_saude_mental"]),

artigo("tristeza-ou-depressao", "Como diferenciar tristeza de sintomas de depressão?", "depressao", 4,
 "Tristeza é uma emoção. Depressão é uma condição de saúde. As duas podem se parecer por fora, mas se diferenciam pela duração, pela intensidade e pelo quanto afetam a vida.",
 [(None, [
   "Ficar triste depois de uma perda, de uma decepção ou de um período difícil é uma resposta humana e esperada. A tristeza costuma ter relação com algo que aconteceu, varia ao longo dos dias e convive com momentos de alívio.",
   "A depressão é diferente das variações normais de humor. Ela não é fraqueza, falta de vontade ou algo que se resolve apenas pensando positivo."]),
  ("O que caracteriza um episódio depressivo", [
   "De acordo com a Organização Mundial da Saúde, em um episódio depressivo a pessoa apresenta humor deprimido (tristeza, irritação, sensação de vazio) ou perda de prazer e interesse pelas atividades, na maior parte do dia, quase todos os dias, por pelo menos duas semanas.",
   "Outros sinais podem estar presentes:",
   ["Dificuldade de concentração.", "Culpa excessiva ou baixa autoestima.", "Falta de esperança em relação ao futuro.",
    "Alterações no sono, no apetite ou no peso.", "Cansaço intenso e falta de energia.", "Pensamentos sobre morte ou suicídio."],
   "Esta lista serve para informar, não para se autodiagnosticar. Só uma avaliação profissional pode dizer se há depressão e qual é o cuidado indicado."]),
  ("O que observar em si", [
   "Três perguntas ajudam a decidir se é hora de buscar apoio: há quanto tempo estou assim? Isso está atrapalhando o que eu preciso ou gostaria de fazer? Perdi o interesse por coisas que antes me faziam bem?",
   "Se a resposta preocupa, procure uma Unidade Básica de Saúde, um CAPS ou um profissional de saúde mental. A depressão tem tratamento, que pode incluir psicoterapia e medicação.",
   "Se houver pensamentos de morte ou de se machucar, não espere: ligue para o CVV no 188 (gratuito, 24 horas) ou procure um serviço de emergência."])],
 ["oms_depressao", "ms_depressao", "cvv"]),

artigo("sozinho-mesmo-acompanhado", "Por que algumas pessoas se sentem sozinhas mesmo acompanhadas?", "solidao", 3,
 "Solidão não é o mesmo que estar só. É possível ter a agenda cheia e a casa cheia e, ainda assim, sentir falta de conexão.",
 [(None, [
   "Costuma-se distinguir duas coisas. O isolamento social é objetivo: ter poucos contatos e poucas relações. A solidão é subjetiva: é o desconforto que surge quando as relações que temos não correspondem às que gostaríamos de ter.",
   "Por isso alguém pode viver sozinho e sentir-se bem, e outra pessoa pode estar cercada de gente e sentir-se só."]),
  ("O que costuma estar por trás", [
   "Sentir-se sozinho acompanhado geralmente tem menos a ver com a quantidade de pessoas e mais com a qualidade do vínculo:",
   ["Conversas que ficam na superfície, sem espaço para o que realmente importa.",
    "A sensação de precisar esconder partes de si para ser aceito.",
    "Mudanças de fase (cidade nova, maternidade ou paternidade, luto, aposentadoria) que afastam a pessoa de quem a entendia.",
    "Relações em que se oferece muita escuta e se recebe pouca."]]),
  ("É mais comum do que parece", [
   "A Organização Mundial da Saúde passou a tratar a conexão social como tema de saúde pública e estima que a solidão atinja cerca de uma em cada seis pessoas no mundo. Sentir-se só não é um defeito pessoal.",
   "Alguns caminhos possíveis: aprofundar um vínculo que já existe em vez de buscar muitos novos, dizer a alguém de confiança como você tem se sentido e participar de atividades regulares com interesses em comum. Se a solidão vier acompanhada de tristeza persistente ou desesperança, vale procurar apoio profissional."])],
 ["oms_conexao", "oms_saude_mental"]),

artigo("periodos-dificeis", "Como lidar com períodos emocionalmente difíceis?", "cotidiano", 4,
 "Não existe fórmula para atravessar uma fase difícil, e ninguém precisa atravessá-la no ritmo dos outros. Algumas atitudes simples, porém, costumam aliviar o peso.",
 [(None, [
   "Períodos difíceis fazem parte da vida: perdas, mudanças, sobrecarga, incertezas. Senti-los não é sinal de fraqueza. A saúde mental, como lembra a Organização Mundial da Saúde, não é a ausência de dificuldades, e sim a capacidade de lidar com as tensões da vida, que varia ao longo do tempo."]),
  ("O que costuma ajudar", [
   ["Dar nome ao que sente. Dizer “estou com medo” ou “estou exausto” já organiza um pouco a experiência.",
    "Manter o básico, mesmo que imperfeito: algum sono, alguma alimentação, algum movimento.",
    "Reduzir o que for possível. Em fases difíceis, fazer menos é uma decisão sensata, não uma falha.",
    "Falar com alguém de confiança. Não é preciso ter uma solução para merecer ser ouvido.",
    "Diminuir o álcool e outras substâncias, que tendem a piorar o humor e o sono.",
    "Reservar pequenas pausas ao longo do dia, sem cobrança de resultado."],
   "Nenhuma dessas atitudes resolve a causa do sofrimento. Elas ajudam a atravessar o período com um pouco mais de sustentação."]),
  ("Quando o período não passa", [
   "Procure ajuda profissional se o sofrimento durar semanas sem alívio, se estiver difícil cumprir as atividades do dia a dia ou se surgirem pensamentos de desistir de tudo.",
   "A porta de entrada no SUS é a Unidade Básica de Saúde. Em sofrimento intenso, os CAPS acolhem diretamente. E o CVV atende pelo 188, a qualquer hora, para quem precisa conversar."])],
 ["oms_saude_mental", "ms_saude_mental", "cvv"]),

artigo("esgotamento-emocional", "O que é esgotamento emocional?", "esgotamento", 4,
 "Um cansaço que o descanso do fim de semana não resolve. O esgotamento emocional aparece quando a exigência é maior que a capacidade de recuperação por tempo demais.",
 [(None, [
   "“Esgotamento emocional” não é um diagnóstico formal. É uma expressão usada para descrever a sensação de estar sem reserva: sem energia, sem paciência e sem disposição para aquilo que antes era possível fazer.",
   "Ele pode surgir no trabalho, mas também no cuidado prolongado de um familiar, na sobrecarga doméstica ou em longos períodos de preocupação."]),
  ("E o burnout?", [
   "O termo mais conhecido é burnout. Na Classificação Internacional de Doenças (CID-11), a Organização Mundial da Saúde o descreve como um fenômeno ocupacional, resultante de estresse crônico no trabalho que não foi administrado com sucesso. Ele não é classificado como uma condição médica e se refere especificamente ao contexto de trabalho.",
   "A OMS o caracteriza por três dimensões:",
   ["Sensação de esgotamento ou falta de energia.",
    "Distanciamento mental do trabalho, ou sentimentos de negativismo e cinismo em relação a ele.",
    "Redução da eficácia profissional."]]),
  ("Sinais para observar", [
   ["Cansaço que não melhora com o descanso habitual.", "Irritação com situações pequenas.",
    "Dificuldade de concentração e esquecimentos.", "Sensação de fazer tudo no automático.",
    "Dores e alterações de sono sem outra explicação."],
   "Esses sinais também podem estar presentes em outras condições, como depressão e ansiedade. Por isso, quando persistem, o melhor caminho é uma avaliação profissional."]),
  ("O que pode ser feito", [
   "O esgotamento raramente é apenas um problema individual: muitas vezes ele reflete condições de trabalho ou de vida que precisam mudar. Conversar sobre carga e limites, pedir ajuda para dividir responsabilidades e recuperar tempos de descanso reais são passos importantes. Se os sinais continuarem, procure um profissional de saúde."])],
 ["oms_burnout", "oms_saude_mental"]),

artigo("como-procurar-ajuda-psicologica", "Como procurar ajuda psicológica?", "cotidiano", 4,
 "Decidir procurar ajuda já é um passo. Saber por onde começar torna o seguinte mais fácil.",
 [(None, [
   "Não é preciso estar em crise para procurar apoio psicológico. Muitas pessoas buscam ajuda para atravessar uma fase, entender padrões que se repetem ou simplesmente ter um espaço para falar."]),
  ("Quem faz o quê", [
   ["Psicólogo(a): profissional formado em Psicologia e registrado no Conselho Regional de Psicologia (CRP). Conduz a psicoterapia.",
    "Psiquiatra: médico(a) especializado em saúde mental. Faz diagnóstico médico e pode prescrever medicação.",
    "Os dois cuidados se complementam e, em muitos casos, acontecem juntos."]]),
  ("Caminhos pelo SUS", [
   ["Unidade Básica de Saúde (UBS): é a porta de entrada. A equipe acolhe, acompanha e encaminha quando necessário.",
    "Centro de Atenção Psicossocial (CAPS): atende pessoas em sofrimento psíquico intenso. Em geral, é possível ir diretamente, sem encaminhamento.",
    "A oferta de serviços varia de um município para outro. Na UBS mais próxima é possível saber o que existe na sua região."]]),
  ("Outros caminhos", [
   ["Clínicas-escola de cursos de Psicologia costumam oferecer atendimento gratuito ou a preço reduzido.",
    "Planos de saúde incluem consultas com psicólogos e psiquiatras; consulte as condições do seu.",
    "No atendimento particular, vale perguntar sobre valores e disponibilidade antes de começar."],
   "Ao escolher um psicólogo, confira o registro no CRP. O atendimento on-line é permitido e segue as mesmas regras de sigilo."]),
  ("A primeira conversa", [
   "Não é preciso chegar com tudo organizado. Dizer “não sei bem por onde começar” é um começo válido. Também é normal não se sentir à vontade com o primeiro profissional: o vínculo importa, e trocar faz parte do processo.",
   "Em situação de crise, não espere por uma consulta: ligue 188 (CVV) ou 192 (SAMU, em emergências médicas)."])],
 ["ms_saude_mental", "cvv"]),

artigo("como-apoiar-alguem", "Como apoiar alguém que está passando por dificuldades?", "relacionamentos", 4,
 "Quem acompanha alguém em sofrimento costuma ter medo de dizer a coisa errada. Na maior parte das vezes, estar presente importa mais do que encontrar a frase certa.",
 [("Escutar antes de aconselhar", [
   "A vontade de resolver é natural, mas conselhos rápidos podem soar como pressa para que a pessoa melhore. Escutar com atenção, sem interromper e sem comparar com outras histórias, já é uma forma concreta de ajuda.",
   ["Em vez de “isso passa” ou “pense positivo”, experimente: “imagino que esteja sendo difícil”.",
    "Em vez de “você precisa reagir”, experimente: “estou aqui, do jeito que você precisar”.",
    "Em vez de adivinhar, pergunte: “o que te ajudaria agora?”."]]),
  ("Oferecer ajuda concreta", [
   "Ofertas vagas (“qualquer coisa, me avisa”) raramente são aceitas. Propostas específicas funcionam melhor: acompanhar a uma consulta, levar uma refeição, ajudar a marcar um atendimento, fazer companhia em uma caminhada.",
   "Você pode sugerir ajuda profissional sem impor. Respeitar o tempo da pessoa não é desistir dela; é continuar por perto."]),
  ("Se houver risco", [
   "Se a pessoa falar em morrer, em desaparecer ou em não aguentar mais, leve a sério. Segundo a Organização Mundial da Saúde, perguntar diretamente sobre pensamentos de suicídio não incentiva o ato; pode aliviar e abrir espaço para pedir ajuda.",
   "Fique por perto, ajude a procurar atendimento (CAPS, UBS ou pronto-socorro) e lembre que o CVV atende pelo 188, gratuitamente, 24 horas. Em risco imediato, ligue para o SAMU no 192."]),
  ("Cuidar de quem cuida", [
   "Apoiar alguém também cansa. Você não precisa dar conta sozinho nem ter todas as respostas. Dividir o cuidado com outras pessoas e ter o seu próprio espaço de apoio é o que permite continuar presente."])],
 ["oms_suicidio", "oms_depressao", "cvv"]),
]

e = html.escape
FOLHA = '<path d="M46 16C28 16 17 26 17 40c0 3 .6 5.6 1.6 8C22 36 30 28 40 24c-9 6-15 14-18 25 2 .6 4 1 6 1 13 0 20-12 18-34z"/>'
MARCA_SVG = f'<svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#263D32"/><g fill="#DCE6D9">{FOLHA}</g></svg>'

NAV = [("inicio", "Início", "index.html"), ("conhecimento", "Conhecimento", "pages/conhecimento.html"),
       ("momentos", "Momentos", "pages/momentos.html"), ("ajuda", "Encontrar ajuda", "pages/encontrar-ajuda.html"),
       ("sobre", "Sobre", "pages/sobre.html")]

def pagina(caminho, titulo, descricao, corpo, atual=None, scripts=()):
    na_raiz = "/" not in caminho
    r = "" if na_raiz else "../"
    def u(destino):  # destino relativo à raiz do site
        return destino if na_raiz else ("../" + destino if not destino.startswith("pages/") else destino[len("pages/"):])
    corpo = corpo.replace("{{r}}", r)
    for chave in ("index.html", "pages/conhecimento.html", "pages/artigo.html", "pages/momentos.html",
                  "pages/encontrar-ajuda.html", "pages/sobre.html", "pages/privacidade.html", "pages/responsabilidade.html"):
        corpo = corpo.replace("{{" + chave + "}}", u(chave))
    itens = "\n".join(
        f'            <li><a href="{u(h)}"{" aria-current=\"page\"" if k == atual else ""}>{n}</a></li>' for k, n, h in NAV)
    tags = "\n".join(f'  <script src="{r}js/{s}" defer></script>' for s in ("main.js", "navigation.js") + tuple(scripts))
    titulo_completo = titulo if "Entre Nós" in titulo else f"{titulo} — Entre Nós"
    doc = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(titulo_completo)}</title>
  <meta name="description" content="{e(descricao)}">
  <meta name="theme-color" content="#263D32">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Entre Nós">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:title" content="{e(titulo_completo)}">
  <meta property="og:description" content="{e(descricao)}">
  <link rel="icon" href="{r}assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{r}css/reset.css">
  <link rel="stylesheet" href="{r}css/variables.css">
  <link rel="stylesheet" href="{r}css/global.css">
  <link rel="stylesheet" href="{r}css/components.css">
  <link rel="stylesheet" href="{r}css/responsive.css">
{tags}
</head>
<body>
  <a class="pular" href="#conteudo">Pular para o conteúdo</a>

  <header class="topo">
    <div class="container topo__linha">
      <a class="marca" href="{u("index.html")}" aria-label="Entre Nós — página inicial">{MARCA_SVG}<span>Entre Nós</span></a>
      <button class="menu-botao" type="button" aria-expanded="false" aria-controls="nav-principal">Menu</button>
      <nav class="nav" id="nav-principal" aria-label="Navegação principal">
        <ul class="nav__lista">
{itens}
        </ul>
      </nav>
    </div>
  </header>

  <main id="conteudo">
{corpo.strip(chr(10))}
  </main>

  <aside class="apoio-faixa" aria-label="Apoio imediato">
    <div class="container">
      Precisa conversar agora? O <strong>CVV</strong> atende pelo <a href="tel:188">188</a>, gratuitamente, 24 horas. Em emergência médica, ligue <a href="tel:192">192</a> (SAMU). <a href="{u("pages/encontrar-ajuda.html")}">Ver todos os caminhos de ajuda</a>
    </div>
  </aside>

  <footer class="rodape">
    <div class="container">
      <div class="rodape__grade">
        <div>
          <p class="rodape__marca">Entre Nós</p>
          <p>Um espaço para cuidar do que sentimos.</p>
          <p style="margin-top:.75rem;max-width:26rem">Conteúdo informativo. Não substitui avaliação, diagnóstico ou acompanhamento profissional.</p>
        </div>
        <nav aria-label="Seções">
          <h2>Navegar</h2>
          <ul class="rodape__lista">
            <li><a href="{u("pages/conhecimento.html")}">Conhecimento</a></li>
            <li><a href="{u("pages/momentos.html")}">Momentos</a></li>
            <li><a href="{u("pages/encontrar-ajuda.html")}">Encontrar ajuda</a></li>
          </ul>
        </nav>
        <nav aria-label="Institucional">
          <h2>O projeto</h2>
          <ul class="rodape__lista">
            <li><a href="{u("pages/sobre.html")}">Sobre</a></li>
            <li><a href="{u("pages/privacidade.html")}">Privacidade</a></li>
            <li><a href="{u("pages/responsabilidade.html")}">Responsabilidade editorial</a></li>
          </ul>
        </nav>
      </div>
      <p class="rodape__fim">© <span data-ano>2026</span> Entre Nós. Este site não usa cookies nem coleta dados pessoais.</p>
    </div>
  </footer>
</body>
</html>
'''
    destino = RAIZ / caminho
    destino.write_text(doc, encoding="utf-8")

def cartao(a, nivel="h3"):
    return f'''        <article class="cartao" data-categoria="{a["categoria"]}">
          <span class="etiqueta">{e(CATEGORIAS[a["categoria"]])}</span>
          <{nivel}><a href="{{{{pages/artigo.html}}}}?id={a["slug"]}">{e(a["titulo"])}</a></{nivel}>
          <p>{e(a["intro"])}</p>
          <p class="cartao__meta">{a["leitura"]} min de leitura</p>
        </article>'''

def cabecalho(sobre, titulo, lead):
    return f'''    <div class="cabecalho-pagina">
      <div class="container">
        <span class="sobretitulo">{sobre}</span>
        <h1>{titulo}</h1>
        <p class="lead">{lead}</p>
      </div>
    </div>'''

PAISAGEM = '''<svg class="hero__paisagem" viewBox="0 0 1200 300" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
        <circle cx="930" cy="110" r="54" fill="#E9DDC4"/>
        <path d="M0 190 C160 120 300 150 450 175 S760 110 930 150 1130 130 1200 150 V300 H0Z" fill="#DCE6D9"/>
        <path d="M0 230 C140 180 260 215 420 205 S700 165 860 200 1080 180 1200 205 V300 H0Z" fill="#9DB3A1"/>
        <g fill="#526F5B">
          <path d="M0 262 C180 228 330 258 520 246 S820 222 1000 250 1140 240 1200 248 V300 H0Z"/>
          <path d="M150 250 l14 -46 14 46z M178 252 l11 -34 11 34z M960 246 l15 -52 15 52z M992 248 l11 -36 11 36z M1030 250 l9 -28 9 28z"/>
        </g>
        <path d="M0 284 C220 262 420 286 640 276 S1000 268 1200 282 V300 H0Z" fill="#263D32"/>
      </svg>'''

# ---------- Início ----------
destaques = "\n".join(cartao(a) for a in ARTIGOS if a["slug"] in ("o-que-e-ansiedade", "como-procurar-ajuda-psicologica", "como-apoiar-alguem"))
cats = "\n".join(f'          <li><a href="{{{{pages/conhecimento.html}}}}?categoria={k}">{e(v)}</a></li>' for k, v in CATEGORIAS.items())
pagina("index.html", "Entre Nós — Um espaço para cuidar do que sentimos",
 "Plataforma de saúde emocional com informação confiável, exercícios de pausa e caminhos de apoio. Gratuita, sem cadastro e sem coleta de dados.",
 f'''    <section class="hero">
      <div class="container">
        <div class="hero__conteudo">
          <span class="sobretitulo">Saúde emocional</span>
          <h1>Um espaço para cuidar do que sentimos.</h1>
          <p class="lead">Informação confiável, pausas para respirar e caminhos de apoio. Sem pressa, sem cadastro e no seu tempo.</p>
          <div class="acoes">
            <a class="botao" href="{{{{pages/conhecimento.html}}}}">Explorar conteúdos</a>
            <a class="botao botao--contorno" href="{{{{pages/momentos.html}}}}">Fazer uma pausa</a>
          </div>
        </div>
      </div>
      {PAISAGEM}
    </section>

    <section class="secao" aria-labelledby="t-caminhos">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="sobretitulo">Por onde começar</span>
          <h2 id="t-caminhos">Três caminhos, conforme o seu momento</h2>
        </div>
        <div class="grade">
          <div class="caminho">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 6c-2-1.5-5-2-8-1.5v13c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.500v-13c-3-.5-6 0-8 1.5zM12 6v13"/></svg>
            <h3>Quero entender</h3>
            <p>Artigos sobre ansiedade, tristeza, solidão, esgotamento e outros temas, com fontes indicadas.</p>
            <a href="{{{{pages/conhecimento.html}}}}">Ir para Conhecimento</a>
          </div>
          <div class="caminho">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 5C11 5 6 9.500 6 15.500c0 1.200.2 2.300.6 3.300M19 5c.8 8.500-2.500 13.500-8 13.500-1.500 0-3-.5-4.400-1.200M19 5c-5 2.500-9 7-12.400 13.800"/></svg>
            <h3>Quero uma pausa</h3>
            <p>Respiração guiada, atenção aos sentidos e perguntas para refletir. Poucos minutos bastam.</p>
            <a href="{{{{pages/momentos.html}}}}">Ir para Momentos</a>
          </div>
          <div class="caminho">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 12.500 5.500 10a3.200 3.200 0 0 1 4.500-4.500l2 2 2-2a3.200 3.200 0 0 1 4.500 4.500L12 16.500l-1.500-1.500M3 14l4 4.500c1 1 2.500 1.500 4 1.500h3"/></svg>
            <h3>Preciso de ajuda</h3>
            <p>Serviços públicos e gratuitos, e como chegar a um atendimento profissional.</p>
            <a href="{{{{pages/encontrar-ajuda.html}}}}">Ir para Encontrar ajuda</a>
          </div>
        </div>
      </div>
    </section>

    <section class="secao secao--areia" aria-labelledby="t-destaques">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="sobretitulo">Em destaque</span>
          <h2 id="t-destaques">Leituras para começar</h2>
        </div>
        <div class="grade">
{destaques}
        </div>
        <div class="acoes"><a class="botao botao--contorno" href="{{{{pages/conhecimento.html}}}}">Ver toda a biblioteca</a></div>
      </div>
    </section>

    <section class="secao" aria-labelledby="t-temas">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="sobretitulo">Temas</span>
          <h2 id="t-temas">Explorar por assunto</h2>
        </div>
        <ul class="categorias">
{cats}
        </ul>
      </div>
    </section>

    <section class="secao secao--verde" aria-labelledby="t-ciclos">
      <div class="container">
        <div class="secao__cabecalho" style="margin-bottom:0">
          <span class="sobretitulo">Nosso jeito de ver</span>
          <h2 id="t-ciclos">Como a natureza, as pessoas têm ciclos</h2>
          <p>Há tempos de crescer, de mudar e de descansar. Tristeza não é fraqueza, e ninguém precisa atravessar uma fase difícil no ritmo dos outros. O Entre Nós não existe para ensinar a ser feliz o tempo inteiro: existe para oferecer conhecimento, acolhimento e caminhos de cuidado.</p>
          <div class="acoes"><a class="botao" href="{{{{pages/sobre.html}}}}">Conhecer o projeto</a></div>
        </div>
      </div>
    </section>''', atual="inicio")

# ---------- Conhecimento ----------
filtros = '          <button class="filtro" type="button" data-filtro="todas" aria-pressed="true">Todas</button>\n' + "\n".join(
    f'          <button class="filtro" type="button" data-filtro="{k}" aria-pressed="false">{e(v)}</button>' for k, v in CATEGORIAS.items())
todos = "\n".join(cartao(a, "h2") for a in ARTIGOS).replace("<h2>", '<h2 style="font-size:var(--t-lg)">')
pagina("pages/conhecimento.html", "Conhecimento", "Biblioteca de conteúdos sobre saúde emocional: ansiedade, depressão, solidão, esgotamento, relacionamentos e mais, com fontes indicadas.",
 cabecalho("Biblioteca", "Conhecimento", "Textos para compreender melhor o que sentimos. Cada artigo indica autoria, fontes e situação de revisão.") + f'''
    <section class="secao">
      <div class="container">
        <div class="busca" role="search">
          <div>
            <label for="busca-artigos">Buscar artigos</label>
            <input type="search" id="busca-artigos" placeholder="Ex.: ansiedade, sono, apoio" autocomplete="off">
          </div>
          <div class="filtros" role="group" aria-label="Filtrar por categoria">
{filtros}
          </div>
        </div>
        <p class="resultado-info" id="resultado-info" role="status" aria-live="polite"></p>
        <div class="grade" id="lista-artigos">
{todos}
        </div>
        <div class="vazio" id="sem-resultados" hidden>
          <h2 style="font-size:var(--t-lg)">Ainda não há conteúdos aqui</h2>
          <p style="margin-top:.5rem">Não encontramos artigos para essa busca ou categoria. A biblioteca está em construção, e cada texto só é publicado depois de verificado.</p>
          <div class="acoes"><button class="botao botao--contorno botao--pequeno" type="button" id="limpar-busca">Ver todos os artigos</button></div>
        </div>
      </div>
    </section>''', atual="conhecimento", scripts=("search.js",))

# ---------- Artigo ----------
lista_noscript = "\n".join(f'            <li>{e(a["titulo"])}</li>' for a in ARTIGOS)
pagina("pages/artigo.html", "Artigo", "Leitura de artigo da biblioteca do Entre Nós.",
 f'''    <div class="container artigo">
      <p style="margin-bottom:var(--e-4)"><a class="voltar" href="{{{{pages/conhecimento.html}}}}">← Voltar para Conhecimento</a></p>
      <article id="artigo"></article>
      <div class="vazio" id="artigo-ausente" hidden>
        <h1 style="font-size:var(--t-xl)">Artigo não encontrado</h1>
        <p style="margin-top:.5rem">O endereço pode estar incompleto ou o conteúdo pode ter sido movido.</p>
        <div class="acoes"><a class="botao" href="{{{{pages/conhecimento.html}}}}">Ir para a biblioteca</a></div>
      </div>
      <noscript>
        <div class="vazio">
          <h1 style="font-size:var(--t-xl)">Esta leitura precisa de JavaScript</h1>
          <p style="margin-top:.5rem">Os artigos são montados no navegador. Ative o JavaScript para ler, ou volte para a <a href="{{{{pages/conhecimento.html}}}}">biblioteca</a>.</p>
        </div>
      </noscript>
    </div>
    <section class="secao secao--areia relacionados" id="relacionados" aria-labelledby="t-rel" hidden>
      <div class="container">
        <div class="secao__cabecalho"><h2 id="t-rel">Conteúdos relacionados</h2></div>
        <div class="grade" id="relacionados-lista"></div>
      </div>
    </section>''', atual="conhecimento", scripts=("data/articles.js", "article.js"))

# ---------- Momentos ----------
pagina("pages/momentos.html", "Um momento para mim", "Exercícios simples de respiração, atenção aos sentidos, pausa e reflexão. Nada é registrado.",
 cabecalho("Momentos", "Um momento para mim", "Pequenas pausas para fazer agora, no seu ritmo. Nada do que você fizer aqui é registrado ou enviado.") + '''
    <section class="secao">
      <div class="container">
        <p class="aviso" style="max-width:44rem;margin-bottom:var(--e-5)"><strong>Um cuidado:</strong> estes exercícios são convites de pausa, não tratamentos. Se algum deles causar desconforto, pare. Em sofrimento intenso, veja <a href="{{pages/encontrar-ajuda.html}}">Encontrar ajuda</a>.</p>

        <section class="exercicio" id="ex-respiracao" aria-labelledby="t-resp">
          <span class="etiqueta">2 minutos</span>
          <h2 id="t-resp" style="margin-top:var(--e-2)">Respiração guiada</h2>
          <p>Acompanhe o círculo: inspire enquanto ele cresce, por 4 segundos, e solte o ar enquanto ele diminui, por 6. Se o ritmo não for confortável, respire do seu jeito.</p>
          <div class="exercicio__palco">
            <div class="respiro" aria-hidden="true"></div>
            <p class="palco__fase" aria-live="polite">Quando quiser, comece.</p>
            <p class="palco__apoio"></p>
            <div class="acoes"><button class="botao" type="button" data-acao="alternar">Começar</button></div>
          </div>
        </section>

        <section class="exercicio" id="ex-sentidos" aria-labelledby="t-sent">
          <span class="etiqueta">3 minutos</span>
          <h2 id="t-sent" style="margin-top:var(--e-2)">Atenção aos sentidos</h2>
          <p>Um jeito de voltar a atenção para o presente, passando por cada um dos cinco sentidos. Avance quando estiver pronto.</p>
          <div class="exercicio__palco" aria-live="polite">
            <p class="passo__numero" aria-hidden="true">5</p>
            <p class="palco__fase"></p>
            <p class="palco__apoio"></p>
            <div class="acoes">
              <button class="botao botao--contorno" type="button" data-acao="anterior">Anterior</button>
              <button class="botao" type="button" data-acao="proximo">Próximo</button>
            </div>
          </div>
        </section>

        <section class="exercicio" id="ex-pausa" aria-labelledby="t-pausa">
          <span class="etiqueta">1 minuto</span>
          <h2 id="t-pausa" style="margin-top:var(--e-2)">Pausa de um minuto</h2>
          <p>Sessenta segundos sem tarefa nenhuma. Não é preciso esvaziar a mente; basta não fazer nada por um instante.</p>
          <div class="exercicio__palco">
            <p class="palco__fase" aria-live="polite">Um minuto, sem tarefa nenhuma.</p>
            <p class="palco__apoio"></p>
            <div class="barra" role="progressbar" aria-label="Progresso da pausa" aria-valuemin="0" aria-valuemax="60" aria-valuenow="0"><div class="barra__fio"></div></div>
            <div class="acoes"><button class="botao" type="button" data-acao="alternar">Começar</button></div>
          </div>
        </section>

        <section class="exercicio" id="ex-reflexao" aria-labelledby="t-refl">
          <span class="etiqueta">Livre</span>
          <h2 id="t-refl" style="margin-top:var(--e-2)">Uma pergunta para refletir</h2>
          <p>Fique com a pergunta pelo tempo que quiser. Responda em pensamento ou no papel: este site não guarda o que você escreve.</p>
          <div class="exercicio__palco">
            <p class="pergunta" aria-live="polite">Do que eu estou precisando neste momento?</p>
            <div class="acoes"><button class="botao botao--contorno" type="button" data-acao="outra">Outra pergunta</button></div>
          </div>
        </section>
      </div>
    </section>''', atual="momentos", scripts=("exercises.js",))

# ---------- Encontrar ajuda ----------
pagina("pages/encontrar-ajuda.html", "Encontrar ajuda", "Caminhos de apoio em saúde mental no Brasil: CVV 188, SAMU 192, CAPS, UBS e como procurar atendimento psicológico.",
 cabecalho("Apoio", "Encontrar ajuda", "Pedir ajuda é um gesto de cuidado. Aqui estão caminhos públicos e gratuitos de atendimento no Brasil.") + '''
    <section class="secao">
      <div class="container">
        <div class="urgencia">
          <h2>Se você está em crise agora</h2>
          <p>Se há risco imediato à sua vida ou à de outra pessoa, ligue para o SAMU no 192 ou vá ao pronto-socorro mais próximo. Se precisa conversar com alguém neste momento, o CVV atende pelo 188, sem custo, a qualquer hora.</p>
          <div class="acoes">
            <a class="botao botao--claro" href="tel:188">Ligar 188 — CVV</a>
            <a class="botao botao--claro" href="tel:192">Ligar 192 — SAMU</a>
          </div>
        </div>
      </div>
    </section>

    <section class="secao secao--areia" aria-labelledby="t-servicos">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="sobretitulo">Serviços</span>
          <h2 id="t-servicos">Onde procurar atendimento</h2>
        </div>
        <div class="grade">
          <article class="recurso">
            <span class="etiqueta">Apoio emocional · 24 horas</span>
            <p class="recurso__numero">188</p>
            <h3>CVV — Centro de Valorização da Vida</h3>
            <p>Apoio emocional e prevenção do suicídio, por voluntários, com sigilo. A ligação é gratuita em todo o país. Também há atendimento por chat e e-mail no site.</p>
            <a class="botao botao--contorno botao--pequeno" href="https://cvv.org.br/" rel="noopener noreferrer">Acessar cvv.org.br</a>
          </article>
          <article class="recurso">
            <span class="etiqueta etiqueta--terra">Emergência médica · 24 horas</span>
            <p class="recurso__numero">192</p>
            <h3>SAMU</h3>
            <p>Serviço de Atendimento Móvel de Urgência. Para situações com risco à vida, incluindo crises em saúde mental com risco imediato. A ligação é gratuita.</p>
            <a class="botao botao--contorno botao--pequeno" href="tel:192">Ligar 192</a>
          </article>
          <article class="recurso">
            <span class="etiqueta">SUS · sofrimento intenso</span>
            <h3>CAPS — Centro de Atenção Psicossocial</h3>
            <p>Serviço público para pessoas em sofrimento psíquico intenso ou persistente, com equipe multiprofissional. Em geral, recebe diretamente, sem necessidade de encaminhamento.</p>
            <p>Para localizar o CAPS da sua região, consulte a secretaria de saúde do município ou a UBS mais próxima.</p>
          </article>
          <article class="recurso">
            <span class="etiqueta">SUS · porta de entrada</span>
            <h3>UBS — Unidade Básica de Saúde</h3>
            <p>O posto de saúde do seu bairro é o primeiro lugar para falar sobre como você tem se sentido. A equipe acolhe, acompanha e encaminha para outros serviços quando necessário.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="secao">
      <div class="container">
        <div class="prosa">
          <h2 style="margin-top:0">Outros caminhos</h2>
          <ul>
            <li><strong>Clínicas-escola:</strong> cursos de Psicologia de universidades costumam oferecer atendimento gratuito ou a preço reduzido.</li>
            <li><strong>Plano de saúde:</strong> consultas com psicólogos e psiquiatras fazem parte da cobertura; verifique as condições do seu plano.</li>
            <li><strong>Atendimento particular:</strong> ao escolher um psicólogo, confira o registro no Conselho Regional de Psicologia (CRP).</li>
          </ul>
          <p>Quer entender melhor as opções? Leia <a href="{{pages/artigo.html}}?id=como-procurar-ajuda-psicologica">Como procurar ajuda psicológica?</a></p>
          <h2>Se a preocupação é com outra pessoa</h2>
          <p>Fique por perto, escute sem julgar e ajude a pessoa a chegar a um desses serviços. Você também pode ligar para o 188 para se orientar. Leia <a href="{{pages/artigo.html}}?id=como-apoiar-alguem">Como apoiar alguém que está passando por dificuldades?</a></p>
          <p class="aviso">O Entre Nós não oferece atendimento, não responde mensagens e não acompanha casos. Os serviços listados são mantidos por outras instituições, e horários e condições podem variar por região.</p>
        </div>
      </div>
    </section>''', atual="ajuda")

# ---------- Sobre ----------
pagina("pages/sobre.html", "Sobre", "Conheça o propósito, a missão e os valores do Entre Nós, uma plataforma de saúde emocional voltada à informação, ao acolhimento e à conexão.",
 cabecalho("O projeto", "Sobre o Entre Nós", "Uma plataforma de saúde emocional feita para informar, acolher e orientar.") + '''
    <section class="secao">
      <div class="container">
        <div class="prosa">
          <h2 style="margin-top:0">O que somos</h2>
          <p>O Entre Nós é uma plataforma digital dedicada à saúde emocional. Reunimos informação confiável, exercícios simples de pausa e caminhos para quem precisa de apoio.</p>
          <p>Não somos uma clínica virtual, um serviço de diagnóstico nem um substituto da psicoterapia. Somos um ambiente complementar de conhecimento e cuidado.</p>

          <h2>Missão</h2>
          <p>Tornar informações sobre saúde emocional mais acessíveis e oferecer um ambiente digital acolhedor, responsável e humano.</p>

          <h2>Por que a natureza</h2>
          <p>A natureza tem ciclos: períodos de crescimento, de mudança e de descanso. As pessoas também passam por fases emocionais diferentes. Por isso, aqui você não vai encontrar a ideia de que tristeza é fraqueza, de que basta pensar positivo ou de que todos precisam superar dificuldades no mesmo ritmo.</p>

          <h2>Valores</h2>
          <ul>
            <li><strong>Empatia e respeito</strong> pelo tempo e pela realidade de cada pessoa.</li>
            <li><strong>Responsabilidade e honestidade</strong> sobre o que este espaço é e o que ele não é.</li>
            <li><strong>Privacidade:</strong> sem cadastro, sem rastreamento, sem venda de dados.</li>
            <li><strong>Acessibilidade:</strong> leitura confortável em qualquer tela e com tecnologias assistivas.</li>
            <li><strong>Ciência e informação confiável</strong>, com fontes indicadas em cada artigo.</li>
            <li><strong>Humanidade</strong> na forma de falar sobre o que sentimos.</li>
          </ul>

          <h2>O que vem depois</h2>
          <p>Esta é a primeira versão. Estão planejados, para etapas futuras, um diário emocional privado, novas experiências interativas, histórias compartilhadas com consentimento e moderação, e a participação de profissionais na produção e revisão dos conteúdos.</p>

          <h2>Como nos sustentamos</h2>
          <p>A prioridade do projeto é o impacto social. Nenhuma informação pessoal ou emocional será comercializada, e eventuais formas de financiamento não poderão comprometer a independência editorial.</p>

          <p>Saiba mais em <a href="{{pages/responsabilidade.html}}">Responsabilidade editorial</a> e <a href="{{pages/privacidade.html}}">Privacidade</a>.</p>
        </div>
      </div>
    </section>''', atual="sobre")

# ---------- Privacidade ----------
pagina("pages/privacidade.html", "Política de privacidade", "O Entre Nós não usa cookies, não exige cadastro e não coleta dados pessoais. Veja como tratamos a sua privacidade.",
 cabecalho("Transparência", "Política de privacidade", "Em resumo: não pedimos, não coletamos e não guardamos dados pessoais seus.") + f'''
    <section class="secao">
      <div class="container">
        <div class="prosa">
          <p><em>Última atualização: 15 de novembro de 2026.</em></p>

          <h2>O que este site não faz</h2>
          <ul>
            <li>Não exige cadastro, login ou identificação.</li>
            <li>Não usa cookies.</li>
            <li>Não usa ferramentas de análise de audiência, publicidade ou rastreamento.</li>
            <li>Não carrega fontes, scripts ou imagens de serviços de terceiros.</li>
            <li>Não possui formulários que enviem informações.</li>
            <li>Não grava nada no seu navegador.</li>
          </ul>

          <h2>Busca e exercícios</h2>
          <p>A busca de artigos e os exercícios da seção Momentos funcionam inteiramente no seu dispositivo. O que você digita na busca ou faz nos exercícios não é enviado nem armazenado.</p>

          <h2>Hospedagem</h2>
          <p>O site é hospedado no GitHub Pages. Como qualquer serviço de hospedagem, o GitHub pode registrar dados técnicos de acesso, como o endereço IP, para fins de segurança e funcionamento. O Entre Nós não tem acesso a esses registros. Mais informações estão na declaração de privacidade do GitHub.</p>

          <h2>Links externos</h2>
          <p>Os artigos e a página Encontrar ajuda apontam para sites de outras instituições. Ao acessá-los, valem as políticas de privacidade de cada um.</p>

          <h2>LGPD</h2>
          <p>Informações sobre saúde e vida emocional são dados pessoais sensíveis segundo a Lei Geral de Proteção de Dados (Lei nº 13.709/2018). Por isso escolhemos, nesta versão, não coletar nenhum dado. Se uma funcionalidade futura envolver dados pessoais, esta política será atualizada antes, com explicação clara sobre finalidade, base legal e direitos do titular.</p>

          <h2>Mudanças nesta política</h2>
          <p>Qualquer alteração será publicada nesta página, com a data de atualização.</p>
        </div>
      </div>
    </section>''')

# ---------- Responsabilidade ----------
pagina("pages/responsabilidade.html", "Limites e responsabilidade editorial", "Como os conteúdos do Entre Nós são produzidos e revisados, e quais são os limites deste espaço.",
 cabecalho("Transparência", "Limites e responsabilidade editorial", "O que você pode esperar deste espaço, e o que ele não pode oferecer.") + '''
    <section class="secao">
      <div class="container">
        <div class="prosa">
          <h2 style="margin-top:0">Os limites deste espaço</h2>
          <ul>
            <li>O conteúdo é informativo e educativo. Não substitui consulta, avaliação, diagnóstico ou tratamento com profissionais de saúde.</li>
            <li>Não fazemos diagnósticos, testes ou classificações, automáticos ou não.</li>
            <li>Não prometemos cura nem resultados.</li>
            <li>Não oferecemos atendimento individual e não respondemos a situações de crise.</li>
          </ul>
          <p class="aviso"><strong>Em crise?</strong> Ligue 188 (CVV, 24 horas, gratuito) ou 192 (SAMU, emergências médicas). Veja <a href="{{pages/encontrar-ajuda.html}}">Encontrar ajuda</a>.</p>

          <h2>Como os conteúdos são produzidos</h2>
          <ul>
            <li><strong>Fontes:</strong> os artigos se baseiam em fontes científicas e institucionais, como a Organização Mundial da Saúde e o Ministério da Saúde, listadas ao final de cada texto.</li>
            <li><strong>Autoria e datas:</strong> cada artigo indica quem escreveu, quando foi publicado e quando foi revisado.</li>
            <li><strong>Revisão profissional:</strong> conteúdos com informação clínica devem ser revisados por profissional de saúde mental. Enquanto isso não acontece, o artigo exibe o aviso “Conteúdo em revisão”.</li>
            <li><strong>Linguagem:</strong> evitamos dramatização, culpa e simplificações como “basta pensar positivo”.</li>
          </ul>

          <h2>Situação atual dos artigos</h2>
          <p>Nesta primeira versão, todos os artigos foram redigidos a partir das fontes indicadas e <strong>aguardam revisão profissional</strong>. Essa situação aparece no topo de cada texto e será atualizada à medida que as revisões forem concluídas.</p>

          <h2>Correções</h2>
          <p>Informações em saúde mudam. Quando um conteúdo for corrigido ou atualizado, a data de revisão será alterada no próprio artigo.</p>

          <h2>Independência</h2>
          <p>O Entre Nós não recebe pagamento para recomendar profissionais, serviços, medicamentos ou produtos. Os serviços indicados em Encontrar ajuda são públicos ou sem fins lucrativos.</p>
        </div>
      </div>
    </section>''')

# ---------- Dados dos artigos ----------
dados = {"categorias": CATEGORIAS, "artigos": ARTIGOS}
(RAIZ / "js/data/articles.js").write_text(
    "/* articles.js — conteúdo da biblioteca.\n"
    "   Para publicar um artigo: adicione um objeto em \"artigos\" e um cartão em pages/conhecimento.html.\n"
    "   \"revisado\": data ISO da revisão profissional (null = aguardando revisão); \"revisor\": nome e registro. */\n"
    "window.ENTRE_NOS = " + json.dumps(dados, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")
print("ok")
