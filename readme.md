<p align="center">
 <img width="100px" src="https://res.cloudinary.com/anuraghazra/image/upload/v1594908242/logo_ccswme.svg" align="center" alt="GitHub Readme Stats" />
 <h2 align="center">GitHub Readme Stats</h2>
 <p align="center">Get dynamically generated GitHub stats on your READMEs!</p>
</p>
  <p align="center">
    <a href="https://github.com/anuraghazra/github-readme-stats/actions">
      <img alt="Tests Passing" src="https://github.com/anuraghazra/github-readme-stats/workflows/Test/badge.svg" />
    </a>
    <a href="https://github.com/minhanh01bg/KT_mouse_grid_build/graphs/contributors">
      <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/minhanh01bg/KT_mouse_grid_build" />
    </a>
    <a href="https://codecov.io/gh/anuraghazra/github-readme-stats">
      <img src="https://codecov.io/gh/minhanh01bg/KT_mouse_grid_build/branch/master/graph/badge.svg" />
    </a>
    <a href="https://github.com/anuraghazra/github-readme-stats/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/minhanh01bg/KT_mouse_grid_build?color=0088ff" />
    </a>
    <a href="https://github.com/anuraghazra/github-readme-stats/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/minhanh01bg/KT_mouse_grid_build?color=0088ff" />
    </a>
    <br />
    <br />
    <a href="https://a.paddle.com/v2/click/16413/119403?link=1227">
      <img src="https://img.shields.io/badge/Supported%20by-VSCode%20Power%20User%20%E2%86%92-gray.svg?colorA=655BE1&colorB=4F44D6&style=for-the-badge"/>
    </a>
    <a href="https://a.paddle.com/v2/click/16413/119403?link=2345">
      <img src="https://img.shields.io/badge/Supported%20by-Node%20Cli.com%20%E2%86%92-gray.svg?colorA=61c265&colorB=4CAF50&style=for-the-badge"/>
    </a>
  </p>
  
---

# Hướng dẫn sử dụng

## Mô tả
- Đây là một ứng dụng nhận diện giọng nói và chuyển thành văn bản. Ứng dụng giúp mọi người khuyết tật tay chân có thể sử dụng được máy tính thông qua giọng nói. Ứng dụng sẽ bắt các từ khóa và thực hiện các hành động tương ứng.
- Ứng dụng sử dụng thư viện speech_recognition của python.
- Ứng dụng sử dụng thư viện pyaudio để lấy dữ liệu âm thanh từ microphone.
- Ứng dụng sử dụng thư viện tkinter để tạo giao diện người dùng.
---
## Cài đặt các thư viện
- Cài đặt python 3.10.6
- Cài đặt thư viện speech_recognition
```md
pip install speech_recognition
```
- Cài đặt thư viện pyaudio
```md
pip install pyaudio
```
- Cài đặt thư viện tkinter
```md
pip install tkinter
```
- Các thư viện còn lại có thể cài đặt trong file requirements.txt
```md
pip install -r requirements.txt
```
---
## Chạy ứng dụng
- Chạy file main.py
```md
python main.py
```
---

## Các chức năng
### Chức năng 1: Di chuyển chuột
- Khi chạy ứng dụng sẽ hiện ra giao diện chính như sau:
![image](images/view.png)
Người dùng có thể chọn một ô bất kì để di chuyển chuột đến chính giữa ô đó
Các từ khóa để có thể bắt được hành động | di chuyển đến ô ..., chọn ô ... 
- Khi chọn được một ô thì chuột sẽ di chuyển đến ô đó và giao diện tiếp tục vẽ thêm chín ô mới trong ô đó như sau:
![image](images/view2.png)
- Để chọn click chuột vào vị trí vừa di chuyển đến, người dùng có thể nói từ khóa "click" hoặc "chọn" để thực hiện hành động click chuột. <br>
ví dụ: <br>
chọn click chuột trái: `chọn chuột trái` hoặc `chuột trái` <br>
chọn click chuột phải: `chọn chuột phải` hoặc `chuột phải` <br>
chọn clich chuột trái 2 lần: `click chuột` <br>
- Để cuộn lên hoặc cuộn xuống người dùng có thể nói từ khóa `cuộn lên` hoặc `cuộn xuống` <br>
### Chức năng 2: Nhập văn bản
- Người dùng có thể nhập vào một ô nào đó bằng cách nói từ khóa `nhập ...` <br>
ví dụ: <br>
Để nhập `nguyễn văn a` vào ô: nói `nhập nguyễn văn a` <br>

- Người dùng có thể xóa một số kí tự nói từ khóa `xóa ...` <br>
ví dụ: <br>
Để xóa 2 kí tự cuối cùng: nói `xóa 2` <br>
Để xóa 1 kí tự cuối cùng: nói `xóa` <br>
### Chức năng 3: Mở ứng dụng
- Để mở một số app như google, word, excel, ... người dùng có thể nói từ khóa `mở ...` <br>
ví dụ: <br>
mở google: nói `mở google` <br>
mở word: nói `mở word` <br>
mở excel: nói `mở excel` <br>

- Sau khi mở google có thể nói mở một trang web mới bằng cách nói từ khóa `mở trang mới`  hoặc `mở tab mới`. Tại thời điểm này có thể nói `nhập ...` và nói `nhập xong` để tìm kiếm. <br>
ví dụ: <br>
Để mở trang web mới: nói `mở trang mới` hoặc `mở tab mới` <br>
nhập `nguyễn văn a` vào ô tìm kiếm: nói `nhập nguyễn văn a` <br>
tìm kiếm: nói `nhập xong` <br>

- Để quay lại trang trước đó nói từ khóa `quay lại` <br>
- Để đóng trang hoặc đóng tab hiện tại nói từ khóa `đóng tab` hoặc `đóng trang` <br>
- Nếu muốn tải lại trang hiện tại nói từ khóa `tải lại` <br>
### Chức năng 4: Một số tiện ích
- Nghe nhạc nói từ khóa `nghe nhạc` <br>
- Nghe thời tiết nói từ khóa `thời tiết` <br>
- Đọc báo nói từ khóa `đọc báo` hoặc `tin tức` <br>
- Nghe giờ nói từ khóa `giờ` <br>
### Chức năng 5: Thoát ứng dụng
- Ngoài ra, người dùng có thể nói từ khóa `thoát` để thoát khỏi ứng dụng <br>


