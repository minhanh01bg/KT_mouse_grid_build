import sys
# from cx_Freeze import setup, Executable
import ssl

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# # ,"c:/users/fancyma/anaconda3/envs/design_interface/lib/site-packages/pygame"
# # Thêm module SSL vào các thư viện của cx_Freeze
build_exe_options = {
    "packages": ["pygame","tkinter", "pynput", "speech_recognition", "pyttsx3", "requests", "webbrowser", "datetime", "os", "playsound", "wikipedia", "selenium", "gtts", "youtube_search", "re", "ssl","certifi","urllib","urllib.request"],
    "include_files": ["./mouse_grid_class.py", "./Type_write_vietnamese.py", "./speech_to_text.py","c:/users/fancyma/anaconda3/envs/design_interface/lib/site-packages/pygame"],
    "include_msvcr": True,
    "include_files": [ssl.get_default_verify_paths().openssl_cafile],
    "zip_include_packages": "*",
    "zip_exclude_packages": ["collections.abc"],
    # "build_exe": "../build"
}

base = None
# if sys.platform == 'win32':
#     base = "Win32GUI"

# setup(
#     name="Virtual Assistant",
#     version="1.0",
#     description="My tkinter app",
#     options={"build_exe": build_exe_options},
#     include_package_data=True,
#     # Thay đổi đường dẫn cho phù hợp
#     executables=[Executable("main.py", base=base)],
#     # install_requires=requirements
# )
from setuptools import setup, find_packages, Executable
# import nuitka
setup(
    name='MyApp',
    version='1.0',
    description='My Python app',
    packages=find_packages(),
    include_package_data=True,
    options={"build_exe": build_exe_options},
    executables=[Executable('main.py', base=base)],
    install_requires=requirements,
    
    # package_data={
    # '': ['*.txt', '*.rst',"*.py"],
    # },
)
