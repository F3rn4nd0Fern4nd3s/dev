from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='Usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='Senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de login', layout)
# Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuario'] == 'fernando' and valores['Senha'] == '123456':
            print('Bem-vindo Fernandinho !:D')
            break