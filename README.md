# SysAdmin Gerência de Provedor
Sistema integrado para gerência de provedor de internet 

[Veja descrição básica do projeto aqui](Descrição.md)

-------------------------------

## Tecnologias Utilizadas

- Python 3.7
- Django 2.2
- SQLite 3

-------------------------------

## Regras de Uso do GIT

### Gitignore

- O arquivo ```.gitignore``` é um item de configuração do software
- Deve ser ignorado do rastreio:
  - artefatos de configuração de IDE
  - arquivos objetos de compilação
  - arquivos temporários
  - qualquer outro artefato que não componha documentação ou código-fonte do software

### Commit

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
