from PIL import Image,ImageEnhance
import pygame as pg
import keyboard
import pyautogui as pag
import copy


class SelectedRange:
    start_point = None
    rect = None
    left_plessed = False
    @classmethod
    def get_range(cls):
        if pg.mouse.get_pressed()[0]:
            if cls.start_point==None or not cls.left_plessed:
                cls.start_point = copy.deepcopy(list(pg.mouse.get_pos()))
            start = copy.deepcopy(cls.start_point)
            end = copy.deepcopy(list(pg.mouse.get_pos()))
            w = end[0]-start[0]
            h = end[1]-start[1]
            if w < 0:
                start[0] += w
                w *= -1
            if h < 0:
                start[1] += h
                h *= -1
            cls.rect = pg.Rect(*start,w,h)
            cls.left_plessed = True
        else:
            cls.left_plessed = False
        return cls.rect


def get_screenshot()->Image.Image|None:
    """範囲を指定してスクリーンショット
    マウス左ドラッグで範囲指定。
    スペースで決定。

    Returns:
        Image.Image|None: Pil Image
    """
    image = pag.screenshot()
    pg.init()
    screen = pg.display.set_mode(flags=pg.FULLSCREEN)
    pg_img = pg.image.fromstring(image.tobytes(),image.size,image.mode)
    img_filter = pg.Surface(pg_img.get_size(),pg.SRCALPHA)
    pg.display.flip()
    while True:
        screen.fill((255,255,255))
        screen.blit(pg_img,[0,0])
        screen.blit(img_filter,[0,0])
        img_filter.fill([0,0,0,150])
        rect = SelectedRange.get_range()
        if rect:
            img_filter.fill((0,0,0,0),rect)
            pg.draw.rect(screen,(255,255,255),rect,width=2)
        pg.display.update()
        for event in pg.event.get():
            if (event.type == pg.QUIT or
                (event.type == pg.KEYDOWN and
                 event.key == pg.K_ESCAPE)):
                pg.quit()
                return None
            if (event.type == pg.KEYDOWN and
                event.key == pg.K_SPACE):
                pg.quit()
                if not rect:
                    return None
                return image.crop((rect.left,rect.top,rect.right,rect.bottom))


if __name__ == "__main__":
    get_screenshot().save("imgs/test.png")