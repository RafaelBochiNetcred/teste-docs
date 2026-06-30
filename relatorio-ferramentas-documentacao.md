# Relatorio de ferramentas para documentacao da API

Este relatorio compara Redocly, Docusaurus e Mintlify para a documentacao da API, considerando o cenario atual: documentacao para clientes integradores, paginas estaticas em Markdown e referencia tecnica gerada a partir de um unico arquivo OpenAPI.

## Contexto

A API hoje utiliza Postman como referencia de documentacao, mas o processo exige atualizacao manual e aumenta o risco de divergencia entre implementacao e documentacao. A nova estrutura precisa permitir:

- manter paginas estaticas simples para guias, autenticacao, conceitos e webhooks;
- gerar a referencia tecnica automaticamente a partir do OpenAPI;
- separar bem conteudo editorial de schemas da API;
- publicar uma experiencia clara para clientes que integram com a API;
- rodar validacoes em CI/CD para evitar documentacao quebrada.

## Criterios de avaliacao

- Experiencia do cliente integrador;
- Suporte a OpenAPI;
- Facilidade para misturar Markdown e referencia de API;
- Custo para um time de 9 pessoas;
- Build e deploy;
- CI/CD;
- Changelog;
- Manutencao e curva de aprendizado;
- Flexibilidade de customizacao.

## Resumo executivo

| Ferramenta | Melhor uso | Ponto forte | Ponto de atencao |
| --- | --- | --- | --- |
| Redocly | Portal de API mais tecnico e robusto | OpenAPI nativo, lint, preview e governanca | Custo por assento e maior acoplamento com a plataforma |
| Docusaurus | Documentacao controlada pelo time e hospedada internamente | Open source, flexivel e sem custo de licenca | OpenAPI depende de plugins e exige mais manutencao |
| Mintlify | Documentacao moderna com boa experiencia visual | Setup simples, boa UX e suporte direto a OpenAPI | Plano pago/Enterprise pode depender de negociacao comercial |

## Comparativo de preco

Valores considerados para um time de 9 pessoas, com base nas paginas publicas de precos consultadas em 26/06/2026.

| Ferramenta | Modelo | Estimativa para 9 pessoas |
| --- | --- | --- |
| Redocly Pro | US$ 10 por usuario/mes | US$ 90/mes ou US$ 1.080/ano |
| Redocly Enterprise | US$ 24 por usuario/mes | US$ 216/mes ou US$ 2.592/ano |
| Docusaurus | Open source | US$ 0 de licenca, mas exige infraestrutura e manutencao |
| Mintlify Starter | Plano gratuito | US$ 0, com limites do plano |
| Mintlify Enterprise | Sob consulta | Precisa validacao comercial |

O Docusaurus tende a ser o menor custo direto, mas nao significa custo zero operacional. Ele exige que o time mantenha build, hospedagem, plugins, atualizacoes e ajustes de layout.

O Redocly tem custo previsivel por usuario e oferece mais recursos prontos para documentacao de API. Para um portal tecnico, reduz trabalho de manutencao.

O Mintlify pode ser competitivo se o plano gratuito atender, mas para uso corporativo e recursos avancados pode exigir plano Enterprise.

## Redocly

### Pontos positivos

- Suporte nativo e maduro a OpenAPI.
- Boa experiencia para referencia tecnica de endpoints.
- Redocly CLI permite lint, validacao e build local.
- Facil separar paginas estaticas de schemas.
- Bom encaixe para API portal.
- Recursos de governanca ajudam a manter padrao de contrato.
- Menor risco tecnico para exibicao de schemas, exemplos, request e response.

### Pontos negativos

- Custo por usuario.
- Menor liberdade visual que uma aplicacao totalmente customizada.
- Pode gerar dependencia da plataforma Redocly.
- Algumas capacidades avancadas ficam associadas aos planos pagos.

### CI/CD

Redocly e forte nesse ponto. O fluxo recomendado pode incluir:

- gerar `openapi.yaml` a partir do backend;
- rodar `redocly lint`;
- rodar build da documentacao;
- publicar apenas se lint e build passarem.

Isso ajuda a impedir que schemas invalidos ou breaking changes entrem sem revisao.

### Changelog

Pode ser mantido como paginas Markdown versionadas no repositorio. Em fluxos mais maduros, pode ser combinado com comparacao de OpenAPI para identificar mudancas relevantes de contrato.

### Build e deploy

O build e direto com a CLI da Redocly. A publicacao pode acontecer na propria plataforma ou em uma esteira interna, dependendo do modelo contratado.

### Adequacao ao projeto

E a ferramenta mais alinhada se a prioridade principal for referencia de API confiavel e com pouca manutencao. Para clientes integradores, tende a entregar a experiencia tecnica mais consistente.

## Docusaurus

### Pontos positivos

