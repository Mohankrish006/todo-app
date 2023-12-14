import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
Input_box = sg.InputText(tooltip="Enter a Todo")
add_button = sg.Button("Add")

window = sg.Window('My todo App', layout=[[label, Input_box,add_button]])
window.read()
print("Hello")
window.close()
