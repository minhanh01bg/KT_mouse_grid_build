import pyautogui
from PIL import Image,ImageDraw,ImageTk,ImageFont
import tkinter as tk
from pynput import keyboard
from speech_to_text import get_audio, speak, get_text, get_number
import os
import playsound
import speech_recognition as sr
import time 
import sys 
import ctypes
import wikipedia
import datetime
import json
import re 
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from mouse_grid_class import Mouse_Grid


def speech_number():
    print("Bot: Hãy cho tôi số của ô bạn muốn chọn")
    text = get_text()
    print(text)
    number = get_number(text)
    if number == -1:
        print("Bot: Không có số này")
        return speech_number()
    return number

def _oneclick():
    print("Bot: Bạn có muốn chọn ô này không?")
    text = get_text()
    if "có" in text:
        return True
    elif "không" in text:
        return False
    else:
        print("Bot: Tôi không hiểu ý bạn")
        return _oneclick()
    
def fill_text():
    print("Bot: Hãy cho tôi nội dung bạn muốn nhập vào ô")
    text = get_text()
    print(text)
    return text


def handle_text(text,mouse_grid,root,grid_size):
    print(text)
    if "di chuyển" in text:
        cell_number = get_number(text)
        if (cell_number < 1 or cell_number > grid_size * grid_size):
            print("Invalid cell number")
            return

        x = (cell_number - 1) % grid_size
        y = (cell_number - 1) // grid_size
        print("x: ", x, "y: ", y)

        mouse_grid.update_location(x, y)
        # print("location_x: ", mouse_grid.location_x, "location_y: ", mouse_grid.location_y)
        target_x = x * mouse_grid.new_grid_x + mouse_grid.new_grid_x // 2 + mouse_grid.old_x
        target_y = y * mouse_grid.new_grid_y + mouse_grid.new_grid_y // 2 + mouse_grid.old_y
        pyautogui.moveTo(target_x, target_y, duration=0.25)
        mouse_grid.update_mouse_location(target_x, target_y)
        mouse_grid.draw_box()
        mouse_grid.old_x = mouse_grid.location_x
        mouse_grid.old_y = mouse_grid.location_y
        root.destroy()
        root.mainloop()
        return 0
    elif "chọn chuột trái" in text:
        root.destroy()
        pyautogui.click(mouse_grid.mouse_location_x, mouse_grid.mouse_location_y, clicks=1, interval=0.0, button='left')


    elif "chọn" in text:
        pass
    
    elif "vẽ lại" in text:
        return -1

if __name__ == "__main__":
    grid_size = 3
    mouse_grid = Mouse_Grid(grid_size)
    # mouse_grid.draw_grid()
    while True:
        # mouse_grid.display_grid()
        root = tk.Tk()
        root.title("Mouse_Grid_draft")
        photo = ImageTk.PhotoImage(mouse_grid.img)
        label = tk.Label(root, image=photo)
        label.place(x=0, y=0)
        root.geometry("%dx%d+%d+%d" % (mouse_grid.img.size[0], mouse_grid.img.size[1], 0, 0))
        root.attributes('-fullscreen', True)
        root.attributes('-alpha', 0.2)
        close_button = tk.Button(root, text="Close", command=root.destroy)
        close_button.pack()
        # import time
        # time.sleep(10)
        root.deiconify()
        root.update()


        text = get_text()
        check_redraw = handle_text(text,mouse_grid,root,grid_size)

        if check_redraw == -1:
            root.destroy()
            mouse_grid = Mouse_Grid(grid_size)
        
        # check_onclick = _oneclick()
        # if (check_onclick == 1):
        #     root.destroy()
        #     pyautogui.click(target_x, target_y, clicks=1, interval=0.0, button='left')
        #     text = fill_text()
        #     pyautogui.typewrite(text)
        #     # pyautogui.click()
        #     mouse_grid = Mouse_Grid(grid_size)
        #     check_onclick = 1

        
        # if check_onclick == 0:
        #     # print("target_x: ", target_x, "target_y: ", target_y)
        #     new_x,new_y = mouse_grid.draw_box()
        #     # mouse_grid.compute_new_grid()
        #     # print("new_grid_x: ", mouse_grid.new_grid_x, "new_grid_y: ", mouse_grid.new_grid_y)
        #     mouse_grid.old_x = mouse_grid.location_x
        #     mouse_grid.old_y = mouse_grid.location_y
        #     root.destroy()
        #     root.mainloop()
        