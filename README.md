# Entre Nós

**Um espaço para cuidar do que sentimos.**

Plataforma digital de saúde emocional: informação, acolhimento e caminhos de apoio.
Site estático em HTML5, CSS3 e JavaScript, sem dependências e sem requisições a terceiros.

## Como ver o site

Abra `index.html` no navegador, ou sirva a pasta:

```bash
python3 -m http.server 8000
```

Para publicar: envie a pasta a um repositório GitHub e ative o GitHub Pages na branch principal (raiz).

## Estrutura

```
index.html              Página inicial
pages/                  conhecimento, artigo, momentos, encontrar-ajuda, sobre, privacidade, responsabilidade
css/                    reset, variables (tokens), global, components, responsive
js/main.js              Inicialização comum
js/navigation.js        Menu em telas pequenas
js/search.js            Busca e filtros da biblioteca
js/article.js           Monta a leitura em artigo.html?id=<slug>
js/exercises.js         Exercícios da página Momentos
js/data/articles.js     Conteúdo dos artigos
assets/                 Ícones, imagens e fontes
tools/gerar.py          Gerador das páginas (opcional)
```

## Decisões documentadas

Ajustes em relação ao Documento Mestre v1.0:

1. **`js/data/articles.js` e `js/article.js`** foram acrescentados: os artigos ficam em um arquivo de dados e `pages/artigo.html` é o modelo único de leitura (`?id=<slug>`).
2. **`tools/gerar.py`** gera as oito páginas com cabeçalho e rodapé idênticos e é a fonte dos textos dos artigos. Uso: `python3 tools/gerar.py .` As páginas também podem ser editadas à mão; nesse caso, não rode o gerador depois, pois ele sobrescreve.
3. **Fontes do sistema** em vez de webfonts: nenhuma requisição externa (privacidade e desempenho). `assets/fonts/` fica reservada para fontes auto-hospedadas.
4. **Sem fotografias por enquanto**: a paisagem do início é um SVG na paleta do projeto. Fotos reais devem seguir a direção fotográfica do documento e ter licença verificada.
5. **Nenhum armazenamento no navegador** (cookies, localStorage). Busca e exercícios rodam apenas no dispositivo.
6. **Scripts clássicos com `defer`** (e não módulos ES) para que o site funcione também aberto direto do disco.
7. **Categorias sem artigos** aparecem nos filtros com um aviso de "em construção", em vez de conteúdo de preenchimento.

## Pendências antes da publicação (Fases 3 e 4)

- [ ] **Revisão profissional dos 7 artigos.** Todos exibem "Conteúdo em revisão". Após revisar, preencha `revisado` (data ISO) e `revisor` no artigo.
- [ ] **Conferir os links das fontes** (OMS, Ministério da Saúde, CVV): não foram verificados automaticamente.
- [ ] **Conferir contatos e condições** de CVV (188), SAMU (192), CAPS e UBS.
- [ ] Definir autoria real dos artigos (hoje: "Equipe Entre Nós").
- [ ] Revisão jurídica das páginas de privacidade e responsabilidade.
- [ ] Testes com leitor de tela e auditoria WCAG completa.
- [ ] Imagem de compartilhamento (`og:image`), `sitemap.xml` e URL canônica após definir o domínio.

## Como adicionar um artigo

Com o gerador: acrescente o artigo em `ARTIGOS` em `tools/gerar.py` e rode-o.
À mão: adicione o objeto em `js/data/articles.js` e um cartão em `pages/conhecimento.html`.
