# SysAdmin Gerência de Provedor
Sistema integrado para gerência de provedor de internet 

[Veja descrição básica do projeto aqui](Descrição.md)

-------------------------------

## Tecnologias Utilizadas

- Python 3.7
- Django 2.2
- SQLite 3
- HTML 5
- CSS 3
- Bootstrap 4

-------------------------------

## Regras de Uso do GIT

### Organização do Repositório

```
.
├─── docs                  # Contém artefatos de docuementação do software
|
└─── src                   # Contém código-fonte do software
     |
     ├─── AdminFinanceiro  # Contém código-fonte de implementação do software
     |
     ├─── Atendente        # Contém código-fonte de implementação do software
     |
     ├─── Base             # Contém código-fonte de implementação do software
     |
     └─── sysadmin         # Contém código-fonte de configuração do framework
```

### Gitignore

- O arquivo ```.gitignore``` é um item de configuração do software
- Deve ser ignorado do rastreio:
  - artefatos de configuração de IDE
  - arquivos objetos de compilação
  - arquivos temporários
  - qualquer outro artefato que não componha documentação ou código-fonte do software

### Commits

- Um commit deve ter o seguinte formato:

```
Resumo curto (72 caracteres ou menos)

Texto explicativo mais detalhado. Use no máximo 72 caracteres por linha
escrita. Use 1 linha em branco para separar cada componente. O corpo
explicativo é opcional, desde que o resumo curto seja mais que 
suficiente.

Outros parágrafos vêm depois de linhas em branco:
- Tópicos também podem ser usados.
- Use 1 hífen seguido por 1 espaço único e idetação com 4 espaços.

[FIX #0]
```

- Commits devem ser atômicos, não devendo englobar várias modificações de um vez.
- A primeira linha de commit é a mais importante (resumo curto) e deve ser iniciada com verbo no particípio.
- Descreva porque uma mudança está sendo feita, como resolve o problema e quais os efeitos colaterais dela.
- Descreva quaisquer limitações do código atual.
- Faça rastreio bidirecional com issues do repositório, usando palara-chave para realizar ação automática no GitHub.

### Branches

- A branch ```master``` deve conter uma versão funcional do software.
- Para cada funcionalidade a ser desenvolvida ou corrigida, criar uma branch ```dev-<nome_da_funcionalidade>```.
- Após testar e validar a funcionalidade, fazer o merge da branch com a ```master```.

### Tags e Releases

- Criar uma release (tag) para cada nova versão do software na branch ```master```.
- Utilizar números de versão no formato ```X.Y``` .
- Incrementar somente o número Y da versão quando corrigir um bug.
- Incrementar o número X e zerar o Y quando lançar uma nova versão a partir de novos requisitos.

-------------------------------

## Regras de Codificação

Como o projeto será codificado nas linguagens Python, HTML e CSS, devem ser seguidas as convenções amplamente aceitas pelo mercado atual, isto é, convenções defindas pela Python Foundation e pela W3C. 

Também devem ser seguidas convenções de documentação de código, que devem ser seguidas somente no código de back-end (Python).

Convenções de notação são aplicadas a qualquer código, pois envolvem a semântica dos identificadores.

### Convenções de codificação

- [Convenções oficiais de codificação em Python, PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [Convenções definidas pelo Google para HTML/CSS](https://google.github.io/styleguide/htmlcssguide.html)

### Convenções de documentação de código

- [Convenções de docstrings em Python, PEP 257](https://www.python.org/dev/peps/pep-0257/)

### Convenções de notação

- Nomes de classes, estruturas e correlatos devem ser um substantivo concreto ou abstrato.
- Nomes de constantes devem ser um substantivo concreto ou abstrato.
- Nomes de atributos e variáveis devem ser um substantivo concreto ou abstrato.
- Métodos, funções e procedimentos devem ser um verbo no imperativo, indicando ação.
- Ao utilizar siglas para nomes, esta deverá ser escrita em caixa alta. O restante do nome deve seguir a regra aplicável a ele.
- Os nomes devem ser suficientemente sugestivos, deixando explícito seu propósito de uso.
- Nomes devem seguir a codificação ASCII (7 bits) e devem ter no máximo 31 caracteres.
- Não se deve utilizar nomes demasiadamente abreviados. Abreviaturas aceitáveis deverão ser explicitamente comentadas. Nomes referenciando expressões matemáticas, se utilizados, também devem ser devidamente comentados.

-------------------------------

## Padrões de Projeto

Os padrões de projeto aplicados ao framework Django podem ser consultados no livro "Django Design Patterns and Best Practices" ```[1]```.

```[1]``` RAVINDRAN, Arun. _Django Design Patterns and Best Practices_: 2. ed. Birmingham: Packt Publishing, 2015. ISBN 978-1-78398-664-4.

[//]: # (Link para compra do livro:)
[//]: # (https://www.packtpub.com/web-development/django-design-patterns-and-best-practices-second-edition)
[//]: # (Link para download gratuito do livro:)
[//]: # (https://docplayer.net/53000043-Django-design-patterns-and-best-practices.html)