- Open source e sem custo de licenca.
- Grande flexibilidade de customizacao.
- Bom para documentacao em Markdown.
- Permite controlar completamente hospedagem, pipeline e layout.
- Funciona bem para paginas estaticas, guias e conteudo explicativo.
- Comunidade ampla e ecossistema maduro.

### Pontos negativos

- Nao possui suporte nativo completo a OpenAPI.
- Depende de plugins, como `redocusaurus`, para renderizar schemas.
- Exige mais manutencao tecnica.
- Pode haver incompatibilidade entre versoes de Docusaurus, React e plugins.
- A experiencia de API pode ser inferior a ferramentas especializadas, se nao houver cuidado no setup.

### CI/CD

O fluxo recomendado pode incluir:

- gerar `openapi.yaml` automaticamente;
- validar o OpenAPI com uma ferramenta externa, como Redocly CLI ou Spectral;
- executar `npm run build`;
- publicar o conteudo estatico gerado.

Como o Docusaurus nao e focado em governanca de API, a validacao do contrato precisa ser adicionada explicitamente ao pipeline.

### Esforco estimado para CI/CD

Para avaliar se o Docusaurus compensa financeiramente, e importante comparar o custo evitado de uma ferramenta paga com o tempo necessario para montar e manter a esteira.

Considerando Redocly Pro como referencia de custo, com 7 colaboradores a US$ 10 por usuario/mes, o custo seria:

| Base de comparacao | Custo |
| --- | ---: |
| 7 usuarios x US$ 10/mes | US$ 70/mes |
| Custo anual | US$ 840/ano |

Esse valor cresce linearmente conforme mais pessoas precisam de acesso. Com 9 colaboradores, por exemplo, o custo passa para US$ 90/mes ou US$ 1.080/ano.

Para o Docusaurus, o custo direto de licenca e zero, mas existe custo de implementacao e manutencao. Um levantamento realista de tarefas seria:

| Tarefa | Estimativa |
| --- | ---: |
| Gerar `openapi.yaml` automaticamente no pipeline | 0,5 a 1 dia |
| Configurar build do Docusaurus em CI | 0,5 dia |
| Validar OpenAPI com Redocly CLI, Spectral ou ferramenta equivalente | 0,5 a 1 dia |
| Configurar deploy estatico, por exemplo S3 + CloudFront | 1 a 2 dias |
| Configurar dominio, HTTPS, cache e invalidacao de CDN | 0,5 a 1 dia |
| Configurar preview por pull request, se necessario | 1 a 2 dias |
| Configurar validacao de links e arquivos quebrados | 0,5 dia |
| Criar processo de changelog | 0,5 a 1 dia |
| Documentar processo interno de publicacao | 0,5 dia |
| Ajustes finos de navegacao, sidebar e renderizacao do OpenAPI | 1 a 2 dias |

Estimativa total:

| Escopo | Tempo estimado |
| --- | ---: |
| CI/CD minimo | 2 a 4 dias |
| CI/CD completo com deploy, validacoes e preview | 5 a 9 dias |
| Manutencao recorrente | 0,5 a 2 dias por mes, dependendo da instabilidade dos plugins e mudancas no schema |

O ponto financeiro principal e que o custo anual de Redocly Pro para 7 pessoas, US$ 840/ano, pode ser menor que o custo de alguns dias de engenharia. Se um dia de trabalho de engenharia custar mais que US$ 420, dois dias de implementacao ja equivalem aproximadamente a um ano de Redocly Pro para 7 usuarios.

Com isso, Docusaurus so paga melhor quando pelo menos uma destas condicoes for verdadeira:

- o time valoriza muito controle total sobre hospedagem, layout e pipeline;
- ja existe infraestrutura padrao para sites estaticos na AWS;
- o time quer evitar custo recorrente por assento no longo prazo;
- poucas pessoas vao manter a documentacao;
- a documentacao sera simples e a referencia OpenAPI nao exigira muitos recursos avancados.

Se o objetivo for reduzir tempo de implementacao, diminuir manutencao e entregar uma experiencia de API mais pronta para clientes, a economia de licenca do Docusaurus pode nao compensar. Nesse caso, pagar US$ 70/mes para 7 pessoas pode ser justificavel, principalmente se evitar uma ou duas semanas de setup e manutencao futura.

### Changelog

Pode ser implementado com paginas Markdown, blog do Docusaurus ou uma secao especifica de releases. A flexibilidade e boa, mas o processo precisa ser definido pelo time.

### Build e deploy

O build gera arquivos estaticos, o que facilita deploy em Vercel, Netlify, S3, CloudFront, GitHub Pages ou infraestrutura propria.

### Adequacao ao projeto

E uma boa escolha se o time quer controle total, custo direto baixo e uma documentacao simples, separando paginas estaticas da referencia OpenAPI. O ponto de atencao e que a parte de schema depende de integracao adicional.

