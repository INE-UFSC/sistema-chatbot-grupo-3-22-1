import PySimpleGUI as sg

class BotView():
    def __init__(self, controlador):
        self.__container = []
        self.__window = sg.Window("Chatbot", self.__container, font=("Helvetica", 14))

    def tela_bot(self):
        self.__container = [[sg.Text('Chatbot Window', size=(
                                30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
                            [sg.Frame("Chat History", layout=[[sg.Text("", key="chat_history", size=(30, 30))]])]]
        self.__window = sg.Window("Seleção de Bots", self.__container, font=("Helvetica", 14))
    
    def atualiza_tela(self, resultado):
        self.__window.Element('chat_history').Update(resultado)

    def le_eventos(self):
        return self.__window.read()
    
    def fim(self):
        self.__window.close()