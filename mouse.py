import pyautogui
from PIL import Image, ImageDraw, ImageTk, ImageFont
import tkinter as tk

screenWidth, screenHeight = pyautogui.size()
# kích thước của một ô trong lưới
cell_size_width = screenWidth//3 
cell_size_height = screenHeight//3 
# kích thước của lưới
grid_size = 3
a,b = 0,0
# img_begin = Image.new('RGB', (screenWidth , screenHeight))
# tạo ảnh trống với kích thước của lưới
img = Image.new('RGB', (cell_size_width * grid_size, cell_size_height * grid_size), (255, 255, 255))
draw = ImageDraw.Draw(img)
# img_begin.paste(img, (a, b))
# img.paste(img_begin, (a, b))
# vẽ lưới ô
for i in range(grid_size):
    for j in range(grid_size):
        x = i * cell_size_width 
        y = j * cell_size_height 
        draw.rectangle((x, y, x + cell_size_width, y + cell_size_height), outline=(0, 0, 0))
        draw.text((x + 40, y + 40), str(j * grid_size + i + 1), fill=(0, 0, 0), font= ImageFont.truetype("arial.ttf", 40))
    # draw.text((x + 10, y + 10), str(i * grid_size +j+ 1), fill=(0, 0, 0))
# # hiển thị lưới ô

def draw_box(location_x,location_y, target_x_, target_y_):
    cell_size_width_ = target_x_ // 3
    cell_size_height_ = target_y_ // 3
    print(cell_size_width_, cell_size_height_)
    # tạo ảnh trống với kích thước của lưới
    # img_new = Image.new('RGB', (cell_size_width_ * grid_size, cell_size_height_ * grid_size), (255, 255, 255))
    # draw = ImageDraw.Draw(img_new)
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * cell_size_width_ + location_x
            y = j * cell_size_height_ + location_y
            # x = i * cell_size_width_
            # y = j * cell_size_height_
            draw.rectangle((x, y, x + cell_size_width_, y + cell_size_height_), outline=(0, 0, 0))
            # draw.text((x, y), str(j * grid_size + i + 1), fill=(0, 0, 0), font= ImageFont.truetype("arial.ttf", 20))
    return cell_size_width_, cell_size_height_

new_grid_x,new_grid_y = cell_size_width, cell_size_height
old_x,old_y = 0,0
location_x, location_y = 0,0
# root = tk.Tk()
# root.title("Mouse_Grid_draft")
# photo = ImageTk.PhotoImage(img)
# label = tk.Label(root, image=photo)
# label.place(x=0, y=0)
# root.geometry("%dx%d+%d+%d" % (img.size[0], img.size[1], a, b))
# root.attributes('-fullscreen', True)
# close_button = tk.Button(root, text="Close", command=root.destroy)
# close_button.pack()
# root.mainloop()

      
while True:
    # hiển thị lưới ô
    root = tk.Tk()
    root.title("Mouse_Grid_draft")
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.place(x=0, y=0)
    root.geometry("%dx%d+%d+%d" % (img.size[0], img.size[1], a, b))
    root.attributes('-fullscreen', True)
    close_button = tk.Button(root, text="Close", command=root.destroy)
    close_button.pack()
    
    # lấy tọa độ của ô được chọn bằng cách nhận đầu vào từ người dùng hoặc từ giọng nói
    cell_number = int(input("Enter cell number: "))
    
    if (cell_number < 1 or cell_number > grid_size * grid_size):
        break

    x = (cell_number - 1) % grid_size
    y = (cell_number - 1) // grid_size
    print(x,y)
    # kich thuoc cua o moi
    target_x_ = new_grid_x
    target_y_ =  new_grid_y
    location_x =location_x +  x * new_grid_x
    location_y =location_y + y * new_grid_y

    
    # chuyển động chuột vào ô được chọn
    target_x = x * new_grid_x + new_grid_x // 2 + a + old_x
    target_y = y * new_grid_y + new_grid_y // 2 + b + old_y
    pyautogui.moveTo(target_x, target_y, duration=0.25)
    print(target_x, target_y)
    print(target_x_, target_y_)
    new_grid_x,new_grid_y = draw_box(location_x, location_y, target_x_, target_y_)
    old_x, old_y = location_x, location_y
    root.destroy()
    root.mainloop()