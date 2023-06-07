import psutil

# Tìm các tiến trình đang chạy và đóng tiến trình của ứng dụng bàn phím
for process in psutil.process_iter():
    try:
        if process.name() == "osk.exe":
            process.kill()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
