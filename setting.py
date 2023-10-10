import keyboard
from PIL import Image
import pyautogui as pag
from screen_shot import get_screenshot

imgs = ["RT","RT-del","more","del-1","del-2"]

def setting():
    print("\nボタンの検出に必要なスクリーンショットを撮影します。\n")
    for i in imgs:
        print("\nサンプル画像のような写真をとれる画面に移ってください。")
        print("準備ができたら[ctrl]を長押ししてください。")
        print("マウス左ボタンで範囲を指定して、スペースで決定します。")
        print("ESCで作業を中断できます。")
        Image.open(f"imgs/sample/{i}.png").show("サンプル画像")
        while not keyboard.is_pressed("ctrl"):
            if keyboard.is_pressed("esc"):
                return
        pag.sleep(0.5)
        ss = get_screenshot()
        if ss:
            ss.save(f"imgs/{i}.png")
        else:
            print("\n作業を中断します。")
            return
    print("\n完了しました。")
    input("Enterで終了...")

setting()