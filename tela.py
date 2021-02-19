import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Valor em Reais (R$)',size=(16,0)),sg.Input(size=(20,0))],
            [sg.Text('Valor em Dólares (U$)',size=(16,0)),sg.Input(size=(20,0))],
            [sg.Button('Converter')]
        ]
        #Janela
        janela = sg.Window('Conversor de moedas').layout(layout)
        #Extração de dados da tela
        self.Button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

tela = TelaPython()
tela.iniciar()