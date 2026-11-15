#!/usr/bin/env python3
"""Gera as páginas estáticas do Entre Nós (cabeçalho e rodapé compartilhados)."""
import json, sys, html, re
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

# =====================================================================
# Configuração do site
# =====================================================================
SITE_URL = "https://smoreiraparanhos-web.github.io/entre-nos/"   # endereço público (canônico, sitemap)
BASE_PATH = "/entre-nos/"                                         # subcaminho no GitHub Pages (usado só no 404)
# Imagem principal do início. Para usar uma fotografia, coloque o arquivo em assets/images/
# e troque os valores abaixo (arquivo, descrição e crédito).
HERO = {"arquivo": "hero.svg", "alt": "", "credito": ""}

import re
CONTEUDO = Path(__file__).parent / "conteudo"
e = html.escape
MESES = "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split()

def data_extenso(iso):
    a, m, d = iso.split("-")
    return f"{int(d)} de {MESES[int(m) - 1]} de {a}"

def url_artigo(a):
    return f"pages/artigos/{a['slug']}.html"

def situacao(a):
    if a["revisado"]:
        return '<span class="situacao situacao--revisado">Revisado por profissional</span>'
    return '<span class="situacao">Aguardando revisão profissional</span>'

POR_CATEGORIA = {k: [a for a in ARTIGOS if a["categoria"] == k] for k in CATEGORIAS}

MARCA_SVG = ('<svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#263D32"/>'
             '<path fill="#DCE6D9" d="M46 16C28 16 17 26 17 40c0 3 .6 5.6 1.6 8C22 36 30 28 40 24c-9 6-15 14-18 25 2 .6 4 1 6 1 13 0 20-12 18-34z"/></svg>')

NAV = [("inicio", "Início", "index.html"), ("conhecimento", "Conhecimento", "pages/conhecimento.html"),
       ("momentos", "Momentos", "pages/momentos.html"), ("ajuda", "Encontrar ajuda", "pages/encontrar-ajuda.html"),
       ("sobre", "Sobre", "pages/sobre.html")]

GERADAS = []  # (caminho, indexável) — usado no sitemap

