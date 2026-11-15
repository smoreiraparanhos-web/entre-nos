/* search.js — busca e filtros da biblioteca (pages/conhecimento.html)
   Os cartões já existem no HTML; este script apenas mostra ou oculta. */
(function () {
  'use strict';

  function normalizar(texto) {
    return texto.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }

  document.addEventListener('DOMContentLoaded', function () {
    var campo = document.getElementById('busca-artigos');
    var lista = document.getElementById('lista-artigos');
    if (!campo || !lista) return;

    var cartoes = Array.prototype.slice.call(lista.querySelectorAll('[data-categoria]'));
    var filtros = Array.prototype.slice.call(document.querySelectorAll('.filtro'));
    var info = document.getElementById('resultado-info');
    var vazio = document.getElementById('sem-resultados');
    var categoria = 'todas';

    var indice = cartoes.map(function (cartao) { return normalizar(cartao.textContent); });

    function aplicar() {
      var termos = normalizar(campo.value).split(/\s+/).filter(Boolean);
      var visiveis = 0;
      cartoes.forEach(function (cartao, i) {
        var naCategoria = categoria === 'todas' || cartao.dataset.categoria === categoria;
        var noTexto = termos.every(function (t) { return indice[i].indexOf(t) !== -1; });
        cartao.hidden = !(naCategoria && noTexto);
        if (!cartao.hidden) visiveis++;
      });
      vazio.hidden = visiveis !== 0;
      info.textContent = visiveis === 1 ? '1 leitura encontrada.' : visiveis + ' leituras encontradas.';
    }

    function escolher(nova) {
      categoria = nova;
      filtros.forEach(function (f) {
        f.setAttribute('aria-pressed', String(f.dataset.filtro === nova));
      });
      aplicar();
    }

    filtros.forEach(function (f) {
      f.addEventListener('click', function () { escolher(f.dataset.filtro); });
    });
    campo.addEventListener('input', aplicar);

    var limpar = document.getElementById('limpar-busca');
    if (limpar) limpar.addEventListener('click', function () { campo.value = ''; escolher('todas'); campo.focus(); });

    // Permite chegar já filtrado: conhecimento.html?categoria=ansiedade
    var inicial = new URLSearchParams(window.location.search).get('categoria');
    if (inicial && filtros.some(function (f) { return f.dataset.filtro === inicial; })) escolher(inicial);
    else aplicar();
  });
})();
