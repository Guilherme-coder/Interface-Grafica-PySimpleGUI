import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key="nome")],
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key="idade")],
            [sg.Text('Sexo', size=(5,0)), sg.Input(size=(2,0), key="sexo")],
            [sg.Button('Enviar dados', size=(18,0))]

        ]
        #Janela
        window = sg.Window('Dados do usuário').layout(layout)
        #Extração dos dados na tela
        self.button, self.values = window.Read()

    def Iniciar(self):
        nome = self.values['nome']
        idade = self.values['idade']
        sexo = self.values['sexo']

        if(sexo == "M" or sexo == "m"):
            sexo = "masculino"
        elif(sexo == "F" or sexo == "f"):
            sexo = "feminino"
        else:
            sexo = "POR FAVOR, INSIRA UM SEXO VÁLIDO"


        print(f"Nome: {nome}\nIdade: {idade}\nSexo: {sexo}")

screen = TelaPython()
screen.Iniciar()