def pagina(caminho, titulo, descricao, corpo, atual=None, scripts=(), faixa=True, indexar=True, json_ld=None, base=None):
    """Escreve uma página completa. No corpo, {{u:caminho/desde/a/raiz}} vira um link relativo correto."""
    r = "" if base else "../" * caminho.count("/")
    u = lambda destino: r + destino
    corpo = re.sub(r"\{\{u:([^}]*)\}\}", lambda m: u(m.group(1)), corpo)
    itens = "\n".join(
        f'            <li><a href="{u(h)}"{" aria-current=\"page\"" if k == atual else ""}>{n}</a></li>' for k, n, h in NAV)
    tags = "\n".join(f'  <script src="{r}js/{s}" defer></script>' for s in ("main.js", "navigation.js") + tuple(scripts))
    titulo_completo = titulo if "Entre Nós" in titulo else f"{titulo} — Entre Nós"
    canonica = SITE_URL + ("" if caminho == "index.html" else caminho)
    extras = ""
    if base:
        extras += f'  <base href="{base}">\n'
    if indexar:
        extras += f'  <link rel="canonical" href="{canonica}">\n  <meta property="og:url" content="{canonica}">\n'
    else:
        extras += '  <meta name="robots" content="noindex">\n'
    if json_ld:
        extras += '  <script type="application/ld+json">' + json.dumps(json_ld, ensure_ascii=False) + '</script>\n'
    faixa_html = f'''
  <aside class="apoio-faixa" aria-label="Apoio imediato">
    <div class="container">
      Precisa conversar agora? O <strong>CVV</strong> atende pelo <a href="tel:188">188</a>, gratuitamente, 24 horas. Em emergência médica, ligue <a href="tel:192">192</a> (SAMU). <a href="{u("pages/encontrar-ajuda.html")}">Ver todos os caminhos de ajuda</a>
    </div>
  </aside>
''' if faixa else ""
    doc = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(titulo_completo)}</title>
  <meta name="description" content="{e(descricao)}">
  <meta name="theme-color" content="#263D32">
{extras}  <meta property="og:type" content="{"article" if json_ld else "website"}">
  <meta property="og:site_name" content="Entre Nós">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:title" content="{e(titulo_completo)}">
  <meta property="og:description" content="{e(descricao)}">
  <meta property="og:image" content="{SITE_URL}assets/images/compartilhar.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{r}assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="{r}assets/fonts/newsreader-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{r}css/reset.css">
  <link rel="stylesheet" href="{r}css/variables.css">
  <link rel="stylesheet" href="{r}css/global.css">
  <link rel="stylesheet" href="{r}css/components.css">
  <link rel="stylesheet" href="{r}css/responsive.css">
{tags}
</head>
<body>
  <a class="pular" href="{"" if not base else caminho}#conteudo">Pular para o conteúdo</a>

  <header class="topo">
    <div class="container topo__linha">
      <a class="marca" href="{u("index.html")}" aria-label="Entre Nós — página inicial">{MARCA_SVG}<span>Entre Nós</span></a>
      <button class="menu-botao" type="button" aria-expanded="false" aria-controls="nav-principal"><span class="menu-botao__icone" aria-hidden="true"></span>Menu</button>
      <nav class="nav" id="nav-principal" aria-label="Navegação principal">
        <ul class="nav__lista">
{itens}
        </ul>
      </nav>
      <a class="botao botao--ajuda" href="{u("pages/encontrar-ajuda.html")}"><span class="rotulo-longo">Preciso de ajuda</span><span class="rotulo-curto">Ajuda</span></a>
    </div>
  </header>

  <main id="conteudo">
{corpo.strip(chr(10))}
  </main>
{faixa_html}
  <footer class="rodape">
    <div class="container">
      <div class="rodape__grade">
        <div>
          <p class="rodape__marca">Entre Nós</p>
          <p class="rodape__assinatura">Um espaço para cuidar do que sentimos.</p>
          <p class="rodape__nota">Plataforma independente de saúde emocional. O conteúdo é informativo e não substitui avaliação, diagnóstico ou acompanhamento profissional.</p>
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
            <li><a href="{u("pages/responsabilidade.html")}">Responsabilidade editorial</a></li>
            <li><a href="{u("pages/privacidade.html")}">Privacidade</a></li>
          </ul>
        </nav>
        <div>
          <h2>Apoio imediato</h2>
          <ul class="rodape__lista">
            <li><a href="tel:188">CVV — 188</a></li>
            <li><a href="tel:192">SAMU — 192</a></li>
          </ul>
        </div>
      </div>
      <p class="rodape__fim"><span>© <span data-ano>2026</span> Entre Nós</span><span>Sem cookies, sem cadastro, sem rastreamento.</span></p>
    </div>
  </footer>
