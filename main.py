import pyautogui
from PIL import Image,ImageDraw,ImageTk,ImageFont
import tkinter as tk
from pynput import keyboard
from pynput.keyboard import Key,Controller
from speech_to_text import get_audio, speak, get_text, get_number, play_music, read_news, get_time, open_application, current_weather, read_news1,weather,get_time1
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
import Type_write_vietnamese
import re

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
            root.destroy()
            return 0

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
    
    elif ("chọn chuột trái" in text and "enter" not in text) or "chuột trái" in text:
        root.destroy()
        pyautogui.click(mouse_grid.mouse_location_x, mouse_grid.mouse_location_y, clicks=1, interval=0.0, button='left')
        return 0

    elif ("chọn chuột phải" in text and "enter" not in text) or "chuột phải" in text:
        root.destroy()
        pyautogui.click(mouse_grid.mouse_location_x, mouse_grid.mouse_location_y, clicks=1, interval=0.0, button='right')
        return 0
    
    elif "click chuột" in text:
        root.destroy()
        pyautogui.click(mouse_grid.mouse_location_x, mouse_grid.mouse_location_y, clicks=2, interval=0.0, button='left')
        return 0
    
    elif "cuộn lên" in text:
        root.destroy()
        number = re.findall(r'\d+',text)
        if len(number):
            pyautogui.scroll(int(number[0]))
        else:
            pyautogui.scroll(500)
        return 0
    
    elif "cuộn xuống" in text:
        root.destroy()
        number = re.findall(r'\d+',text)
        if len(number):
            pyautogui.scroll(-int(number[0]))
        else:
            pyautogui.scroll(-500)
        return 0
    
    elif "nhập" in text and "xong" not in text:
        root.destroy()
        content = text.split("nhập",1)[1]
        Type_write_vietnamese.type(content)
        return 0
    
    # alt + left
    elif "quay lại" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.alt)
        keyb.press(Key.left)
        keyb.release(Key.left)
        keyb.release(Key.alt)
        return 0

    # alt + right
    elif "chuyển tiếp" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.alt)
        keyb.press(Key.right)
        keyb.release(Key.right)
        keyb.release(Key.alt)
        return 0
    
    # tab
    elif "chuyển ô nhập" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.tab)
        keyb.release(Key.tab)
        return 0
    # ctrl + r
    elif "tải lại" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.ctrl)
        keyb.press('r')
        keyb.release('r')
        keyb.release(Key.ctrl)
        return 0
    
    # ctrl + w
    elif "đóng trang" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.ctrl)
        keyb.press('w')
        keyb.release('w')
        keyb.release(Key.ctrl)
        return 0
    
    # ctrl + t
    elif "mở trang mới" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.ctrl)
        keyb.press('t')
        keyb.release('t')
        keyb.release(Key.ctrl)
        return 0
    # ctrl + shift + t
    elif "mở lại trang" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.ctrl)
        keyb.press(Key.shift)
        keyb.press('t')
        keyb.release('t')
        keyb.release(Key.shift)
        keyb.release(Key.ctrl)
        return 0
    # get weather
    elif "thời tiết" in text:
        root.destroy()
        weather()
        return 0
    # play music
    elif "nghe nhạc" in text:
        root.destroy()
        play_music()
        return 0
    # read news
    elif "đọc tin tức" in text:
        root.destroy()
        read_news1()
        return 0
    # get time 
    elif "thời gian" in text or "mấy giờ" in text or "giờ" in text:
        root.destroy()
        get_time1()
        return 0
    # open application
    elif "mở" in text:
        root.destroy()
        open_application(text)
        return 0
    # press enter
    elif "nhập xong" in text or "nhấn enter" in text or "chọn enter" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.enter)
        keyb.release(Key.enter)
        return 0
    
    elif "vẽ lại" in text:
        return -1
    
    elif "thoát" in text:
        root.destroy()
        raise SystemExit(0)
    
    return -2

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
        root.attributes("-topmost", True)
        close_button = tk.Button(root, text="Close", command=root.destroy)
        close_button.pack()
        root.deiconify()
        root.update()
        # root.after(0, get_text)
        # root.update_idletasks()
        # root.mainloop()

        text = get_text()
        check_redraw = handle_text(text,mouse_grid,root,grid_size)

        if check_redraw == -1:
            root.destroy()
            mouse_grid = Mouse_Grid(grid_size)

        if check_redraw == -2:
            print("Bot: Tôi không hiểu ý bạn")
            root.destroy()
            # break

        