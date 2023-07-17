import pyautogui
from pydub import AudioSegment
from pydub.playback import play
import os
print(os.getcwd())

def handle_CMD(CMD):
    cmd_splitted = CMD.split("|")
    if cmd_splitted[0] == "k":
        press_key(cmd_splitted[1])
    elif cmd_splitted[0] == "mclick":
        mouse_click(cmd_splitted[1])


def press_key(key):
    pyautogui.press(key)


def mouse_click(button):
    if button == "0":
        pyautogui.leftClick()
    elif button == 1:
        pyautogui.rightClick()

def play_sound(sound):
    FILE_PATH = "./Host_App/Sounds/"
    if sound == "djoin":
        sound_audio = AudioSegment.from_wav(FILE_PATH + "discordJoin.wav")
        play(sound_audio)

#play_sound("djoin")

#* 
# k|{key} -> press_key(key)
# mclick|{0 or 1} -> mouse_click(button) 0 = left, 1 = right*#
