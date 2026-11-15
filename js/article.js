/* article.js — monta a leitura em pages/artigo.html?id=<slug>
   Dados em js/data/articles.js. Todo texto é inserido com textContent. */
(function () {
  'use strict';

  function el(tag, texto, classe) {
    var no = document.createElement(tag);
    if (texto) no.textContent = texto;
    if (classe) no.className = classe;
    return no;
  }

  function data(iso) {
    if (!iso) return null;
    var p = iso.split('-');
    return new Date(Number(p[0]), Number(p[1]) - 1, Number(p[2]))
      .toLocaleDateString('pt-BR', { day: 'numeric', month: 'long', year: 'numeric' });
  }

  function meta(dl, termo, valor) {
    var div = document.createElement('div');
    div.appendChild(el('dt', termo + ': '));
    div.appendChild(el('dd', valor));
    dl.appendChild(div);
  }

  document.addEventListener('DOMContentLoaded', function () {
    var alvo = document.getElementById('artigo');
    var dados = window.ENTRE_NOS;
    if (!alvo || !dados) return;

    var id = new URLSearchParams(window.location.search).get('id');
    var artigo = dados.artigos.filter(function (a) { return a.slug === id; })[0];
    if (!artigo) { document.getElementById('artigo-ausente').hidden = false; return; }

    document.title = artigo.titulo + ' — Entre Nós';
    var descricao = document.querySelector('meta[name="description"]');
    if (descricao) descricao.setAttribute('content', artigo.intro);

    var topo = el('header', null, 'artigo__topo');
    topo.appendChild(el('span', dados.categorias[artigo.categoria], 'etiqueta'));
    topo.appendChild(el('h1', artigo.titulo));
    topo.appendChild(el('p', artigo.intro, 'lead'));
    var dl = el('dl', null, 'artigo__meta');
    meta(dl, 'Autoria', artigo.autoria);
    meta(dl, 'Publicação', data(artigo.publicado));
    meta(dl, 'Revisão', artigo.revisado ? data(artigo.revisado) + ', por ' + artigo.revisor : 'aguardando revisão profissional');
    meta(dl, 'Leitura', artigo.leitura + ' min');
    topo.appendChild(dl);
    alvo.appendChild(topo);

    if (!artigo.revisado) {
      var aviso = el('p', null, 'aviso');
      aviso.appendChild(el('strong', 'Conteúdo em revisão. '));
      aviso.appendChild(document.createTextNode('Este texto foi escrito a partir das fontes listadas ao final e ainda aguarda revisão de um profissional de saúde mental.'));
      aviso.style.maxWidth = 'var(--largura-leitura)';
      aviso.style.marginBottom = 'var(--e-5)';
      alvo.appendChild(aviso);
    }

    var corpo = el('div', null, 'prosa prosa--artigo');
    artigo.secoes.forEach(function (secao) {
      if (secao.titulo) corpo.appendChild(el('h2', secao.titulo));
      secao.blocos.forEach(function (bloco) {
        if (Array.isArray(bloco)) {
          var ul = document.createElement('ul');
          bloco.forEach(function (item) { ul.appendChild(el('li', item)); });
          corpo.appendChild(ul);
        } else {
          corpo.appendChild(el('p', bloco));
        }
      });
    });
    var lembrete = el('p', 'Este conteúdo é informativo e não substitui avaliação, diagnóstico ou acompanhamento profissional.', 'aviso aviso--verde');
    corpo.appendChild(lembrete);
    alvo.appendChild(corpo);

    var fontes = el('section', null, 'fontes');
    fontes.appendChild(el('h2', 'Fontes'));
    var ol = document.createElement('ol');
    artigo.fontes.forEach(function (f) {
      var li = document.createElement('li');
      var a = el('a', f.nome);
      a.href = f.url;
      a.rel = 'noopener noreferrer';
      li.appendChild(a);
      ol.appendChild(li);
    });
    fontes.appendChild(ol);
    alvo.appendChild(fontes);

    // Conteúdos relacionados: mesma categoria primeiro, depois os demais.
    var outros = dados.artigos.filter(function (a) { return a.slug !== artigo.slug; });
    outros.sort(function (a, b) {
      return (b.categoria === artigo.categoria) - (a.categoria === artigo.categoria);
    });
    var grade = document.getElementById('relacionados-lista');
    outros.slice(0, 3).forEach(function (a) {
      var cartao = el('article', null, 'cartao');
      cartao.appendChild(el('span', dados.categorias[a.categoria], 'etiqueta'));
      var h3 = document.createElement('h3');
      var link = el('a', a.titulo);
      link.href = 'artigo.html?id=' + encodeURIComponent(a.slug);
      h3.appendChild(link);
      cartao.appendChild(h3);
      cartao.appendChild(el('p', a.intro));
      cartao.appendChild(el('p', a.leitura + ' min de leitura', 'cartao__meta'));
      grade.appendChild(cartao);
    });
    document.getElementById('relacionados').hidden = false;
  });
})();
