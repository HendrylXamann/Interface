from PySimpleGUI import PySimpleGUI as sg #Importando a biblioteca e dando um "apelido"

#Início da função 1
def interface():
    sg.theme('Reddit') #Utilizando um tema padrão 
    layout = [ #Váriavel com uma lista que cria todos os inputs da área de login, inclusive o botão
        [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
        [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
        [sg.Text('Token'), sg.Input(key='token', size=(20, 1))],
        [sg.Button('Entrar')]
    ]
    return layout #O comando do que quero retornar dessa função, no caso tudo que compõe a várivel layout

#Início da função 2
def login1(janela): 
    event, values = janela.read() #lê os eventos e valores da janela 
    return event, values

#Até aqui foi a criação da interface de login, daqui em diante é a evocação dessas funções para que ela surja:
layout = interface()
janela = sg.Window('Tela de Login', layout)
event, values = login1(janela)

#Essas variáveis abaixo armazenam os valores inseridos pelo usuario, caso fosse utilizar essa interface em outro código
#poderia utilizar esses valores
usuario = values['usuario']
senha = values['senha']
token = values['token']



