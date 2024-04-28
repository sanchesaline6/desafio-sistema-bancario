# Desafio - Criando um Sistema Bancário com Python

## Versão 1

### Instruções

Fomos contratado por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

#### Operação de depósito

Deve ser possível depositar valores positivos para a minha conta bancária . A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

#### Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrado.

#### Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

## Versão 2


### Função de saque

A função de saque deve receber os argmuentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

### Cadastrar usuário (cliente do banco)

O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

### Cadastrar conta bancária (vincular com usuário)

O programa deve armazenar contas em uma lista, uma contaé composta por agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário (cliente)

### Dica

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

## Versão 3

### Objetivo Geral
Iniciar a modelagem do sistema bancário em POO. Adicionar classes para cliente e as operaçoes bancárias: depósito e saque.
Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés
de dicionários. O código deve seguir o mdoelo de classes UML a seguir:

[!Diagrama UML - Sistema Bancário](content/uml_bancario.png)

### Desafio extra

Após concluir a modelagem das classes e a criação dos métodos. Atualizar os métodos que tratam as opções do menu,
para funcionarem com as classes modeladas.