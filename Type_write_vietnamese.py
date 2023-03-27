import pyautogui
import pyperclip
import platform
# in windows, use ctrl + v
# import pyautogui
# import pyperclip

# pyperclip.copy("Vũ Minh Anh")
# pyautogui.hotkey("ctrl", "v")
def type(text: str):    
    pyperclip.copy(text)
    if platform.system() == "Darwin":
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.hotkey("ctrl", "v")


type("Vũ Minh Anh")

