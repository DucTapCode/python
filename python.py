from gtts import gTTS
import os

# Văn bản cần chuyển đổi
text = input()

# Tạo đối tượng gTTS
tts = gTTS(text=text, lang='vi')

# Lưu giọng nói vào file
tts.save("output.mp3")

# Phát file âm thanh
os.system("start output.mp3")  # Với Windows
# os.system("afplay output.mp3")  # Với macOS
# os.system("mpg321 output.mp3")  # Với Linux
