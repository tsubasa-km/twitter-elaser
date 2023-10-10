import pyautogui as pag
import keyboard
import sys

# https://twitter.com

SCREEN_SIZE = pag.size()

rt_line = None
more_line = None
deleted_n = {"RT":0,"Tweet":0}

def exit():
    print(f"{deleted_n}")
    sys.exit()

print("RTボタンにポインタをおいてctrlを押してください。")
while True:
    if keyboard.is_pressed("esc"): exit()
    if keyboard.is_pressed("ctrl"):
        pos = pag.position()
        pag.move(100,0)
        pag.sleep(1)
        rt_line = [pos.x-50,0,100+1,SCREEN_SIZE[1]]
        if pag.locateOnScreen("imgs/RT.png",confidence=0.7,region=rt_line):
            print("OK")
            break
        else:
            print("Not found active RT button.")

print("...ボタンにポインタをおいてctrlを押してください。")
while True:
    if keyboard.is_pressed("esc"): exit()
    if keyboard.is_pressed("ctrl"):
        pos = pag.position()
        pag.move(100,0)
        pag.sleep(1)
        more_line = [pos.x-50,0,100+1,SCREEN_SIZE[1]]
        if pag.locateOnScreen("imgs/more.png",confidence=0.7,region=more_line):
            print("OK")
            break
        else:
            print("Not found active more button.")

def click(img_path,**args):
    box = pag.locateOnScreen(img_path,**args)
    if box:
        pag.click(pag.cctrl(box))
        return True
    else:
        return False

while True:
    while True:
        if keyboard.is_pressed("esc"): exit()
        found = click("imgs/RT.png",region=rt_line,confidence=0.9,grayscale=False)
        pag.sleep(1)
        if not found:
            break
        pag.move(100,0)
        pag.sleep(1)
        click("imgs/RT-del.png",confidence=0.7)
        pag.sleep(1)
        deleted_n["RT"] += 1

    if keyboard.is_pressed("esc"): exit()
    found = click("imgs/more.png",region=more_line,confidence=0.7)
    pag.move(100,0)
    pag.sleep(1)
    
    if not click("imgs/del-1.png",confidence=0.7) or not found:
        pag.scroll(-300)
        pag.sleep(1.3)
        continue

    pag.sleep(1)
    click("imgs/del-2.png",confidence=0.7)
    pag.sleep(1)
    deleted_n["Tweet"] += 1