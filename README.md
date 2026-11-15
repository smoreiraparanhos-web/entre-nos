# Entre Nós

**Um espaço para cuidar do que sentimos.**

Plataforma independente de saúde emocional: informação, acolhimento e caminhos de apoio.
Site estático em HTML5, CSS3 e JavaScript, sem dependências e sem requisições a terceiros.

## Como ver o site

Abra `index.html` no navegador, ou sirva a pasta:

```bash
python3 -m http.server 8000
```

Publicação: GitHub Pages, a partir da raiz da branch principal.

## Estrutura

```
index.html                 Página inicial
404.html                   Página de endereço inexistente (GitHub Pages)
sitemap.xml                Mapa do site
pages/                     conhecimento, momentos, encontrar-ajuda, sobre, privacidade, responsabilidade
pages/artigos/<slug>.html  Uma página estática por artigo
pages/artigo.html          Índice de leituras; redireciona os links antigos (?id=<slug>)
css/                       reset, variables (tokens e fontes), global, components, responsive
js/main.js                 Inicialização comum
js/navigation.js           Menu em telas pequenas
js/search.js               Busca e filtros da biblioteca
js/article.js              Redirecionamento dos links antigos de artigo
js/exercises.js            Exercícios da página Momentos
assets/fonts/              Newsreader (licença SIL OFL), hospedada localmente
assets/images/             hero.svg (ilustração provisória) e compartilhar.png (imagem de compartilhamento)
tools/gerar.py             Gerador das páginas e fonte dos textos dos artigos
tools/conteudo/*.html      Textos das páginas institucionais
```

## Como editar

As páginas HTML são geradas. Edite a fonte e rode o gerador:

```bash
python3 tools/gerar.py .
```

- **Artigos:** lista `ARTIGOS` em `tools/gerar.py`. Um artigo novo aparece sozinho na biblioteca, nos filtros, no índice de temas e no sitemap.
- **Revisão profissional:** em `artigo(...)`, os campos `revisado` (data ISO) e `revisor` (nome e registro profissional) trocam o aviso "Conteúdo em revisão" pela indicação de revisão. Só preencha com revisões que de fato aconteceram.
- **Textos institucionais:** `tools/conteudo/`.
- **Fotografia do início:** coloque o arquivo em `assets/images/` e ajuste `HERO` no topo da configuração em `tools/gerar.py` (arquivo, descrição e crédito). Proporção indicada: vertical, cerca de 900 x 1035 px, em JPEG ou WebP abaixo de 200 KB.
- **Endereço do site:** `SITE_URL` e `BASE_PATH` em `tools/gerar.py`. Mude os dois se o repositório ou o domínio mudar.

Editar um HTML gerado à mão funciona, mas a mudança se perde na próxima execução do gerador.

## Decisões documentadas

1. **Uma página estática por artigo.** Na primeira versão os artigos eram montados por JavaScript em `artigo.html?id=`. Leitores sem JavaScript, buscadores e pré-visualizações de link viam "Artigo não encontrado". Agora o texto está no HTML; `artigo.html` redireciona os links antigos.
2. **`js/data/articles.js` foi removido**: o conteúdo passou para o HTML e a fonte única é `tools/gerar.py`.
3. **Fonte Newsreader auto-hospedada** (SIL Open Font License) para os títulos e o texto dos artigos. Nenhuma requisição a terceiros.
4. **Ilustração provisória no lugar de fotografia.** Não foi possível obter fotos com licença verificada; o espaço está pronto para recebê-las.
5. **Nenhum armazenamento no navegador** (cookies, localStorage). Busca e exercícios rodam apenas no dispositivo.
6. **Scripts clássicos com `defer`** para que o site funcione também aberto direto do disco.
7. **Temas sem artigos** aparecem como "em preparação", em vez de conteúdo de preenchimento.
8. **`404.html` usa `<base href="/entre-nos/">`**, porque o GitHub Pages o serve em qualquer profundidade de endereço.

## Pendências

- [ ] **Revisão profissional dos 7 artigos.** Todos exibem "Conteúdo em revisão".
- [ ] **Conferir os links das fontes** (OMS, Ministério da Saúde, CVV): não foram verificados.
- [ ] **Conferir contatos e condições** de CVV (188), SAMU (192), CAPS e UBS.
- [ ] **Autoria:** hoje "Equipe Entre Nós". Definir a autoria real e decidir como informar o processo de redação.
- [ ] **Fotografias de natureza** com licença verificada, seguindo a direção fotográfica do projeto.
- [ ] Revisão jurídica das páginas de privacidade e responsabilidade.
- [ ] Testes com leitor de tela e auditoria WCAG completa.
- [ ] Enviar `sitemap.xml` ao Google Search Console.
