/* exercises.js — exercícios de pages/momentos.html
   Nada do que acontece aqui é armazenado ou enviado. */
(function () {
  'use strict';

  /* 1. Respiração guiada: inspirar 4 s, soltar 6 s, por 12 ciclos (2 minutos). */
  function respiracao() {
    var raiz = document.getElementById('ex-respiracao');
    if (!raiz) return;
    var circulo = raiz.querySelector('.respiro');
    var fase = raiz.querySelector('.palco__fase');
    var apoio = raiz.querySelector('.palco__apoio');
    var botao = raiz.querySelector('[data-acao="alternar"]');
    var CICLOS = 12, INSPIRA = 4000, SOLTA = 6000;
    var temporizador = null, ciclo = 0;

    function parar(mensagem) {
      clearTimeout(temporizador);
      temporizador = null;
      circulo.style.transitionDuration = '1s';
      circulo.classList.remove('is-cheio');
      fase.textContent = mensagem || 'Quando quiser, comece.';
      apoio.textContent = '';
      botao.textContent = 'Começar';
    }

    function inspirar() {
      ciclo++;
      if (ciclo > CICLOS) { parar('Pronto. Volte no seu tempo.'); return; }
      circulo.style.transitionDuration = INSPIRA + 'ms';
      circulo.classList.add('is-cheio');
      fase.textContent = 'Inspire pelo nariz';
      apoio.textContent = 'Ciclo ' + ciclo + ' de ' + CICLOS;
      temporizador = setTimeout(soltar, INSPIRA);
    }

    function soltar() {
      circulo.style.transitionDuration = SOLTA + 'ms';
      circulo.classList.remove('is-cheio');
      fase.textContent = 'Solte o ar devagar';
      temporizador = setTimeout(inspirar, SOLTA);
    }

    botao.addEventListener('click', function () {
      if (temporizador) { parar(); return; }
      ciclo = 0;
      botao.textContent = 'Parar';
      inspirar();
    });
  }

  /* 2. Atenção aos sentidos (5-4-3-2-1). */
  function sentidos() {
    var raiz = document.getElementById('ex-sentidos');
    if (!raiz) return;
    var passos = [
      { n: '5', t: 'coisas que você consegue ver', d: 'Olhe ao redor sem pressa. Repare em cores, formas, na luz.' },
      { n: '4', t: 'coisas que você consegue tocar', d: 'A textura da roupa, o apoio da cadeira, a temperatura do ar.' },
      { n: '3', t: 'sons que você consegue ouvir', d: 'Os mais próximos e os mais distantes. Não precisa nomear todos.' },
      { n: '2', t: 'cheiros que você consegue perceber', d: 'Se não perceber nenhum, lembre de dois cheiros de que gosta.' },
      { n: '1', t: 'sabor que você consegue sentir', d: 'Ou apenas note como está a sua boca agora.' }
    ];
    var numero = raiz.querySelector('.passo__numero');
    var fase = raiz.querySelector('.palco__fase');
    var apoio = raiz.querySelector('.palco__apoio');
    var anterior = raiz.querySelector('[data-acao="anterior"]');
    var proximo = raiz.querySelector('[data-acao="proximo"]');
    var i = 0;

    function mostrar() {
      if (i >= passos.length) {
        numero.textContent = '·';
        fase.textContent = 'Você chegou ao fim.';
        apoio.textContent = 'Perceba como está agora, sem precisar avaliar.';
        proximo.textContent = 'Recomeçar';
      } else {
        numero.textContent = passos[i].n;
        fase.textContent = passos[i].t;
        apoio.textContent = passos[i].d;
        proximo.textContent = 'Próximo';
      }
      anterior.disabled = i === 0;
    }

    proximo.addEventListener('click', function () { i = i >= passos.length ? 0 : i + 1; mostrar(); });
    anterior.addEventListener('click', function () { if (i > 0) i--; mostrar(); });
    mostrar();
  }

  /* 3. Pausa de um minuto. */
  function pausa() {
    var raiz = document.getElementById('ex-pausa');
    if (!raiz) return;
    var fase = raiz.querySelector('.palco__fase');
    var apoio = raiz.querySelector('.palco__apoio');
    var fio = raiz.querySelector('.barra__fio');
    var barra = raiz.querySelector('.barra');
    var botao = raiz.querySelector('[data-acao="alternar"]');
    var TOTAL = 60, restante = TOTAL, intervalo = null;
    var convites = ['Solte os ombros.', 'Descanse o olhar em um ponto.', 'Sinta os pés no chão.', 'Não há nada a resolver neste minuto.'];

    function desenhar() {
      fio.style.width = ((TOTAL - restante) / TOTAL * 100) + '%';
      barra.setAttribute('aria-valuenow', String(TOTAL - restante));
    }

    function parar(mensagem) {
      clearInterval(intervalo);
      intervalo = null;
      restante = TOTAL;
      fase.textContent = mensagem || 'Um minuto, sem tarefa nenhuma.';
      apoio.textContent = '';
      botao.textContent = 'Começar';
      if (!mensagem) desenhar();
    }

    botao.addEventListener('click', function () {
      if (intervalo) { parar(); return; }
      restante = TOTAL;
      desenhar();
      botao.textContent = 'Parar';
      fase.textContent = convites[0];
      apoio.textContent = restante + ' segundos';
      intervalo = setInterval(function () {
        restante--;
        desenhar();
        if (restante <= 0) { parar('O minuto passou. Siga quando quiser.'); return; }
        apoio.textContent = restante + ' segundos';
        if (restante % 15 === 0) fase.textContent = convites[(TOTAL - restante) / 15];
      }, 1000);
    });
  }

  /* 4. Perguntas para reflexão. */
  function reflexao() {
    var raiz = document.getElementById('ex-reflexao');
    if (!raiz) return;
    var perguntas = [
      'O que ocupou mais espaço em mim hoje?',
      'Do que eu estou precisando neste momento?',
      'O que eu diria a um amigo que estivesse se sentindo como eu?',
      'Qual foi um momento pequeno e bom desta semana?',
      'O que está sob o meu controle hoje, e o que não está?',
      'Com quem eu gostaria de conversar com mais calma?',
      'O que o meu corpo está me dizendo agora?',
      'O que eu posso deixar para amanhã sem culpa?'
    ];
    var alvo = raiz.querySelector('.pergunta');
    var botao = raiz.querySelector('[data-acao="outra"]');
    var i = Math.floor(Math.random() * perguntas.length);
    alvo.textContent = perguntas[i];
    botao.addEventListener('click', function () {
      i = (i + 1) % perguntas.length;
      alvo.textContent = perguntas[i];
    });
  }

  /* 5. Uma palavra para hoje: frases de ânimo, sem promessas. */
  function palavra() {
    var raiz = document.getElementById('ex-palavra');
    if (!raiz) return;
    var frases = [
      'Hoje não precisa ser um dia bom. Basta ser um dia possível.',
      'Você já atravessou dias que pareciam não ter fim. Eles tiveram.',
      'Descansar não é perder tempo. É parte do caminho.',
      'O que você sente agora é real, e não é tudo o que você é.',
      'Um passo pequeno ainda é um passo.',
      'Pedir ajuda é um jeito de continuar, não de desistir.',
      'Você não precisa dar conta de tudo hoje. Só da próxima coisa.',
      'Dias difíceis não apagam o que você já construiu.',
      'Ir devagar também é ir.',
      'Você merece o mesmo cuidado que oferece aos outros.',
      'Nem todo dia rende. Alguns só precisam ser atravessados.',
      'Tem gente que fica melhor porque você existe, mesmo quando você não percebe.'
    ];
    var alvo = raiz.querySelector('.pergunta');
    var botao = raiz.querySelector('[data-acao="outra"]');
    var i = Math.floor(Math.random() * frases.length);
    alvo.textContent = frases[i];
    botao.addEventListener('click', function () {
      i = (i + 1) % frases.length;
      alvo.textContent = frases[i];
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    respiracao(); sentidos(); pausa(); reflexao(); palavra();
  });
})();
