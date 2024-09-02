import app.utils.db_methods as db_service
import time
from datetime import datetime

class Usuario:
    def login():
        menu = """
                             Sistema de Gestão de Projetos                    
        """

        print(menu)
        login = input("Insira sua credencial de acesso (cpf): ")
        senha = input("Insira a sua senha: ")

        return login, senha
    
    def cadastro():
        login = ""
        senha = ""

        menu = """
                             Sistema de Gestão de Projetos                    
        """

        print(menu)
        tipo_usuario = input("Tipo do Usuário (Usuário (U), Gerente (G), Gerente Master (GM)): ")
        if (tipo_usuario in ["U", "G", "GM"]):
            if (tipo_usuario == "G" or tipo_usuario == "GM"):
                primeiro_acesso = input("Primeiro Acesso? (s/n): ")
                if primeiro_acesso == "s":
                    tipo_usuario = "GM"
                    print("Realize o cadastro de Gerente Master")
                    nome = input("Insira seu nome: ")
                    sobrenome = input("Insira seu sobrenome: ")
                    email = input("Insira seu email: ")
                    login = input("Insira seu cpf (apenas números): ")
                    senha = input("Insira a sua senha: ")
                    senha_master = input("Crie a sua senha de acesso privilegiado: ")

                    db_service.cadastra_usuario(nome, sobrenome, email, login, senha, tipo_usuario, senha_master)
                    print("\n\033[1mCadastro concluído com sucesso!\n\033[0m")
                elif primeiro_acesso == "n":
                    login_gm = input("Insira o cpf com acesso privilegiado: ")
                    senha_master = input("Insira a senha para acesso privilegiado: ")
                    permissao = db_service.verifica_GerenteMaster(login_gm, senha_master)
                    if (permissao):
                        nome = input("Insira seu nome: ")
                        sobrenome = input("Insira seu sobrenome: ")
                        email = input("Insira seu email: ")
                        login = input("Insira seu cpf (apenas números): ")
                        senha = input("Insira a sua senha: ")
                        senha_master = input("Crie a sua senha de acesso privilegiado: ")
                        db_service.cadastra_usuario(nome, sobrenome, email, login, senha, tipo_usuario, senha_master)
                        print("\n\033[1mCadastro concluído com sucesso!\n\033[0m")
                    else:
                        print("\n\033[1mAcesso negado! Você não possui permissão!\n\033[0m")

            elif (tipo_usuario == "U"):
                nome = input("Insira seu nome: ")
                sobrenome = input("Insira seu sobrenome: ")
                email = input("Insira seu email: ")
                login = input("Insira seu cpf (apenas números): ")
                senha = input("Insira a sua senha: ")

                db_service.cadastra_usuario(nome, sobrenome, email, login, senha, tipo_usuario)
                print("\n\033[1mCadastro concluído com sucesso!\n\033[0m")
        else:
            print("\n\033[1mDigite um tipo de usuário válido!\033[0m")

        return login, senha
    

    def progresso_projeto():
        id_usuario = []
        projetos_usuario = []

        while(len(id_usuario) <= 0):
            menu = """
                                Sistema de Gestão de Projetos                    
            """
            print(menu)
            cpf = input("Digite o seu cpf: ")
            id_usuario = db_service.consulta_id(cpf)

            if(len(id_usuario) <= 0):
                print("\n\033[1mUsuário Inválido!\n\033[0m")
                menu = """
                                        Sistema de Gestão de Projetos

                1 - Volta ao menu inicial                           2 - Tentar novamente                    
                """

                opc_menu = None
                while(opc_menu != 1): 
                    print(menu)
                    opc_menu = input("Selecione uma opção: ")
                    if(opc_menu == '1'):
                        return None
                    elif(opc_menu == '2'):
                        break
                    else:
                        print("Digite uma opção válida!")
            
        id_usuario = id_usuario[0][0]

        projetos = db_service.consulta_projeto(id_usuario)

        for projeto in projetos:
            id = str(projeto[2])
            if len(id) > 0:
                ids_usuario = id.replace("[", "").replace("]", "").split(",")
                for i in range(len(ids_usuario)):
                    ids_usuario[i] = ids_usuario[i].strip()
                
                if(str(id_usuario) in ids_usuario):
                    projetos_usuario.append(projeto)

        if(len(projetos_usuario) > 0):
            for projeto in projetos_usuario:
                print(f"\n\033[1mNome projeto\033[0m: {str(projeto[3])} - \033[1mStatus\033[0m: {str(projeto[7])}")
        else:
            print("Nenhum projeto encontrado!")

        time.sleep(5)

        opc_menu = None
        while(opc_menu != 1):
            menu = """
                             Sistema de Gestão de Projetos
            
1 - Voltar ao menu inicial                                                    
            """
            
            print(menu)
            opc_menu = input("Selecione uma opção: ")
            if(opc_menu == '1'):
                return None
            else:
                print("Digite uma opção válida!")

        
    def comunicacao():
        id_usuario = []
        projetos_usuario = []

        while(len(id_usuario) <= 0):
            menu = """
                                Sistema de Gestão de Projetos                    
            """
            print(menu)
            cpf = input("Digite o seu cpf: ")
            id_usuario = db_service.consulta_id(cpf)

            if(len(id_usuario) <= 0):
                print("\n\033[1mUsuário Inválido!\n\033[0m")
                menu = """
                                        Sistema de Gestão de Projetos

                1 - Volta ao menu inicial                           2 - Tentar novamente                    
                """

                opc_menu = None
                while(opc_menu != 1): 
                    print(menu)
                    opc_menu = input("Selecione uma opção: ")
                    if(opc_menu == '1'):
                        return None
                    elif(opc_menu == '2'):
                        break
                    else:
                        print("Digite uma opção válida!")
        
        id_usuario = id_usuario[0][0]

        projetos = db_service.consulta_projeto(id_usuario)

        for projeto in projetos:
            id = str(projeto[2])
            if len(id) > 0:
                ids_usuario = id.replace("[", "").replace("]", "").split(",")
                for i in range(len(ids_usuario)):
                    ids_usuario[i] = ids_usuario[i].strip()
                
                if(str(id_usuario) in ids_usuario):
                    projetos_usuario.append(projeto)
        
        if(len(projetos_usuario) > 0):
            for projeto in projetos_usuario:
                print(f"\n\033[1mID Projeto\033[0m: {str(projeto[0])} - \033[1mNome projeto\033[0m: {str(projeto[3])} - \033[1mCPF Gerente do projeto\033[0m: {str(projeto[1])}")
        else:
            print("Nenhum projeto encontrado!")

        time.sleep(5)

        opc_menu = None
        while(opc_menu != 0):
            menu = """
                                    Sistema de Gestão de Projetos
            
            1 - Enviar mensagem                                       2 - Voltar ao menu inicial                                                    
            """
            
            print(menu)
            opc_menu = input("Selecione uma opção: ")
            if(opc_menu == '1'):
                cpf_gerente = input("Informe o CPF do gerente responsável pelo projeto: ")
                nome_gerente = db_service.consulta_nome_usuario(cpf_gerente)

                if (nome_gerente):
                    print(f"Chat com Gerente {nome_gerente.title()}")
                    input("Digite sua mensagem: ")
                    print("Enviando mensagem...")
                    time.sleep(3)
                    print("Mensagem enviada!")
                    time.sleep(2)
                else:
                    print("\n\033[1mCPF Inválido!\n\033[0m")
                    opc_menu = None
            elif(opc_menu == '2'):
                break
                return None
            else:
                print("Digite uma opção válida!")


