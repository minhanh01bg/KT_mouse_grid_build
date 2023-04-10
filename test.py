import webbrowser
from youtube_search import YoutubeSearch
import os 
text = "excel"
if "google" in text:
    print("Mở google")
    os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")
elif "word" in text:
    print("Mở word")
    os.startfile("C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")
elif "excel" in text:
    print("Mở excel")
    os.startfile("C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")
else:
    print("Ứng dụng bạn muốn mở không có trong danh sách")