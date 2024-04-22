"""Neste módulo você construirá um simulador de
cadastro de senha e inicialização de celular.

Vamos supor que o usuário acabou de comprar um celular na loja e
após a primeira carga, ele liga o celular pela primeira vez.

Ao iniciar o celular, a primeira coisa que aparece na tela é o pedido
para cadastrar a senha e, logo após, confirmar a senha.

Essa é a sua primeira tarefa.
Construa o pedido de senha e confirmação.
Se a senha confirmada estiver correta, exiba a mensagem: Senha
correta. Bem-vindo.
Senão, exiba a mensagem: Senha incorreta. Tente novamente."""



print('----------------------Seja Bem-Vindo--------------------------')
print('----------Iremos Cadastrar suas Credenciais-------------------')
senha = input('Informe a senha: ')
confirme = input('Coloque sua Senha novamente para confirmação: ')

if senha == confirme:
    print('Senha correta. Bem-vindo.')
else:
    print('Senha incorreta. Tente novamente.')
