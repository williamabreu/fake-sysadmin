# Casos de Teste


## Cadastrar Plano

- AÇÃO:
    ```
    - Preencher Nome e Valor
    - Clicar em salvar
    ```

- RESULTADO ESPERADO:
    ```
    - Novo registro adicionado na tabela Plan
    ```

---------------------------------------

## Modificar Plano

- AÇÃO:
    ```
    - Alterar Nome e/ou Valor
    - Clicar em salvar
    ```

- RESULTADO ESPERADO:
    ```
    - Se algum dos valores for alterado...
        - Novo registro adicionado na tabela Plan
    - Senão...
        - Nenhuma alteração
    ```

---------------------------------------

## Excluir Plano

- AÇÃO:
    ```
    - Clicar em excluir
    ```

- RESULTADO ESPERADO:
    ```
    - Registro removido da tabela Plan
    ```

## Cadastrar Cliente

- AÇÃO:
    ```
    - Preencher Nome, CPF, RG, Data de Nascimento e Endereço
    - Escolher Plano
    - Preencher Data e Hora de instalação
    - Clicar em salvar
    ```

- RESULTADO ESPERADO:
    ```
    - Novo registro adicionado na tabela Person
    - Novo registro adicionado na tabela Contract
    - Novo registro adicionado na tabela Schedule, diferente dos demais (único)
    - Novo registro adicionado na tabela Client
    ```

---------------------------------------

## Modificar cadastro do Cliente

- AÇÃO:
    ```
    - Alerar Nome, CPF, RG, Data de Nascimento e Endereço
    - Clicar em salvar
    ```

- RESULTADO ESPERADO:
    ```
    - Se algum dos valores for alterado...
        - Alterar o(s) registro(s) na tabela Person
    - Senão...
        - Nenhuma alteração
    ```

---------------------------------------

## Alterar plano do Cliente

- AÇÃO:
    ```
    - Escolher Plano
    - Clicar em salvar
    ```

- RESULTADO ESPERADO:
    ```
    - Se o plano for alterado...
        - Exclusão do registro antigo da tabela Contract
        - Adição do novo registro na tabela Contract
        - Alteração da chave-estrangeira Contract do registro na tabela Client
    - Senão...
        - Nenhuma alteração
    ```

---------------------------------------

## Cancelar assinatura do Cliente

- AÇÃO:
    ```
    - Clicar em cancelar assinatura.
    ```

- RESULTADO ESPERADO:
    ```
    - Exclusão do registro na tabela Person
    - Exclusão do registro na tabela Contract
    - Exclusão do registro na tabela Schedule
    - Exclusão do registro na tabela Client
    ```

---------------------------------------