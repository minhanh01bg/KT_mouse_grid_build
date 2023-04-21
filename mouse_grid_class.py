import pyautogui
from PIL import Image,ImageDraw,ImageTk,ImageFont
import tkinter as tk
from speech_to_text import get_audio, speak, get_text, get_number

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
        self.mouse_location_x = 0
        self.mouse_location_y = 0
        
    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x = i * self.new_grid_x + self.location_x
                y = j * self.new_grid_y + self.location_y
                self.draw.rectangle((x, y, x + self.new_grid_x, y + self.new_grid_y), outline=(0, 0, 0, 255),width=1)
                self.draw.text((x, y), str(j * self.grid_size + i + 1), fill=(0, 0, 0, 255), font=ImageFont.truetype("arial.ttf", 40))
        # return 0,0
    def draw_box(self):
        self.new_grid_x = self.new_grid_x // 3
        self.new_grid_y = self.new_grid_y // 3
        print(self.new_grid_x, self.new_grid_y)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x = i * self.new_grid_x + self.location_x
                y = j * self.new_grid_y + self.location_y
                # x = i * self.new_grid_x
                # y = j * self.new_grid_y
                self.draw.rectangle((x, y, x + self.new_grid_x, y + self.new_grid_y), outline=(0, 0, 0, 255))
                # self.draw.text((x, y), str(j * grid_size + i + 1), fill=(0, 0, 0, 255), font= ImageFont.truetype("arial.ttf", 10))
        return self.new_grid_x, self.new_grid_y
    def update_mouse_location(self,target_x,target_y):
        self.mouse_location_x = target_x
        self.mouse_location_y = target_y

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
        self.root.attributes('-alpha', 0.2)
        self.root.attributes("-topmost", True)
        close_button = tk.Button(self.root, text="Close", command=self.root.destroy)
        close_button.pack()
        self.root.deiconify()
        self.root.update()
        # self.root.mainloop()


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

