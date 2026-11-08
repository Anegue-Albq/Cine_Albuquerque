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

Problema encontrado: as tentativas de gravar a árvore e criar a branch pelo acesso conectado ao GitHub retornaram HTTP 403, Resource not accessible by integration. Os arquivos foram preparados localmente; não houve criação de branch, PR ou alteração da main. CI no GitHub e deployment ainda não foram executados.

Próximo passo: aplicar os arquivos no repositório por uma conexão com permissão de escrita, selecionar GitHub Actions em Settings > Pages e conferir as execuções reais. As evidências serão acrescentadas após isso.

Contagem parcial: três mensagens do usuário nesta prática, uma delas autorizando a implementação. Não representa uma versão final já validada em produção. Alterações manuais pelo aluno: nenhuma informada até este registro.

## Evidências a reunir para o PDF final

- URL do repositório e conteúdo do workflow.
- URL e resultado da CI em pull request.
- URL e resultado de CI e CD após push na main.
- URL pública e captura da aplicação publicada com a mudança visível.
- Prompts adicionais, problemas reais, ajustes, intervenções manuais e contagem final.
