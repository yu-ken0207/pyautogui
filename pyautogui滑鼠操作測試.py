import pyautogui
import time

# 獲取當前螢幕解析度
screenWidth, screenHeight = pyautogui.size()
print(pyautogui.size())


# 獲取當前滑鼠位置
currentMouseX, currentMouseY = pyautogui.position()
print(pyautogui.position())


# 2秒鐘滑鼠移動座標為100,100位置  絕對移動
#pyautogui.moveTo(100, 100,2)
#pyautogui.moveTo(x=100, y=100,duration=2, tween=pyautogui.linear)


#滑鼠移到螢幕中央。
#pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

pyautogui.moveTo(1111, 965) #移動
pyautogui.click()   #點擊

time.sleep(1)

pyautogui.moveTo(1501, 864) #移動
pyautogui.click(interval=1)   #點擊


# 滑鼠左擊一次
#pyautogui.click()
# clicks 點選次數
# interval點選之間的間隔
# button 'left', 'middle', 'right' 對應滑鼠 左 中 右或者取值(1, 2, or 3)
# tween 漸變函式
#pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)


#pyautogui.scroll(200)     # 滑鼠向上滾動200畫素
#pyautogui.scroll(-100)    #   負數向下
