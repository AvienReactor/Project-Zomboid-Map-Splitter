import PySimpleGUI as sg
import imagecutv2

#--- GUI Definition ---#
button1 = "Split Map"

layout = [
    [sg.Text("Input Image:", tooltip="Set to path of Image"), sg.Input(key="-IN-"), sg.FileBrowse(file_types=(("Image Files","*"),))],
    [sg.Text("Output Folder:"), sg.Input(key="-OUT-"), sg.FolderBrowse()],
    [sg.Text("Type:"), sg.InputCombo(values="Normal Vegitation ZombieSpawn",key="-TYPE-", size=15)],
    [sg.Text("Columns:", tooltip="Number of columns"), sg.Input(key="-COL-",size=5)],
    [sg.Text("Rows:", tooltip="Number of rows"), sg.Input(key="-ROW-",size=5)],
    [sg.Exit(), sg.Button(button1, tooltip="Split into chunks")],
]

window = sg.Window("Project Zomboid Map Splitter", layout, element_justification="right")

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == button1:
        imagecutv2.SplitMap(values["-IN-"], values["-OUT-"], values["-TYPE-"], values["-COL-"], values["-ROW-"])
        sg.popup("Converting complete")
window.close()