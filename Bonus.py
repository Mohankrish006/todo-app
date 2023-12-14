import PySimpleGUI as sg

label1 = sg.Text("Select files to Compress: ")
input1 = sg.Input()
Choose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
Choose_button2 = sg.FolderBrowse("Choose")

Compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
    layout = [[label1, input1, Choose_button1],
        [label2, input2, Choose_button2], [Compress_button]])

window.read()
window.close()
