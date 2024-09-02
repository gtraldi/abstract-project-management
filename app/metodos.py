import app.utils.db_methods as db_service
import classes as cl
import app.metodos as M

def login_Acesso():
    menu = """
                             Sistema de Gestão de Projetos
                             
    1 - Login
    2 - Cadastro de Usuário
    """

    opc_menu = 0
    sucesso = False
    while (not sucesso):
        while(opc_menu not in [1,2]):
            print(menu)
            opc_menu = int(input("Digite uma opção: "))
            if(opc_menu == 1):
                login, senha = cl.Usuario.login()
                sucesso = M.db_service.verifica_Login(login, senha)
            elif(opc_menu == 2):
                login, senha = cl.Usuario.cadastro()
            else:
                print("\n\033[1mDigite uma opção válida!\033[0m")
        
        opc_menu = 0

    return login


def cadastro(login):
    menu = """
                             Sistema de Gestão de Projetos
        Deseja realizar um novo cadastro de Gerente? (Ex.: Sim/Nao)
    """
    print(menu)
    opc = input()


def menu(login):
    tipo_usuario = str(db_service.verifica_tipo_usuario(login))

    if(tipo_usuario == "U"):
        menu_Principal = """
                                    Sistema de Gestão de Projetos
        
        1 - Progresso dos projetos                                 3 - Finalizar Programa
        2 - Comunicação                                            
        """
    
        opc_menu = None
        while(opc_menu != 0):
            print(menu_Principal)
            opc_menu = int(input("Digite uma opção: "))

            if(opc_menu == 1):
                opc_menu = cl.Usuario.progresso_projeto()
            elif(opc_menu == 2):
                opc_menu = cl.Usuario.comunicacao()
            elif(opc_menu == 3):
                print("Finalizando o programa!")
                opc_menu = 0
            else:
                print("Opção Inválida! Digite novamente!")   

    elif(tipo_usuario == "G"):
        menu_Principal = """
                                        Sistema de Gestão de Projetos
            
            1 - Criação de Projetos                                    6 - Geração de Relatórios
            2 - Atribuição de tarefas                                  7 - Comunicação
            3 - Progresso dos projetos                                 8 - Orçamentos
            4 - Dashboard dos Projetos                                 9 - Histórico Atividades
            5 - Gerenciamento de Prazos                                10 - Finalizar Programa                                  
        """

        opc_menu = None
        while(opc_menu != 0):
            print(menu_Principal)
            opc_menu =int(input("Digite uma opção: "))
            if(opc_menu == 1):
                opc_menu = cl.Gerente.criar_projeto()
            elif(opc_menu == 2):
                opc_menu = cl.Gerente.atribui_tarefa()
            elif(opc_menu == 3):
                opc_menu = cl.Gerente.progresso_projeto()
            elif(opc_menu == 4):
                opc_menu = cl.Gerente.dashboard_projeto()
            elif(opc_menu == 5):
                opc_menu = cl.Gerente.gerenciamento_Prazo()
            elif(opc_menu == 6):
                opc_menu = cl.Gerente.gerar_relatorio()
            elif(opc_menu == 7):
                opc_menu = cl.Usuario.comunicacao()
            elif(opc_menu == 8):
                opc_menu = cl.Gerente.consultar_orcamento()
            elif(opc_menu == 9):
                opc_menu = cl.Gerente.historico_atividade()
            elif(opc_menu == 10):
                print("Finalizando o programa!")
                opc_menu = 0
            else:
                print("Opção Incorreta! Digite novamente!")
    
    elif(tipo_usuario == "GM"):
        menu_Principal = """
                                        Sistema de Gestão de Projetos
            
            1 - Criação de Projetos                                    7 - Comunicação
            2 - Atribuição de tarefas                                  8 - Orçamentos
            3 - Progresso dos projetos                                 9 - Histórico Atividades
            4 - Dashboard dos Projetos                                 10 - Configurações do Sistema
            5 - Gerenciamento de Prazos                                11 - Finalizar Programa 
            6 - Geração de Relatórios                             
        """

        opc_menu = None
        while(opc_menu != 0):
            print(menu_Principal)
            opc_menu =int(input("Digite uma opção: "))
            if(opc_menu == 1):
                opc_menu = cl.Gerente.criar_projeto()
            elif(opc_menu == 2):
                cl.Gerente.atribui_tarefa()
            elif(opc_menu == 3):
                opc_menu = cl.Usuario.progresso_projeto()
            elif(opc_menu == 4):
                cl.Gerente.dashboard_projeto()
            elif(opc_menu == 5):
                cl.Gerente.gerenciamento_Prazo()
            elif(opc_menu == 6):
                cl.Gerente.gerar_relatorio()
            elif(opc_menu == 7):
                cl.Usuario.comunicacao()
            elif(opc_menu == 8):
                cl.Gerente.consultar_orcamento()
            elif(opc_menu == 9):
                cl.Gerente.historico_atividade()
            elif(opc_menu == 10):
                cl.Gerente_Master.configuracao_Sistema()
            elif(opc_menu == 11):
                print("Finalizando o programa!")
                opc_menu = 0
            else:
                print("Opção Incorreta! Digite novamente!")

def main():
    db_service.criaBanco()
    print("As tabelas foram criadas com sucesso.")