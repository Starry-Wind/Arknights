import os
import pyautogui
import cv2 as cv
import numpy as np
import time




def screenshot():
    os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
    os.system('adb pull /sdcard/screencap.png ./debug/screenshot.png')


    
def scan_screenshot(prepared):
    screenshot = cv.imread('./debug/screenshot.png')
    result = cv.matchTemplate(screenshot, prepared, cv.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    return {'screenshot': screenshot, 'min_val': min_val, 'max_val': max_val, 'min_loc': min_loc, 'max_loc': max_loc}





 
def calculated(result, shape):
    mat_top, mat_left = result['max_loc']
    prepared_height, prepared_width, prepared_channels = shape

    x = int((mat_top + mat_top + prepared_width) / 2)

    y = int((mat_left + mat_left + prepared_height) / 2)

    return x,y
    






 

def start():
    os.system('adb connect 127.0.0.1:62001')   #连接模拟器
    screenshot()
    target = cv.imread('./temp/startgame.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.9999:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)
    else:
        print("未在主界面，请重试")
    
    time.sleep(2)
    screenshot()
    target = cv.imread('./temp/chose.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.9999:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)


    time.sleep(3)
    screenshot()
    target = cv.imread('./temp/start1.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.9999:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)


    time.sleep(3)
    screenshot()
    target = cv.imread('./temp/start2.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.98:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)



def check():
    screenshot()
    target = cv.imread('./temp/qiyu.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.9:
        os.system('adb shell input tap 60 60')
        time.sleep(1)
        os.system('adb shell input tap 60 60')
        return 1


def start_day():
    time.sleep(5)
    screenshot()
    target = cv.imread('./temp/start3.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.97:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)


    
    screenshot()
    target = cv.imread('./temp/suoxiao.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.97:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)
    
        

    screenshot()
    target = cv.imread('./temp/fangda.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.9:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)



    time.sleep(2)
    screenshot()
    target = cv.imread('./temp/ziyuanqu.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.9:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)
        screenshot()
        target = cv.imread('./temp/startmission.png')
        result = scan_screenshot(target)
        time.sleep(1)
        if result['max_val'] > 0.9:
            points = calculated(result, target.shape)
            print(points)
            os.system('adb shell input tap %d %d' %points)
    else:
        screenshot()
        target = cv.imread('./temp/buliequ.png')
        result = scan_screenshot(target)
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)
        screenshot()
        target = cv.imread('./temp/startmission.png')
        result = scan_screenshot(target)
        time.sleep(1)
        if result['max_val'] > 0.9:
            points = calculated(result, target.shape)
            print(points)
            os.system('adb shell input tap %d %d' %points)
    
   




def startmission():
    time.sleep(1)
    screenshot()
    target = cv.imread('./temp/ready1.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.97:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)


    time.sleep(1)

    screenshot()
    target = cv.imread('./temp/ready2.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.97:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)

    time.sleep(1)
    screenshot()
    target = cv.imread('./temp/yes.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.97:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)

    time.sleep(7)

    os.system('adb shell input tap 100 90')
    time.sleep(1)
    os.system('adb shell input tap 1500 650')
    time.sleep(4)
    os.system('adb shell input tap 1500 650')
    time.sleep(4)
    os.system('adb shell input tap 60 1000')


    
def nextday():
    screenshot()
    target = cv.imread('./temp/nextday.png')
    result = scan_screenshot(target)
    if result['max_val'] > 0.97:
    
        points = calculated(result, target.shape)
        print(points)
        os.system('adb shell input tap %d %d' %points)



def leave():
    os.system('adb shell input tap 60 60') 
    os.system('adb shell input tap 1200 985')
    os.system('adb shell input tap 1250 740') 
    time.sleep(3)
    os.system('adb shell input tap 1750 935')
    time.sleep(2)
    os.system('adb shell input tap 1750 935')
    time.sleep(2)
    os.system('adb shell input tap 1750 935')
    




while True:
    print("三秒后开始")
    time.sleep(3)
    start()
    start_day()  #开始第一次行动
    time.sleep(2)
    if(check()==1):         #检测奇遇
        time.sleep(2)
        os.system('adb shell input tap 1240 988') 
        time.sleep(1)
        os.system('adb shell input tap 1275 740')
        time.sleep(5)
        os.system('adb shell input tap 1748 940')
        time.sleep(2)
        os.system('adb shell input tap 1795 935')
        print("发现错误，重新开始")
    else:    
        time.sleep(1)
        startmission()
        start_day()  #开始第二次行动
        time.sleep(1)
        startmission()
        time.sleep(1)
        nextday()   #进入第二天
        start_day() #开始第一次行动
        time.sleep(1)
        startmission()
        start_day()  #开始第二次行动
        time.sleep(1)
        startmission()
        time.sleep(1)
        nextday()   #进入第三天
        time.sleep(15)  #等待播报
        start_day() #开始第一次行动
        time.sleep(1)
        startmission()
        start_day()  #开始第二次行动
        time.sleep(1)
        startmission()
        time.sleep(1)
        nextday()   #进入第四天
        time.sleep(15)  #等待播报
        start_day() #开始第一次行动
        time.sleep(1)
        startmission()
        start_day()  #开始第二次行动
        time.sleep(1)
        startmission()
        time.sleep(1)
        leave()
        print("已完成轮次")