</body>
</html>
'''
    destino = RAIZ / caminho
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(doc, encoding="utf-8")
    GERADAS.append((caminho, indexar))

def cabecalho(sobre, titulo, lead, extra=""):
    return f'''    <div class="cabecalho-pagina">
      <div class="container">
        <span class="sobretitulo">{sobre}</span>
        <h1>{titulo}</h1>
        <p class="lead">{lead}</p>{extra}
      </div>
    </div>'''

def leitura(a, nivel="h3", biblioteca=False):
    """Linha editorial de artigo (listas do início, da biblioteca e de relacionados)."""
    miolo = f'''<{nivel}><a href="{{{{u:{url_artigo(a)}}}}}">{e(a["titulo"])}</a></{nivel}>
            <p>{e(a["intro"])}</p>
            <p class="meta"><span>{a["leitura"]} min de leitura</span>{situacao(a)}</p>'''
    cat = f'<span class="etiqueta">{e(CATEGORIAS[a["categoria"]])}</span>'
    if biblioteca:
        return f'''          <article class="leitura" data-categoria="{a["categoria"]}">
            {cat}
            <div>
            {miolo}
            </div>
          </article>'''
    return f'''          <article class="leitura">
            {cat}
            {miolo}
          </article>'''

def prosa(nome):
    texto = (CONTEUDO / f"{nome}.html").read_text(encoding="utf-8").rstrip()
    return "\n".join("          " + l if l else l for l in texto.split("\n"))

def por_slug(slug):
    return next(a for a in ARTIGOS if a["slug"] == slug)

# =====================================================================
# Início
# =====================================================================
principal = por_slug("o-que-e-ansiedade")
secundarias = "\n".join(leitura(por_slug(s)) for s in ("tristeza-ou-depressao", "como-procurar-ajuda-psicologica", "como-apoiar-alguem"))

def contagem(k):
    n = len(POR_CATEGORIA[k])
    return "em preparação" if n == 0 else ("1 leitura" if n == 1 else f"{n} leituras")

temas = "\n".join(f'          <li><a href="{{{{u:pages/conhecimento.html}}}}?categoria={k}"><span>{e(v)}</span><small>{contagem(k)}</small></a></li>'
                  for k, v in CATEGORIAS.items())
credito = f'\n            <figcaption>{e(HERO["credito"])}</figcaption>' if HERO["credito"] else ""

def fase(estacao, nome, texto, desenho):
    return f'''          <div class="fase">
            <svg viewBox="0 0 40 40" fill="none" stroke="#D5DFD3" stroke-width="1.5" aria-hidden="true"><circle cx="20" cy="20" r="18"/>{desenho}</svg>
            <p class="fase__estacao">{estacao}</p>
            <h3>{nome}</h3>
            <p>{texto}</p>
          </div>'''

fases = "\n".join([
    fase("Primavera", "Brotar", "Recomeços raramente são grandiosos. Às vezes, é só voltar a ter vontade de alguma coisa pequena.",
         '<path d="M20 2a18 18 0 0 1 18 18H20z" fill="#D5DFD3" stroke="none"/>'),
    fase("Verão", "Florescer", "Há fases de energia e de presença. Elas não são a medida de todas as outras, nem uma obrigação permanente.",
         '<circle cx="20" cy="20" r="18" fill="#D5DFD3" stroke="none"/>'),
    fase("Outono", "Soltar", "Perdas, despedidas e mudanças pedem tempo. Deixar ir também faz parte de continuar.",
         '<path d="M20 2a18 18 0 0 0 0 36z" fill="#D5DFD3" stroke="none"/>'),
    fase("Inverno", "Repousar", "Recolher-se não é desistir. Muita coisa se refaz em silêncio, antes de aparecer.", ""),
])

pagina("index.html", "Entre Nós — Um espaço para cuidar do que sentimos",
 "Plataforma independente de saúde emocional: leituras com fontes indicadas, pausas guiadas e caminhos de apoio. Gratuita, sem cadastro e sem rastreamento.",
 f'''    <section class="hero">
      <div class="container hero__grade">
        <div>
          <span class="sobretitulo">Saúde emocional</span>
          <h1>Um espaço para cuidar do que <em>sentimos</em>.</h1>
          <p class="lead">Leituras cuidadosas, pausas para respirar e caminhos de apoio. Sem pressa, no seu tempo.</p>
          <div class="acoes">
            <a class="botao" href="{{{{u:pages/conhecimento.html}}}}">Explorar as leituras</a>
            <a class="botao botao--contorno" href="{{{{u:pages/momentos.html}}}}">Fazer uma pausa</a>
          </div>
          <ul class="hero__garantias">
            <li>Gratuito</li>
            <li>Sem cadastro</li>
            <li>Sem rastreamento</li>
          </ul>
        </div>
        <figure class="moldura">
          <img src="{{{{u:assets/images/{HERO["arquivo"]}}}}}" alt="{e(HERO["alt"])}" width="900" height="1035" fetchpriority="high">{credito}
        </figure>
      </div>
    </section>

    <section class="secao" aria-labelledby="t-caminhos">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="sobretitulo">Por onde começar</span>
          <h2 id="t-caminhos">O que você procura hoje?</h2>
        </div>
        <ol class="caminhos">
          <li class="caminho">
            <span class="caminho__num" aria-hidden="true">01</span>
            <h3><a href="{{{{u:pages/conhecimento.html}}}}">Quero entender</a></h3>
            <p>Textos sobre ansiedade, tristeza, solidão e esgotamento, com as fontes indicadas.</p>
            <span class="caminho__seta" aria-hidden="true">→</span>
          </li>
          <li class="caminho">
            <span class="caminho__num" aria-hidden="true">02</span>
            <h3><a href="{{{{u:pages/momentos.html}}}}">Quero uma pausa</a></h3>
            <p>Quatro exercícios breves de respiração, atenção e reflexão. De um a três minutos.</p>
            <span class="caminho__seta" aria-hidden="true">→</span>
          </li>
          <li class="caminho">
            <span class="caminho__num" aria-hidden="true">03</span>
            <h3><a href="{{{{u:pages/encontrar-ajuda.html}}}}">Preciso de ajuda</a></h3>
            <p>Serviços públicos e gratuitos, e como chegar a um atendimento profissional.</p>
            <span class="caminho__seta" aria-hidden="true">→</span>
          </li>
        </ol>
      </div>
    </section>

    <section class="secao secao--borda" aria-labelledby="t-leituras">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="sobretitulo">Conhecimento</span>
          <h2 id="t-leituras">Leituras para começar</h2>
        </div>
        <div class="destaque">
          <article class="destaque__principal">
            <span class="etiqueta">{e(CATEGORIAS[principal["categoria"]])}</span>
            <h3><a href="{{{{u:{url_artigo(principal)}}}}}">{e(principal["titulo"])}</a></h3>
            <p>{e(principal["intro"])}</p>
            <p class="meta">{principal["leitura"]} min de leitura · {"Revisado por profissional" if principal["revisado"] else "Aguardando revisão profissional"}</p>
          </article>
          <div>
            <div class="leituras">
{secundarias}
            </div>
            <p style="margin-top:var(--e-4)"><a class="link-seta" href="{{{{u:pages/conhecimento.html}}}}">Ver todas as leituras</a></p>
          </div>
        </div>
      </div>
    </section>

    <section class="secao ciclos" aria-labelledby="t-ciclos">
      <div class="container">
        <div class="ciclos__intro">
          <div>
            <span class="sobretitulo">Nosso jeito de ver</span>
            <h2 id="t-ciclos">A vida acontece em ciclos</h2>
          </div>
          <p>Uma floresta não floresce o ano inteiro. Há meses de broto, de copa cheia, de folhas no chão e de galhos nus, e nenhum deles é um erro. Com o que sentimos, costuma ser parecido.</p>
        </div>
        <div class="fases">
{fases}
        </div>
        <p class="ciclos__fecho">Nenhuma estação dura para sempre, e ninguém precisa atravessá-las no mesmo ritmo. Mas ciclos não explicam tudo: quando o inverno parece não passar, <a href="{{{{u:pages/encontrar-ajuda.html}}}}">vale procurar ajuda</a>.</p>
      </div>
    </section>

    <section class="secao" aria-labelledby="t-temas">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="sobretitulo">Temas</span>
          <h2 id="t-temas">Explorar por assunto</h2>
          <p>A biblioteca cresce devagar: cada texto só entra depois de ter as fontes conferidas.</p>
        </div>
        <ul class="temas">
{temas}
        </ul>
      </div>
    </section>

    <section class="secao secao--areia" aria-labelledby="t-apoio">
      <div class="container apoio">
        <div>
          <span class="sobretitulo">Apoio</span>
          <h2 id="t-apoio">Se hoje estiver difícil demais</h2>
          <p>Você não precisa esperar a situação piorar para pedir ajuda. Estes serviços são gratuitos e funcionam a qualquer hora.</p>
          <div class="acoes"><a class="botao botao--contorno" href="{{{{u:pages/encontrar-ajuda.html}}}}">Ver todos os caminhos de ajuda</a></div>
        </div>
        <div class="telefones">
          <a class="telefone" href="tel:188"><strong>188</strong><span><b>CVV — Centro de Valorização da Vida</b>Apoio emocional, 24 horas</span></a>
          <a class="telefone" href="tel:192"><strong>192</strong><span><b>SAMU</b>Emergências médicas, 24 horas</span></a>
        </div>
      </div>
    </section>''', atual="inicio", faixa=False,
 json_ld={"@context": "https://schema.org", "@type": "WebSite", "name": "Entre Nós", "url": SITE_URL, "inLanguage": "pt-BR",
          "description": "Plataforma independente de saúde emocional."})
# o início é um site, não um artigo
p = RAIZ / "index.html"; p.write_text(p.read_text().replace('og:type" content="article"', 'og:type" content="website"'))

# =====================================================================
# Conhecimento (biblioteca)
# =====================================================================
filtros = f'            <button class="filtro" type="button" data-filtro="todas" aria-pressed="true">Todas <small>{len(ARTIGOS)}</small></button>\n' + "\n".join(
    f'            <button class="filtro" type="button" data-filtro="{k}" aria-pressed="false">{e(v)} <small>{len(POR_CATEGORIA[k])}</small></button>' for k, v in CATEGORIAS.items())
todos = "\n".join(leitura(a, "h2", biblioteca=True) for a in ARTIGOS)
pagina("pages/conhecimento.html", "Conhecimento", "Biblioteca de leituras sobre saúde emocional: ansiedade, depressão, solidão, esgotamento, relacionamentos e mais, com fontes indicadas.",
 cabecalho("Biblioteca", "Conhecimento", "Textos para compreender melhor o que sentimos. Cada leitura indica autoria, fontes e situação de revisão.") + f'''
    <section class="secao">
      <div class="container">
        <div class="busca" role="search">
          <div>
            <label for="busca-artigos">Buscar por palavra ou assunto</label>
            <input type="search" id="busca-artigos" placeholder="Ex.: ansiedade, cansaço, apoio" autocomplete="off">
          </div>
          <div class="filtros" role="group" aria-label="Filtrar por tema">
{filtros}
          </div>
        </div>
        <p class="resultado-info" id="resultado-info" role="status" aria-live="polite"></p>
        <div class="leituras leituras--biblioteca" id="lista-artigos">
{todos}
        </div>
        <div class="vazio" id="sem-resultados" hidden>
          <h2>Ainda não há leituras aqui</h2>
          <p>Não encontramos textos para essa busca ou tema. A biblioteca está em construção, e preferimos publicar pouco a publicar sem verificar.</p>
          <div class="acoes"><button class="botao botao--contorno botao--pequeno" type="button" id="limpar-busca">Ver todas as leituras</button></div>
        </div>
      </div>
    </section>''', atual="conhecimento", scripts=("search.js",))

# =====================================================================
# Artigos (uma página estática por artigo)
# =====================================================================
def corpo_artigo(a):
    partes = []
    for s in a["secoes"]:
        if s["titulo"]:
            partes.append(f'          <h2>{e(s["titulo"])}</h2>')
        for b in s["blocos"]:
            if isinstance(b, list):
                partes.append("          <ul>\n" + "\n".join(f"            <li>{e(i)}</li>" for i in b) + "\n          </ul>")
            else:
                partes.append(f"          <p>{e(b)}</p>")
    return "\n".join(partes)

for a in ARTIGOS:
    outros = sorted((o for o in ARTIGOS if o is not a), key=lambda o: o["categoria"] != a["categoria"])[:3]
    relacionados = "\n".join(leitura(o) for o in outros)
    fontes = "\n".join(f'            <li><a href="{e(f["url"])}" rel="noopener noreferrer">{e(f["nome"])}</a></li>' for f in a["fontes"])
    if a["revisado"]:
        revisao = f'{data_extenso(a["revisado"])}, por {e(a["revisor"])}'
        aviso = ""
    else:
        revisao = "Aguardando revisão profissional"
        aviso = '''
        <p class="aviso"><strong>Conteúdo em revisão.</strong> Este texto ainda não foi revisado por um profissional de saúde mental. Ele foi redigido a partir das fontes listadas ao final e deve ser lido como informação geral, não como orientação clínica.</p>'''
    pagina(url_artigo(a), a["titulo"], a["intro"], f'''    <div class="container artigo">
      <nav class="trilha" aria-label="Você está em">
        <ol>
          <li><a href="{{{{u:index.html}}}}">Início</a></li>
          <li><a href="{{{{u:pages/conhecimento.html}}}}">Conhecimento</a></li>
          <li><a href="{{{{u:pages/conhecimento.html}}}}?categoria={a["categoria"]}">{e(CATEGORIAS[a["categoria"]])}</a></li>
        </ol>
      </nav>
      <article>
        <header class="artigo__topo">
          <span class="etiqueta">{e(CATEGORIAS[a["categoria"]])}</span>
          <h1>{e(a["titulo"])}</h1>
          <p class="lead">{e(a["intro"])}</p>
        </header>
        <dl class="ficha">
          <div><dt>Autoria</dt><dd>{e(a["autoria"])}</dd></div>
          <div><dt>Publicação</dt><dd><time datetime="{a["publicado"]}">{data_extenso(a["publicado"])}</time></dd></div>
          <div><dt>Revisão</dt><dd>{revisao}</dd></div>
          <div><dt>Leitura</dt><dd>{a["leitura"]} minutos</dd></div>
        </dl>{aviso}
        <div class="prosa prosa--artigo">
{corpo_artigo(a)}
          <p class="aviso aviso--verde">Este conteúdo é informativo e não substitui avaliação, diagnóstico ou acompanhamento profissional. <a href="{{{{u:pages/responsabilidade.html}}}}">Como produzimos nossos conteúdos</a>.</p>
        </div>
        <section class="fontes" aria-labelledby="t-fontes">
          <h2 id="t-fontes">Fontes consultadas</h2>
          <ol>
{fontes}
          </ol>
          <p>Os links levam a sites externos, de responsabilidade das instituições citadas.</p>
        </section>
        <aside class="artigo__ajuda" aria-labelledby="t-ajuda">
          <h2 id="t-ajuda">Precisa de apoio agora?</h2>
          <p>O CVV atende pelo <a href="tel:188">188</a>, gratuitamente, 24 horas. Em emergência médica, ligue <a href="tel:192">192</a>. Veja também <a href="{{{{u:pages/encontrar-ajuda.html}}}}">outros caminhos de ajuda</a>.</p>
        </aside>
      </article>
    </div>
    <section class="secao secao--borda relacionados" aria-labelledby="t-rel">
      <div class="container">
        <div class="secao__cabecalho" style="margin-bottom:var(--e-4)"><h2 id="t-rel">Continuar lendo</h2></div>
        <div class="leituras" style="max-width:48rem">
{relacionados}
        </div>
      </div>
    </section>''', atual="conhecimento", faixa=False,
     json_ld={"@context": "https://schema.org", "@type": "Article", "headline": a["titulo"], "description": a["intro"],
              "inLanguage": "pt-BR", "datePublished": a["publicado"], **({"dateModified": a["revisado"]} if a["revisado"] else {}),
              "author": {"@type": "Organization", "name": a["autoria"]},
              "publisher": {"@type": "Organization", "name": "Entre Nós"},
              "mainEntityOfPage": SITE_URL + url_artigo(a)})

# Endereço antigo (artigo.html?id=<slug>): redireciona para a página do artigo e, sem id, lista as leituras.
indice = "\n".join(f'          <li class="leitura"><span class="etiqueta">{e(CATEGORIAS[a["categoria"]])}</span><h2><a data-slug="{a["slug"]}" href="artigos/{a["slug"]}.html">{e(a["titulo"])}</a></h2></li>' for a in ARTIGOS)
pagina("pages/artigo.html", "Leituras", "Índice das leituras do Entre Nós.",
 cabecalho("Biblioteca", "Leituras", "Cada leitura tem o seu próprio endereço. Escolha uma para começar.") + f'''
    <section class="secao">
      <div class="container">
        <p class="aviso" id="aviso-endereco" role="status" hidden style="max-width:48rem;margin-bottom:var(--e-4)"></p>
        <ul class="leituras" style="max-width:48rem">
{indice}
        </ul>
        <p style="margin-top:var(--e-4)"><a class="link-seta" href="conhecimento.html">Buscar e filtrar na biblioteca</a></p>
      </div>
    </section>''', atual="conhecimento", scripts=("article.js",), indexar=False)

# =====================================================================
# Momentos
# =====================================================================
sumario = '''
        <nav class="sumario" aria-label="Exercícios desta página">
          <a href="#ex-respiracao">Respiração guiada <small>2 min</small></a>
          <a href="#ex-sentidos">Atenção aos sentidos <small>3 min</small></a>
          <a href="#ex-pausa">Pausa de um minuto <small>1 min</small></a>
          <a href="#ex-reflexao">Uma pergunta <small>livre</small></a>
        </nav>'''
pagina("pages/momentos.html", "Um momento para mim", "Exercícios simples de respiração, atenção aos sentidos, pausa e reflexão. Nada é registrado.",
 cabecalho("Momentos", "Um momento para mim", "Pequenas pausas para fazer agora, no seu ritmo. Nada do que você fizer aqui é registrado ou enviado.", sumario) + '''
    <section class="secao">
      <div class="container">
        <p class="aviso" style="max-width:46rem;margin-bottom:var(--e-6)"><strong>Um cuidado:</strong> estes exercícios são convites de pausa, não tratamentos. Se algum deles causar desconforto, pare. Em sofrimento intenso, veja <a href="{{u:pages/encontrar-ajuda.html}}">Encontrar ajuda</a>.</p>

        <section class="exercicio" id="ex-respiracao" aria-labelledby="t-resp">
          <div class="exercicio__texto">
            <span class="etiqueta">2 minutos</span>
            <h2 id="t-resp">Respiração guiada</h2>
            <p>Acompanhe o círculo: inspire enquanto ele cresce, por 4 segundos, e solte o ar enquanto ele diminui, por 6. Se o ritmo não for confortável, respire do seu jeito.</p>
          </div>
          <div class="exercicio__palco">
            <div class="respiro" aria-hidden="true"></div>
            <p class="palco__fase" aria-live="polite">Quando quiser, comece.</p>
            <p class="palco__apoio"></p>
            <div class="acoes"><button class="botao" type="button" data-acao="alternar">Começar</button></div>
          </div>
        </section>

        <section class="exercicio" id="ex-sentidos" aria-labelledby="t-sent">
          <div class="exercicio__texto">
            <span class="etiqueta">3 minutos</span>
            <h2 id="t-sent">Atenção aos sentidos</h2>
            <p>Um jeito de trazer a atenção de volta para o presente, passando por cada um dos cinco sentidos. Avance quando estiver pronto.</p>
          </div>
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
          <div class="exercicio__texto">
            <span class="etiqueta">1 minuto</span>
            <h2 id="t-pausa">Pausa de um minuto</h2>
            <p>Sessenta segundos sem tarefa nenhuma. Não é preciso esvaziar a mente; basta não fazer nada por um instante.</p>
          </div>
          <div class="exercicio__palco">
            <p class="palco__fase" aria-live="polite">Um minuto, sem tarefa nenhuma.</p>
            <p class="palco__apoio"></p>
            <div class="barra" role="progressbar" aria-label="Progresso da pausa" aria-valuemin="0" aria-valuemax="60" aria-valuenow="0"><div class="barra__fio"></div></div>
            <div class="acoes"><button class="botao" type="button" data-acao="alternar">Começar</button></div>
          </div>
        </section>

        <section class="exercicio" id="ex-reflexao" aria-labelledby="t-refl">
          <div class="exercicio__texto">
            <span class="etiqueta">Sem tempo marcado</span>
            <h2 id="t-refl">Uma pergunta para refletir</h2>
            <p>Fique com a pergunta pelo tempo que quiser. Responda em pensamento ou no papel: este site não guarda o que você escreve.</p>
          </div>
          <div class="exercicio__palco">
            <p class="pergunta" aria-live="polite">Do que eu estou precisando neste momento?</p>
            <div class="acoes"><button class="botao botao--contorno" type="button" data-acao="outra">Outra pergunta</button></div>
          </div>
        </section>
      </div>
    </section>''', atual="momentos", scripts=("exercises.js",))

# =====================================================================
# Encontrar ajuda
# =====================================================================
pagina("pages/encontrar-ajuda.html", "Encontrar ajuda", "Caminhos de apoio em saúde mental no Brasil: CVV 188, SAMU 192, CAPS, UBS e como procurar atendimento psicológico.",
 cabecalho("Apoio", "Encontrar ajuda", "Pedir ajuda é um gesto de cuidado. Aqui estão caminhos públicos e gratuitos de atendimento no Brasil.") + f'''
    <section class="secao" style="padding-bottom:0">
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

    <section class="secao" aria-labelledby="t-servicos">
      <div class="container">
        <div class="secao__cabecalho">
          <span class="sobretitulo">Serviços</span>
          <h2 id="t-servicos">Onde procurar atendimento</h2>
        </div>
        <div class="servicos">
          <article class="servico">
            <p class="servico__numero">188</p>
            <div><span class="etiqueta">Apoio emocional · 24 horas</span><h3>CVV — Centro de Valorização da Vida</h3></div>
            <div class="servico__corpo">
              <p>Apoio emocional e prevenção do suicídio, por voluntários, com sigilo. A ligação é gratuita em todo o país. Também há atendimento por chat e e-mail no site.</p>
              <a class="link-seta" href="https://cvv.org.br/" rel="noopener noreferrer">Acessar cvv.org.br</a>
            </div>
          </article>
          <article class="servico">
            <p class="servico__numero">192</p>
            <div><span class="etiqueta">Emergência médica · 24 horas</span><h3>SAMU</h3></div>
            <div class="servico__corpo">
              <p>Serviço de Atendimento Móvel de Urgência. Para situações com risco à vida, incluindo crises em saúde mental com risco imediato. A ligação é gratuita.</p>
              <a class="link-seta" href="tel:192">Ligar 192</a>
            </div>
          </article>
          <article class="servico">
            <p class="servico__numero servico__numero--sigla">CAPS</p>
            <div><span class="etiqueta">SUS · sofrimento intenso</span><h3>Centro de Atenção Psicossocial</h3></div>
            <div class="servico__corpo">
              <p>Serviço público para pessoas em sofrimento psíquico intenso ou persistente, com equipe multiprofissional. Em geral, recebe diretamente, sem necessidade de encaminhamento.</p>
              <p>Para localizar o CAPS da sua região, consulte a secretaria de saúde do município ou a UBS mais próxima.</p>
            </div>
          </article>
          <article class="servico">
            <p class="servico__numero servico__numero--sigla">UBS</p>
            <div><span class="etiqueta">SUS · porta de entrada</span><h3>Unidade Básica de Saúde</h3></div>
            <div class="servico__corpo">
              <p>O posto de saúde do seu bairro é o primeiro lugar para falar sobre como você tem se sentido. A equipe acolhe, acompanha e encaminha para outros serviços quando necessário.</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="secao secao--areia">
      <div class="container">
        <div class="prosa">
{prosa("encontrar-ajuda")}
        </div>
      </div>
    </section>''', atual="ajuda", faixa=False)

# =====================================================================
# Páginas institucionais (texto em tools/conteudo/*.html)
# =====================================================================
def institucional(arquivo, titulo, descricao, sobre, h1, lead, atual=None):
    pagina(f"pages/{arquivo}.html", titulo, descricao, cabecalho(sobre, h1, lead) + f'''
    <section class="secao">
      <div class="container">
        <div class="prosa">
{prosa(arquivo)}
        </div>
      </div>
    </section>''', atual=atual)

institucional("sobre", "Sobre", "Conheça o propósito, a missão e os valores do Entre Nós, uma plataforma independente de saúde emocional.",
              "O projeto", "Sobre o Entre Nós", "Uma plataforma independente de saúde emocional, feita para informar, acolher e orientar.", atual="sobre")
institucional("privacidade", "Política de privacidade", "O Entre Nós não usa cookies, não exige cadastro e não coleta dados pessoais. Veja como tratamos a sua privacidade.",
              "Transparência", "Política de privacidade", "Em resumo: não pedimos, não coletamos e não guardamos dados pessoais seus.")
institucional("responsabilidade", "Limites e responsabilidade editorial", "Como os conteúdos do Entre Nós são produzidos e revisados, e quais são os limites deste espaço.",
              "Transparência", "Limites e responsabilidade editorial", "O que você pode esperar deste espaço, e o que ele não pode oferecer.")

# =====================================================================
# 404 (o GitHub Pages serve este arquivo em qualquer endereço inexistente; por isso usa <base>)
# =====================================================================
pagina("404.html", "Página não encontrada", "O endereço procurado não existe no Entre Nós.",
 cabecalho("Erro 404", "Este caminho não leva a lugar nenhum", "O endereço pode ter mudado ou ter sido digitado de outro jeito. Estes caminhos continuam abertos:") + '''
    <section class="secao">
      <div class="container">
        <div class="acoes" style="margin-top:0">
          <a class="botao" href="index.html">Página inicial</a>
          <a class="botao botao--contorno" href="pages/conhecimento.html">Leituras</a>
          <a class="botao botao--contorno" href="pages/momentos.html">Momentos</a>
          <a class="botao botao--contorno" href="pages/encontrar-ajuda.html">Encontrar ajuda</a>
        </div>
      </div>
    </section>''', indexar=False, base=BASE_PATH)

# =====================================================================
# Sitemap
# =====================================================================
urls = "\n".join(f"  <url><loc>{SITE_URL}{'' if c == 'index.html' else c}</loc></url>" for c, ok in GERADAS if ok)
(RAIZ / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
print(f"{len(GERADAS)} páginas geradas")
