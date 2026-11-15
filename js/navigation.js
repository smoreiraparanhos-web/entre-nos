/* navigation.js — menu principal em telas pequenas */
(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {
    var botao = document.querySelector('.menu-botao');
    var nav = document.getElementById('nav-principal');
    if (!botao || !nav) return;

    function definir(aberta) {
      nav.classList.toggle('is-aberta', aberta);
      botao.setAttribute('aria-expanded', String(aberta));
    }

    botao.addEventListener('click', function () {
      definir(botao.getAttribute('aria-expanded') !== 'true');
    });

    document.addEventListener('keydown', function (evento) {
      if (evento.key === 'Escape' && botao.getAttribute('aria-expanded') === 'true') {
        definir(false);
        botao.focus();
      }
    });
  });
})();
