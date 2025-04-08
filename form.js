import PySimpleGUI as sg

sg.theme('DarkTeal9')

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name', size=(15,1)), sg.InputText],
    [sg.Submit(), sg.Exit]
]
