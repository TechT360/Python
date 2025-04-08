import PySimpleGUI as sg

sg.theme('DarkTeal9')

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name', size=(15, 1)), sg.InputText()],  # Added parentheses
    [sg.Submit(), sg.Exit()]
]

# Create the window
window = sg.Window('Form Example', layout)

# Event loop
while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    if event == 'Submit':
        sg.popup(f"You entered: {values[0]}")

window.close()