## Mintlify

### Pontos positivos

- Experiencia visual moderna e amigavel para clientes.
- Suporte simples a Markdown/MDX.
- Suporte a OpenAPI e API playground.
- Configuracao de navegacao simples via `docs.json`.
- Boa opcao para documentacao publica ou semi-publica com foco em UX.
- Baixa friccao para criar uma experiencia polida rapidamente.

### Pontos negativos

- Menos controle total que uma solucao hospedada internamente.
- Plano Enterprise pode exigir contato comercial.
- Pode haver limitacoes de customizacao dependendo do plano.
- O time fica mais dependente do modelo e convencoes da plataforma.

### CI/CD

Mintlify oferece validacoes como broken links e pode ser integrado ao fluxo de deploy. Um pipeline recomendado inclui:

- gerar `openapi.yaml`;
- validar links e estrutura da documentacao;
- validar schema OpenAPI;
- publicar quando as validacoes passarem.

### Changelog

Mintlify tem suporte especifico para changelog, o que facilita comunicar mudancas de API aos clientes. Para uma API consumida por integradores, esse e um ponto importante.

### Build e deploy

O desenvolvimento local usa a CLI da Mintlify. O deploy segue o fluxo da plataforma, com integracao ao repositorio. A vantagem e reduzir trabalho operacional; a desvantagem e depender mais da plataforma.

### Adequacao ao projeto

E uma boa escolha se a prioridade for uma documentacao com excelente experiencia para o cliente e baixo esforco de apresentacao. Faz sentido quando o time quer uma documentacao bonita e organizada sem manter muitos detalhes de frontend.

## Comparativo por criterio

| Criterio | Redocly | Docusaurus | Mintlify |
| --- | --- | --- | --- |
| OpenAPI | Excelente | Bom com plugin | Muito bom |
| Paginas estaticas | Bom | Excelente | Excelente |
| UX para cliente | Muito boa | Depende do setup | Excelente |
| Custo direto | Medio | Baixo | Baixo a indefinido |
| Manutencao | Baixa/media | Media/alta | Baixa |
| Controle visual | Medio | Alto | Medio |
| CI/CD | Forte | Precisa montar | Bom |
| Changelog | Bom, mas depende do fluxo | Manual/flexivel | Forte |
| Build estatico | Sim | Sim | Plataforma/CLI |
| Risco tecnico | Baixo | Medio | Baixo/medio |

## Recomendacao

Para o cenario da API, a melhor escolha depende da prioridade principal.

Se o foco for a melhor experiencia tecnica para integradores, com OpenAPI como parte central da documentacao, Redocly e a opcao mais segura. Ele reduz risco na renderizacao de schemas e oferece melhores recursos nativos para governanca de API.

Se o foco for custo direto baixo, controle total e uma documentacao simples, Docusaurus e uma alternativa viavel. Ele atende bem a estrutura de paginas estaticas separadas da referencia de API, desde que o time aceite manter plugins e validacoes adicionais.

Se o foco for velocidade, boa apresentacao e experiencia moderna para clientes, Mintlify e uma alternativa muito forte. Ele parece especialmente adequado quando a documentacao precisa parecer produto, nao apenas um site tecnico.

## Conclusao

Considerando que a documentacao sera usada por clientes que integram com a API, a experiencia do consumidor deve pesar mais que apenas o custo de licenca.

A recomendacao principal e priorizar Redocly ou Mintlify.

Redocly e mais indicado se a referencia OpenAPI for o centro da experiencia e se o time quiser mais seguranca tecnica para contrato de API.

Mintlify e mais indicado se o objetivo for entregar rapidamente uma documentacao moderna, organizada e agradavel para clientes.

Docusaurus continua sendo uma boa opcao se o time quiser controle total e baixo custo direto, mas exige mais responsabilidade interna sobre plugins, build, validacao de OpenAPI e experiencia final.

Para a estrutura atual, onde existe um unico schema OpenAPI e paginas estaticas simples, as tres ferramentas comportam o projeto. A diferenca esta menos na capacidade de suportar a estrutura e mais no custo operacional e na qualidade da experiencia entregue ao cliente.

## Fontes consultadas

- Redocly Pricing: https://redocly.com/pricing
- Redocly CLI: https://redocly.com/docs/cli
- Docusaurus Documentation: https://docusaurus.io/docs
- Docusaurus Deployment: https://docusaurus.io/docs/deployment
- Mintlify Pricing: https://www.mintlify.com/pricing
- Mintlify OpenAPI Setup: https://www.mintlify.com/docs/api-playground/openapi-setup
- Mintlify CI: https://www.mintlify.com/docs/deploy/ci
- Mintlify Changelogs: https://www.mintlify.com/docs/create/changelogs
