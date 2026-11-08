# Prática DevOps: CI/CD com IA

## Projeto e estratégia

O Cine Albuquerque é um site estático com HTML, CSS e imagens. O deployment usa GitHub Pages por ser compatível com esses arquivos e integrado ao GitHub Actions. Não há dependências de aplicação ou etapa de compilação. O Python 3.12 executa uma verificação com a biblioteca padrão, sem pip install.

## Fluxo

O arquivo `.github/workflows/ci-cd.yml` executa CI em push na main e pull_request direcionado à main. A CI faz checkout, configura Python, verifica o site e prepara `_site` apenas com HTML, CSS e imagens. Em push na main, armazena esse conteúdo como artefato do Pages.

O job deploy depende de ci com `needs: ci` e só executa em push na main. Usa o artefato validado, o ambiente github-pages e permissões pages: write e id-token: write. Pull requests executam a verificação sem publicar.

Referência: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Configuração inicial e reprodução

1. No GitHub, abrir Settings > Pages > Build and deployment.
2. Selecionar GitHub Actions como Source. Essa configuração administrativa precisa ser confirmada pelo proprietário.
3. Abrir o PR da implementação e conferir o job Validar site na aba Checks.
4. Após integrar na main, conferir os jobs de CI e deployment na aba Actions.
5. Abrir a URL retornada pelo deployment. Conferir entrada demonstrativa, catálogo, imagens, resenhas e links de retorno.
6. Fazer uma alteração visível no site por novo PR e integrar na main; confirmar que a nova versão foi publicada automaticamente.

Localmente: `python3 scripts/validate_site.py`.

## Escopo da verificação

Verifica a existência das 13 páginas esperadas, título e idioma declarados, referências locais em src/href/action e url() de CSS, caminhos relativos e imagens com src. Também bloqueia o envio de uma senha demonstrativa por um input com name.

Não é um validador completo de HTML/CSS nem verifica disponibilidade de serviços externos, conteúdo das imagens ou autenticação. O login é uma demonstração sem autenticação; os campos não são enviados ao catálogo.

## Registro do uso da IA em 08/11/2026

### Interação 1: análise do enunciado

Prompt: “Vamos realizar essa prática de Devops, que requer auxílio de inteligência artificial”; analisar o documento, explicar a participação e aguardar o link do repositório.

Resultado: identificação das exigências de CI, CD, evidências e PDF final. Nenhum arquivo do projeto foi alterado nessa interação.

### Interação 2: escolha do projeto

Prompt: `https://github.com/Anegue-Albq/Cine_Albuquerque`

Resultado: análise do código e definição da estratégia GitHub Pages. Foram identificados caminho Windows em imagem e envio de campos do login demonstrativo pela URL.

### Interação 3: implementação

Prompt: “Certo, pode fazer as alterações necessárias, e após delas, me mande uma descrição nesse formato para cada bloco de alterações: (Diff 1 - ***.tipo-do-arquivo) : ‘Alterações’ …”

Alterações pela IA: correção do caminho da imagem, remoção de imagens sem src, identificação do login como demonstrativo e remoção dos names dos campos, criação do verificador, workflow e deste registro.

Verificação local: 13 páginas e 49 referências locais aprovadas. Em cópias temporárias, o verificador rejeitou três falhas introduzidas: referência a arquivo inexistente, caminho Windows e envio da senha demonstrativa.

### Interação 4: envio e publicação

Prompt: “Pode fazer isso pra mim: Suba o commit e de push na branch principal, depois realize o deploy”

Resultado: commit [064ee86](https://github.com/Anegue-Albq/Cine_Albuquerque/commit/064ee86f80b80209faae49c8eb7babd3f01e576e) enviado diretamente à main. A CI e o deployment foram concluídos com sucesso no GitHub Actions.

Contagem do recorte técnico registrado: quatro interações relevantes para análise, implementação e publicação. Os prompts da primeira e da terceira interação foram apresentados como trechos ou resumos; essa contagem não representa todas as mensagens da conversa. Alterações manuais no código pelo aluno: nenhuma informada.

## Evidências verificadas

- [Repositório](https://github.com/Anegue-Albq/Cine_Albuquerque).
- [Pipeline](../.github/workflows/ci-cd.yml).
- [Execução de CI/CD na main](https://github.com/Anegue-Albq/Cine_Albuquerque/actions/runs/42529806145): job Validar site e job Publicar no GitHub Pages concluídos com sucesso.
- [Aplicação publicada](https://anegue-albq.github.io/Cine_Albuquerque/): entrada atualizada com o texto Login demonstrativo.
- Verificação HTTP após o deployment: resposta 200 na entrada, site.html, resenha1.html e na imagem corrigida do título.
- Validação local: 13 páginas e 49 referências locais aprovadas; três cenários de falha introduzidos em cópias temporárias foram rejeitados.

## Validação em pull request

Esta atualização de documentação será enviada em uma branch separada e em PR direcionado à main para comprovar o gatilho pull_request. O resultado deverá ser conferido na aba Checks da PR. Nesse evento, o job de CI deve executar e o job de deployment deve ser ignorado.

O teste em PR é adicional ao fluxo de push e deployment já comprovado. Seu resultado não é considerado aprovado até a conclusão real do GitHub Actions.

## Próxima entrega

Reunir o resultado da CI na PR, capturas das execuções e do site publicado e consolidar o PDF com pipeline, registro técnico, alterações e análise do processo.
