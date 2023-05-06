import os
import subprocess as sp

paths = {
    'google': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    'photoshop': "E:\\Photoshop\\Adobe Photoshop 2022\\Photoshop.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_google():
    os.startfile(paths['google'])


def open_photoshop():
    os.startfile(paths['photoshop'])

def open_calculator():
    os.startfile(paths['calculator'])