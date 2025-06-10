#Usuario informa a senha para logar.
senha: str = (input("Informe a senha: "))

if senha == "proz@2025":
    print("Logado com sucesso")
else:
    print("Senha inválida")
    
    

lista_contatos: list = []
while True: 
    opcao: str = input(''' \n Bem vindo a sua Agenda \n O que deseja fazer: 
\n A - Inserir contato \n B - Exibir contatos \n C - Editar contato \n D - Excluir contatos \n X - Sair \n''')
    
    match opcao.upper():
        case "A": #inserir contato
            nome_contato: str = input("Nome: ")
            telefone_contato: str = input("Telefone: ")
            email_contato: str = input("E-mail: ")
            cidade_contato: str = input("Cidade: ")
            contato = {
                "nome": nome_contato,
                "telefone": telefone_contato,
                "e-mail": email_contato,
                "cidade": cidade_contato,
            }
            lista_contatos.append(contato)
            print("Contato adicionado com sucesso")
            
              
            
    
        
    
    











