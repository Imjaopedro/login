import PySimpleGUI as sg
import mysql.connector


def criar_tabela_usuarios():
    comando = mysql.connector.connect(host='localhost', user='root', password='Senha00@', database='teste')
    cursor = comando.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            senha VARCHAR(100) NOT NULL
        )
    """)
    comando.commit()
    comando.close()


def cadastrar_usuario(nome, senha):
    comando = mysql.connector.connect(host='localhost', user='root', password='Senha00@', database='teste')
    cursor = comando.cursor()
    cursor.execute(f'INSERT INTO usuarios (nome, senha) VALUES ("{nome}" ,"{senha}")')
    comando.commit()
    comando.close()


def verificar_login(nome, senha):
    comando = mysql.connector.connect(host='localhost', user='root', password='Senha00@', database='teste')
    cursor = comando.cursor()
    cursor.execute(f'SELECT * FROM usuarios WHERE nome = "{nome}"" AND senha = "{senha}"')
    result = cursor.fetchone()
    comando.close()
    return result is not None


layout = [
    [sg.Text('Nome de usuário:'), sg.Input(key='-USERNAME-')],
    [sg.Text('Senha:'), sg.Input(key='-PASSWORD-', password_char='*')],
    [sg.Button('Cadastrar'), sg.Button('Login')]
]


criar_tabela_usuarios()

window = sg.Window('Sistema de Login', layout)


while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == 'Cadastrar':
        nome = values['-USERNAME-']
        senha = values['-PASSWORD-']
        cadastrar_usuario(nome, senha)
        sg.popup('Usuário cadastrado com sucesso!')
    
    if event == 'Login':
        nome = values['-USERNAME-']
        senha = values['-PASSWORD-']
        if verificar_login(nome, senha):
            sg.popup('Login bem-sucedido!')
        else:
            sg.popup('Usuário ou senha inválidos!')
        

window.close()

