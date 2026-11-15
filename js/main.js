/* main.js — inicialização comum a todas as páginas */
(function () {
  'use strict';
  // Sinaliza ao CSS que o JavaScript está ativo (melhoria progressiva).
  document.documentElement.classList.add('js');

  document.addEventListener('DOMContentLoaded', function () {
    var ano = document.querySelector('[data-ano]');
    if (ano) ano.textContent = String(new Date().getFullYear());
  });
})();
