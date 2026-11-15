/* article.js — compatibilidade com o endereço antigo dos artigos.
   Antes: pages/artigo.html?id=<slug>. Agora cada artigo é uma página própria em pages/artigos/<slug>.html.
   Este script apenas redireciona os links antigos; o conteúdo já está no HTML. */
(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {
    var id = new URLSearchParams(window.location.search).get('id');
    if (!id) return;
    var links = document.querySelectorAll('a[data-slug]');
    for (var i = 0; i < links.length; i++) {
      if (links[i].getAttribute('data-slug') === id) {
        window.location.replace(links[i].href);
        return;
      }
    }
    var aviso = document.getElementById('aviso-endereco');
    if (aviso) {
      aviso.textContent = 'Não encontramos a leitura deste endereço. Estas são as que estão disponíveis.';
      aviso.hidden = false;
    }
  });
})();