class Gerente(Usuario):
    def criar_projeto():
        id_usuario = []
        list_ids = []
        verifica = False
        opc_menu = None

        while(len(id_usuario) <= 0 or not verifica):
            menu = """
                                Sistema de Gestão de Projetos                    
            """
            print(menu)
            cpf_gerente = input("Digite o seu CPF: ")
            verifica = db_service.verifica_gerente(cpf_gerente)
            
            if(not verifica):    
                menu = """
                                            Sistema de Gestão de Projetos
            
                1 - Voltar ao menu inicial                                   2 - Tentar novamente                                                   
                """

                print(menu)
                opc_menu = input("Selecione uma opção: ")
                while (opc_menu != 0):
                    print("Selecione uma opção: ")
                    if opc_menu == '1':
                        return None
                    elif opc_menu == '2':
                        break
                    else:
                        print("\n\033[1mDigite uma opção válida!\n\033[0m")
            else:
                qtd_funcionarios = input("Digite a quantidade de funcionários que atuaram no projeto: ")

                i = 0
                while (i != int(qtd_funcionarios)):
                    cpf_usuario = input("Digite o CPF do usuário atuará no projeto: ")
                    id_usuario = db_service.consulta_id(cpf_usuario)

                    if(len(id_usuario) <= 0):
                        print("\n\033[1mUsuário Inválido!\n\033[0m")
                        menu = """
                                                Sistema de Gestão de Projetos
                
                        1 - Voltar ao menu inicial                                   2 - Tentar novamente                     
                        """

                        opc_menu = None
                        while(opc_menu != 1): 
                            print(menu)
                            opc_menu = input("Selecione uma opção: ")
                            if(opc_menu == '1'):
                                return None
                            elif(opc_menu == '2'):
                                break
                            else:
                                print("Digite uma opção válida!")
                    else:
                        i+=1
                        id_usuario = str(id_usuario[0][0])
                        if(id_usuario in list_ids):
                            print("\nEsse usuário já foi adicionado!\n")
                        else:
                            list_ids.append(id_usuario)
                
                id_usuarios = ""
                for id in list_ids:
                    id_usuarios = id_usuarios + f"{id}, "

                id_usuarios = f"[{id_usuarios}]"
                        
                nome_projeto = input("Digite o nome do projeto: ")
                finalidade = input("Digite a finalidade do projeto: ")
                descricao = input("Insira a descrição do projeto: ")
                data_criacao = datetime.now().strftime("%d/%m/%Y")
                orcamento = float(input("Digite o orçamento disponibilizado para o projeto: "))

                db_service.cria_projeto(cpf_gerente, id_usuarios, nome_projeto, qtd_funcionarios, finalidade, descricao, data_criacao, orcamento)
                print("Criando projeto...")
                time.sleep(3)
                print("Projeto criado com sucesso!")
                time.sleep(2)

                return None
    

    def progresso_projeto():
        projetos = []
        while(len(projetos) <= 0):
            menu = """
                                Sistema de Gestão de Projetos                    
            """
            print(menu)
            cpf_gerente = input("Digite o seu cpf: ")
            verifica = db_service.verifica_gerente(cpf_gerente)
            if(not verifica):
                menu = """
                                            Sistema de Gestão de Projetos
            
                1 - Voltar ao menu inicial                                   2 - Tentar novamente                                                   
                """

                print(menu)
                opc_menu = input("Selecione uma opção: ")
                while (opc_menu != 0):
                    print("Selecione uma opção: ")
                    if opc_menu == '1':
                        return None
                    elif opc_menu == '2':
                        break
                    else:
                        print("\n\033[1mDigite uma opção válida!\n\033[0m")
            else:
                projetos = db_service.consulta_projeto_gerente(cpf_gerente)

                if(len(projetos) > 0):
                    for projeto in projetos:
                        print(f"\n\033[1mID Projeto\033[0m: {str(projeto[0])} - \033[1mNome projeto\033[0m: {str(projeto[3])} - "\
                              + f"\033[1mStatus\033[0m: {str(projeto[7])} - \033[1mCPF Gerente do projeto\033[0m: {str(projeto[1])} - "\
                                 + f"\033[1mID Usuário\033[0m: {str(projeto[2])} - \033[1mFuncionários\033[0m: {str(projeto[4])}")
                        
                    time.sleep(5)
                else:
                    print("Nenhum projeto encontrado!")
                    
                    time.sleep(5)
                    
                    opc_menu = None
                    while(opc_menu != 1):
                        menu = """
                                        Sistema de Gestão de Projetos
                        
            1 - Voltar ao menu inicial                                                    
                        """
                        
                        print(menu)
                        opc_menu = input("Selecione uma opção: ")
                        if(opc_menu == '1'):
                            return None
                        else:
                            print("Digite uma opção válida!")


    def atribui_tarefa():
        verifica = False
        while(not verifica):
            menu = """
                                    Sistema de Gestão de Projetos                    
                """
            print(menu)
            id_projeto = input("Digite o seu ID do projeto: ")
            verifica = db_service.verifica_id_projeto(id_projeto)

            if(not verifica):
                menu = """
                                            Sistema de Gestão de Projetos
            
                1 - Voltar ao menu inicial                                   2 - Tentar novamente                                                   
                """

                print(menu)
                opc_menu = input("Selecione uma opção: ")
                while (opc_menu != 0):
                    print("Selecione uma opção: ")
                    if opc_menu == '1':
                        return None
                    elif opc_menu == '2':
                        break
                    else:
                        print("\n\033[1mDigite uma opção válida!\n\033[0m")
            else:
                descricao = input("Insira a descrição da tarefa: ")
                db_service.cria_tarefa(id_projeto, descricao)

                print("\nAtribuindo tarefa...")
                time.sleep(2)
                print("Tarefa criada com sucesso!")
                time.sleep(2)
                return None

    def dashboard_projeto():
        pass
    def gerenciamento_Prazo():
        pass
    def gerar_relatorio():
        pass
    def consultar_orcamento():
        pass
    def historico_atividade():
        pass


class Gerente_Master(Gerente):
    def configuracao_Sistema():
        pass