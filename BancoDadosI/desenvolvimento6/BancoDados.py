import sqlite3

# CRUD incompleto, apenas criação do banco de dados, 
# criação da tabela, inserção e visualização de dados.

conexao = sqlite3.connect("BancoDadosI/Desenvolvimento6/ESCOLA.db")

conexao.execute('''CREATE TABLE IF NOT EXISTS ALUNO
                ( 
                    aluno_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(80) NOT NULL,
                    email VARCHAR(80),
                    endereço VARCHAR(80)
                
                );''')

def cadastrarAluno(nome, email, endereco):
    conexao.execute("INSERT INTO ALUNO(nome, email, endereço) VALUES (?, ?, ?);", (nome, email, endereco))
    conexao.commit()
    print("Aluno cadastrado")

def listarAlunos():
    listaAlunos = conexao.execute("SELECT * FROM ALUNO;")
    for aluno in listaAlunos:
        print(aluno)


cadastrarAluno("João Carlos", "Jcarlos@gmail.com", "Rua 13 de maio")
cadastrarAluno("João Vitor", "Jvitor@gmail.com", "Rua da Saudade")
cadastrarAluno("Paulo André", "Pandr@gmail.com", "Rua do Sol")

listarAlunos()