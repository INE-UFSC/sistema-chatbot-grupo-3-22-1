import PySimpleGUI as sg



container = [[sg.Text(""*15, key='fala_bot', size=(40, 1))],
             [sg.Text("Nome do Bot:"), sg.InputText('', key='codigo')],
             [sg.Button("Selecionar Bot"), sg.Text("", key="feedback_selecao", size=(5, 1))]]

frame1 = [sg.Frame('Teste', layout=[[sg.Text('', key="line_01", size=(20, 5))],
                              [sg.Text('', key="line_02")],
                              [sg.Text('', key="line_03")],
                              [sg.Text('', key="line_04")],
                              [sg.Text('', key="line_05")],
                              [sg.Text('', key="line_06")],
                              [sg.Text('', key="line_07")]])]

layout = [
    [sg.Text('Chatbot Window', size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Frame("Chat History", layout=[[sg.Text("", key="chat_history", size=(30, 30))]])], [sg.Frame("This is another Frame", layout=[[sg.Text("", key="chat_abab", size=(15, 5))]])]]
window = sg.Window('a', layout)

while True:
    event, values = window.read()
