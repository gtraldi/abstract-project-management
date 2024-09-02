import sqlite3

def criaBanco():
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    tabela1 = """CREATE TABLE IF NOT EXISTS tab_usuario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR (20) NOT NULL,
                sobrenome VARCHAR (60),
                cpf VARCHAR(15) NOT NULL,
                senha VARCHAR(10) NOT NULL,
                email VARCHAR(25),
                tipo_usuario VARCHAR(80) NOT NULL,
                senha_master VARCHAR(80))"""
                
    tabela2 = """CREATE TABLE IF NOT EXISTS tab_projeto(
                id_projeto INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf_gerente INTEGER (5) NOT NULL,
                id_usuario INTEGER (5) NOT NULL,
                nome_projeto VARCHAR(100) NOT NULL,
                quantidade_funcionarios VARCHAR(10) NOT NULL,
                finalidade VARCHAR(25),
                descricao VARCHAR(100),
                status_atualizado VARCHAR(80) NOT NULL,
                data_criacao VARCHAR(10),
                orçamento FLOAT (50),
                FOREIGN KEY(id_usuario) REFERENCES tab_usuario(id)
                FOREIGN KEY(cpf_gerente) REFERENCES tab_usuario(cpf))"""

    tabela3 = """CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                projeto_id INTEGER,
                funcionario_id INTEGER,
                prazo VARCHAR(25),
                FOREIGN KEY (projeto_id) REFERENCES Projeto(id),
                FOREIGN KEY (funcionario_id) REFERENCES tab_usuario(id))"""
    
    tabela4 = """CREATE TABLE IF NOT EXISTS historico (
                tipo_atividade VARCHAR(64) NOT NULL,
                projeto_id INTEGER,
                funcionario_id INTEGER,
                data VARCHAR(25),
                FOREIGN KEY (projeto_id) REFERENCES Projeto(id),
                FOREIGN KEY (funcionario_id) REFERENCES tab_usuario(id))"""

    cursor.execute(tabela1)
    cursor.execute(tabela2)
    cursor.execute(tabela3)
    conexao.commit()
    conexao.close()


def verifica_Login(login, senha):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    cont = 0
    sql = """SELECT * FROM tab_usuario WHERE cpf = ('""" + login + """');"""

    sucesso = False
    try:
        cursor.execute(sql)
        if(cursor.fetchall() != []):
            conexao.commit()
            conexao.close()
            if(verifica_senha(senha)):
                print("\n\033[1mSeja Bem Vindo! Acesso Conectado!\033[0m")
                return True
            else:
                print("\n\033[1mSenha Incorreta!\033[0m")
                return False
        else:
            print("\n\033[1mUsuário não cadastrado!\033[0m")
            return False
        
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()
        

def verifica_senha(senha):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = """SELECT * FROM tab_usuario WHERE senha = ('""" + senha + """');"""
    try:
        cursor.execute(sql)
        if(cursor.fetchall()!= []):
            conexao.commit()
            conexao.close()
            return True
        else:
            return False
        
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def verifica_gerente(cpf_gerente):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""SELECT * FROM tab_usuario WHERE cpf = ({cpf_gerente});"""
    try:
        cursor.execute(sql)
        if(cursor.fetchall() != []):
            conexao.commit()
            conexao.close()
            return True
        else:
            print("\n\033[1mCPF inválido! Tente novamente\n\033[0m")
            return False
        
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def verifica_tipo_usuario(login):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""SELECT tipo_usuario FROM tab_usuario WHERE cpf = ({login});"""
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        if(row != 'NULL' or row != 0):
            conexao.commit()
            conexao.close()
            return row[0]
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def verifica_GerenteMaster(login, senha_master):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""SELECT * FROM tab_usuario WHERE cpf = ('{login}') and tipo_usuario = ('GM') and senha_master = ('{senha_master}');"""
    try:
        cursor.execute(sql)
        if(cursor.fetchall()):
            conexao.commit()
            conexao.close()
            return True
        else:
            return False
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def verifica_id_projeto(id_projeto):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""SELECT * FROM tab_projeto WHERE id_projeto = ({id_projeto});"""
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        if(row != 'NULL' or row != 0):
            conexao.commit()
            conexao.close()
            return row[0]
        else:
            print("\n\033[1mID inválido! Projeto não encontrado, tente novamente\n\033[0m")
            return None
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def cadastra_usuario(nome, sobrenome, email, login, senha, tipo_usuario, senha_master=None):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""INSERT INTO tab_usuario (nome, sobrenome, email, cpf, senha, tipo_usuario, senha_master)
        VALUES ('{nome}', '{sobrenome}', '{email}', {login}, '{senha}', '{tipo_usuario}', '{senha_master}');"""
    try:
        cursor.execute(sql)
        conexao.commit()
        conexao.close()
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def consulta_id(cpf):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""SELECT id FROM tab_usuario WHERE cpf = ('{cpf}');"""
    try:
        cursor.execute(sql)
        row = cursor.fetchall()
        if(row != 'NULL' or row != 0 or row != []):
            conexao.commit()
            conexao.close()
            return row
        else:
            return []
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def consulta_projeto(id_usuario):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""SELECT * FROM tab_projeto"""
    try:
        cursor.execute(sql)
        row = cursor.fetchall()
        if(row != 'NULL' or row != 0 or row != []):
            conexao.commit()
            conexao.close()
            return row
        else:
            return []
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def consulta_projeto_gerente(cpf_gerente):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""SELECT * FROM tab_projeto WHERE cpf_gerente = {cpf_gerente};"""
    try:
        cursor.execute(sql)
        row = cursor.fetchall()
        if(row != 'NULL' or row != 0 or row != []):
            conexao.commit()
            conexao.close()
            return row
        else:
            return []
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def consulta_nome_usuario(cpf):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""SELECT nome FROM tab_usuario WHERE cpf = ('{cpf}');"""
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        if(row != 'NULL' and row != 0 and row):
            conexao.commit()
            conexao.close()
            return row[0]
        else:
            return None
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def cria_projeto(cpf_gerente, id_usuario, nome_projeto, qtd_funcionarios, finalidade, descricao, data_criacao, orcamento):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()
    sql = f"""INSERT INTO tab_projeto (cpf_gerente, id_usuario, nome_projeto, quantidade_funcionarios, finalidade, descricao,
      status_atualizado, data_criacao, orçamento)
        VALUES ('{cpf_gerente}', '{id_usuario}', '{nome_projeto}', {qtd_funcionarios}, '{finalidade}', '{descricao}', 'A fazer', '{data_criacao}', '{orcamento}');"""
    try:
        cursor.execute(sql)
        conexao.commit()
        conexao.close()
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()


def cria_tarefa(id_projeto, descricao):
    conexao = sqlite3.connect("GestaoProjetos.db")
    cursor = conexao.cursor()

    sql_id_usuario = f"""SELECT id_usuario FROM tab_projeto WHERE id_projeto = ({id_projeto})"""
    cursor.execute(sql_id_usuario)
    id_usuario = cursor.fetchall()[0][0]

    sql = f"""INSERT INTO Tarefas (descricao, projeto_id, funcionario_id)
        VALUES ('{descricao}', {id_projeto}, {id_usuario});"""
    try:
        cursor.execute(sql)
        conexao.commit()
        conexao.close()
    except sqlite3.IntegrityError as e:
        raise Exception("Erro!", e)
        conexao.commit()
        conexao.close()