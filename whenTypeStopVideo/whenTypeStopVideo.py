import time
from pynput import keyboard
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# 使用selenium创建一个Edge浏览器实例，需要替换为你的Edge WebDriver路径
options = Options()
service = Service('./msedgedriver.exe')
driver = webdriver.Edge(options=options, service=service)

# 访问你的Bilibili视频
driver.get('https://www.bilibili.com/video/BV1Lx41167E3/?spm_id_from=333.999.0.0&vd_source=a249f0cab5afb0bf4145dcf674cac958')

# 暂停的javascript脚本
pause_script = """
var vids = document.getElementsByTagName('video');
for (var i = vids.length - 1; i >= 0; i--){
    vids[i].pause();
}
"""

# 播放的javascript脚本
play_script = """
var vids = document.getElementsByTagName('video');
for (var i = vids.length - 1; i >= 0; i--){
    vids[i].play();
}
"""

# 标记键盘最后一次输入时间
last_key_press_time = time.time()

# 定义键盘按键按下的事件
def on_press(key):
    global last_key_press_time
    # 更新键盘最后一次输入时间
    last_key_press_time = time.time()
    # 执行暂停的javascript脚本
    driver.execute_script(pause_script)

# 创建键盘监听器
listener = keyboard.Listener(on_press=on_press)
listener.start()

# 每隔一段时间检查键盘是否在3秒内有输入
while True:
    if time.time() - last_key_press_time > 2:
        # 如果3秒内没有输入，执行播放的javascript脚本
        driver.execute_script(play_script)
    time.sleep(0.1)
