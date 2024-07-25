import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

# Hàm mở hộp thoại chọn file ảnh
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        load_image(file_path)

# Hàm mở hộp thoại chọn file video
def open_video():
    global cap, video_mode
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")])
    if file_path:
        if cap:
            cap.release()
        cap = cv2.VideoCapture(file_path)
        video_mode = True
        play_video()

# Hàm tải và hiển thị ảnh
def load_image(path):
    global video_mode
    video_mode = False
    try:
        img = Image.open(path)
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img
        path_entry.delete(0, tk.END)
        path_entry.insert(0, path)
    except Exception as e:
        print(f"Failed to load image: {e}")

# Hàm cập nhật ảnh từ đường dẫn trong entry
def update_image():
    path = path_entry.get()
    load_image(path)

# Hàm phát video
def play_video():
    if video_mode:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
            frame = cv2.resize(frame, (screen_width, screen_height))
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            panel.config(image=img)
            panel.image = img
        panel.after(10, play_video)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Simple Media Viewer")
root.attributes("-fullscreen", True)  # Thiết lập cửa sổ toàn màn hình

# Thêm phím ESC để thoát khỏi chế độ toàn màn hình
def exit_fullscreen(event):
    root.attributes("-fullscreen", False)

root.bind("<Escape>", exit_fullscreen)

# Tạo frame để chứa các nút và entry
frame = tk.Frame(root)
frame.pack(side=tk.TOP, fill=tk.X)

# Nút mở ảnh
open_image_button = tk.Button(frame, text="Open Image", command=open_image)
open_image_button.pack(side=tk.LEFT, padx=5, pady=5)

# Nút mở video
open_video_button = tk.Button(frame, text="Open Video", command=open_video)
open_video_button.pack(side=tk.LEFT, padx=5, pady=5)

# Entry để nhập đường dẫn ảnh
path_entry = tk.Entry(frame, width=50)
path_entry.pack(side=tk.LEFT, padx=5, pady=5)

# Nút cập nhật ảnh từ đường dẫn
update_button = tk.Button(frame, text="Update Image", command=update_image)
update_button.pack(side=tk.LEFT, padx=5, pady=5)

# Tạo panel để hiển thị ảnh hoặc video
panel = tk.Label(root)
panel.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Khởi tạo biến toàn cục
cap = None
video_mode = False

# Chạy vòng lặp chính
root.mainloop()