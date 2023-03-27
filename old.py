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

class Mouse_Grid:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.screenWidth, self.screenHeight = pyautogui.size()
        self.cell_size_width = self.screenWidth // self.grid_size
        self.cell_size_height = self.screenHeight // self.grid_size
        self.img = Image.new('RGBA', (self.cell_size_width * self.grid_size, self.cell_size_height * self.grid_size), (255, 255, 255, 255))
        self.draw = ImageDraw.Draw(self.img)
        self.location_x, self.location_y = 0, 0
        self.new_grid_x, self.new_grid_y = self.cell_size_width, self.cell_size_height
        self.old_x, self.old_y = 0, 0
        self.draw_grid()
        self.root = None
        
    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x = i * self.new_grid_x + self.location_x
                y = j * self.new_grid_y + self.location_y
                self.draw.rectangle((x, y, x + self.new_grid_x, y + self.new_grid_y), outline=(0, 0, 0, 255))
                self.draw.text((x, y), str(j * self.grid_size + i + 1), fill=(0, 0, 0, 255), font=ImageFont.truetype("arial.ttf", 40))
        # return 0,0
    def draw_box(self):
        self.new_grid_x = self.new_grid_x // 3
        self.new_grid_y = self.new_grid_y // 3
        print(self.new_grid_x, self.new_grid_y)
        for i in range(grid_size):
            for j in range(grid_size):
                x = i * self.new_grid_x + self.location_x
                y = j * self.new_grid_y + self.location_y
                # x = i * self.new_grid_x
                # y = j * self.new_grid_y
                self.draw.rectangle((x, y, x + self.new_grid_x, y + self.new_grid_y), outline=(0, 0, 0, 255))
                # self.draw.text((x, y), str(j * grid_size + i + 1), fill=(0, 0, 0, 255), font= ImageFont.truetype("arial.ttf", 10))
        return self.new_grid_x, self.new_grid_y
    
    def update_location(self, x, y):
        self.location_x = self.location_x + x * self.new_grid_x
        self.location_y = self.location_y + y * self.new_grid_y

    def compute_new_grid(self):
        self.new_grid_x = self.new_grid_x // 3
        self.new_grid_y = self.new_grid_y // 3
    
    def display_grid(self):
        self.root = tk.Tk()
        self.root.title("Mouse_Grid_draft")
        photo = ImageTk.PhotoImage(self.img)
        label = tk.Label(self.root, image=photo)
        label.place(x=0, y=0)
        self.root.geometry("%dx%d+%d+%d" % (self.img.size[0], self.img.size[1], 0, 0))
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)
        close_button = tk.Button(self.root, text="Close", command=self.root.destroy)
        close_button.pack()
        self.root.deiconify()
        self.root.update()
        # self.root.mainloop()


# class MyGUI:
#     def __init__(self,mouse_grid):
#         self.root = tk.Tk()
#         self.root.title("Mouse_Grid_draft")
#         self.photo = ImageTk.PhotoImage(mouse_grid.img)
#         self.label = tk.Label(self.root, image=self.photo)
#         self.label.place(x=0, y=0)
#         self.root.geometry("%dx%d+%d+%d" % (mouse_grid.img.size[0], mouse_grid.img.size[1], 0, 0))
#         self.root.attributes('-fullscreen', True)
#         self.root.attributes('-alpha', 0.3)
#         self.close_button = tk.Button(self.root, text="Close", command=self.root.destroy)
#         self.close_button.pack()
#         self.root.deiconify()
#         self.root.update()

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
        # cell_number = int(input("Enter the cell number: "))

        cell_number = speech_number()

        if (cell_number < 1 or cell_number > grid_size * grid_size):
            print("Invalid cell number")
            break

        x = (cell_number - 1) % grid_size
        y = (cell_number - 1) // grid_size
        print("x: ", x, "y: ", y)

        mouse_grid.update_location(x, y)
        # print("location_x: ", mouse_grid.location_x, "location_y: ", mouse_grid.location_y)
        target_x = x * mouse_grid.new_grid_x + mouse_grid.new_grid_x // 2 + mouse_grid.old_x
        target_y = y * mouse_grid.new_grid_y + mouse_grid.new_grid_y // 2 + mouse_grid.old_y
        pyautogui.moveTo(target_x, target_y, duration=0.25)
        # check_onclick = int(input("Enter 1 to click: "))
        
        check_onclick = _oneclick()
        if (check_onclick == 1):
            root.destroy()
            pyautogui.click(target_x, target_y, clicks=1, interval=0.0, button='left')
            text = fill_text()
            pyautogui.typewrite(text)
            # pyautogui.click()
            mouse_grid = Mouse_Grid(grid_size)
            check_onclick = 1

        
        if check_onclick == 0:
            # print("target_x: ", target_x, "target_y: ", target_y)
            new_x,new_y = mouse_grid.draw_box()
            # mouse_grid.compute_new_grid()
            # print("new_grid_x: ", mouse_grid.new_grid_x, "new_grid_y: ", mouse_grid.new_grid_y)
            mouse_grid.old_x = mouse_grid.location_x
            mouse_grid.old_y = mouse_grid.location_y
            root.destroy()
            root.mainloop()
        