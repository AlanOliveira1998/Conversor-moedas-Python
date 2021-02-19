import PySimpleGUI as sg 
class TelaPython:
    def __init__(self)
    #Layout
    layout = [
        [sg.Text('Valor em reais'),sg.Input()],
        [sg.Text('Valor em dolara'),sg.Input()],
        [sg.Button('Converter')]
    ]
    #janela
    janela = sg.Window("Dados do Usuário").layout(layout)
    #Extrair dados da tela
    self.Button, self.Values = janela.read
    def iniciar(self):
        print(self.values)

tela = TelaPython()
tela.iniciar()