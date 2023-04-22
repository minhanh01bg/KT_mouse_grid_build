# import speech_to_text
import pyautogui
from PIL import Image,ImageDraw,ImageTk,ImageFont
import tkinter as tk
from pynput.keyboard import Key,Controller
from speech_to_text import get_audio, speak, get_text, get_number, play_music, read_news, get_time, open_application, current_weather, read_news1,weather,get_time1
import re 
from mouse_grid_class import Mouse_Grid
import Type_write_vietnamese
import re

def extract_numbers(str):
    return re.findall('\d+', str)


def handle_text(text,mouse_grid,root,grid_size,check):
    print(text)
    if "di chuyển" in text or "chọn ô" in text or "chọn số" in text or "chọn ô số" in text or "chọn o" in text or "ô" in text.split() or "o" in text.split():
        try:
            cell_number = get_number(text)
            if (cell_number < 1 or cell_number > grid_size * grid_size):
                speak("tôi không nghe rõ ô bạn muốn chọn.")
                root.destroy()
                return 0

            x = (cell_number - 1) % grid_size
            y = (cell_number - 1) // grid_size
            # print("x: ", x, "y: ", y)

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
        except:
            return -2
    
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
    elif "đóng trang" in text or "đóng tab" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.ctrl)
        keyb.press('w')
        keyb.release('w')
        keyb.release(Key.ctrl)
        return 0
    
    # backspace
    elif "xóa" in text:
        root.destroy()
        keyb = Controller()
        try:
            number = extract_numbers(text)
            # print(number[0])
            num = number[0]
            for i in range(int(num)):
                keyb.press(Key.backspace)
                keyb.release(Key.backspace)
        except:
            keyb.press(Key.backspace)
            keyb.release(Key.backspace)
        return 0

    # ctrl + t
    elif "mở trang mới" in text or "mở tab mới" in text:
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
        current_weather(check)
        # weather()
        return 0
    # play music
    elif "nghe nhạc" in text or "nhạc" in text:
        root.destroy()
        play_music(check)
        return 0
    # read news
    elif "đọc tin tức" in text or "tin tức" in text or "đọc báo" in text:
        root.destroy()
        read_news1(check)
        return 0
    # get time 
    elif "thời gian" in text or "mấy giờ" in text or "giờ" in text or "ngày" in text or "tháng" in text or "năm" in text:
        root.destroy()
        get_time(text)
        return 0
    # open application
    elif "mở" in text:
        root.destroy()
        open_application(text)
        return 0
    # press enter
    elif "nhập xong" in text or "enter" in text:
        root.destroy()
        keyb = Controller()
        keyb.press(Key.enter)
        keyb.release(Key.enter)
        return 0
    
    elif "dừng" in text or "tạm dừng vẽ" in text:
        root.destroy()
        return 1

    elif "vẽ lại" in text or "vẽ" in text:
        return -1
    
    elif "thoát" in text:
        root.destroy()
        import sys
        print(1)
        sys.exit()
        # raise SystemExit(0)
    # root.destroy()
    return -2

if __name__ == "__main__":
    grid_size = 3
    mouse_grid = Mouse_Grid(grid_size)
    # mouse_grid.draw_grid()
    check = True
    while True:
        # mouse_grid.display_grid()
        # try:
            root = tk.Tk()
            root.title("Mouse_Grid_draft")
            photo = ImageTk.PhotoImage(mouse_grid.img)
            label = tk.Label(root, image=photo)
            label.place(x=0, y=0)
            root.geometry("%dx%d+%d+%d" % (mouse_grid.img.size[0], mouse_grid.img.size[1], 0, 0))
            root.attributes('-fullscreen', True)

            if check == True:
                root.attributes('-alpha', 0.3)
            else:
                root.attributes('-alpha', 0)

            root.attributes("-topmost", True)
            # close_button = tk.Button(root, text="Close", command=root.destroy)
            # close_button.pack()
            root.deiconify()
            root.update()
            # root.after(0, get_text)
            # root.update_idletasks()
            # root.mainloop()

            text = get_text(check)
            check_redraw = handle_text(text,mouse_grid,root,grid_size,check)

            if check_redraw == -1:
                root.destroy()
                mouse_grid = Mouse_Grid(grid_size)
                check = True

            if check_redraw == 1:
                check = False

            if check_redraw == -2:
                speak("Tôi không hiểu ý bạn")
                root.destroy()
                # break
        # except:
        #     pass
            

        