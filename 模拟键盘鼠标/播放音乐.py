import time
import pygame

# 音乐路径
filepath = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\不仅仅是喜欢.mp3"

# 全部模块初始化
# pygame.init()

# 初始化
pygame.mixer.init()

# 加载音乐
# pygame.mixer.Sound(filepath)
pygame.mixer.music.load(filepath)

# 暂停
# pygame.mixer.music.pause()

# 播放
# pygame.mixer.Sound.play()
pygame.mixer.music.play()

# 暂停
time.sleep(100)

# 停止
pygame.mixer.music.stop()
# pygame.mixer.Sound.stop()