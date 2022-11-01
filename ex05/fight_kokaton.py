from time import sleep
import pygame as pg
import sys
from random import randint
import os

COLOR_INV = 1


class Screen:
    def __init__(self, title, wh, bgimg):
        # 練習1
        pg.display.set_caption(title) # "逃げろ！こうかとん"
        self.sfc = pg.display.set_mode(wh) # (1600,900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) # "fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) # 練習2


class Bird:
    key_delta = {
        pg.K_UP:    [0, -8],
        pg.K_DOWN:  [0, +8],
        pg.K_LEFT:  [-8, 0],
        pg.K_RIGHT: [+8, 0],
    }  


    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) # 練習3

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.bilt(self.sfc, self.rct) 同じ


class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) # 練習3

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy) # 練習6
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct) # 練習5


class Trans_Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) 
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (radius, radius), radius) 
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound_inv(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        if yoko == -1 or tate == -1:
            pg.draw.circle(self.sfc, (COLOR_INV, 0, 0), (10, 10), 10)
        self.blit(scr)


def check_bound(obj_rct, scr_rct):

    """
    obj_rct：こうかとんrct、または、爆弾rct
    scr_rct：スクリーンrct
    領域内：+1/領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def check_bound_inv(obj_rct, scr_rct):
    global COLOR_INV
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
        if COLOR_INV == 1:
            COLOR_INV = 0
        else:
            COLOR_INV = 1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
        if COLOR_INV == 1:
            COLOR_INV = 0
        else:
            COLOR_INV = 1
    return yoko, tate

def main():
    # 練習1
    scr = Screen("負けるな！こうかとん", (1600,900), "fig/pg_bg.jpg")

    # 練習3
    kkt = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5
    bkd1 = Bomb((255, 0, 0), 10, (+5, +5), scr)
    bkd2 = Bomb((255, 255, 0), 10, (+3, +3), scr)
    bkd3 = Trans_Bomb((0, 0, 255), 10, (+1, +1), scr)

    #画面にSTARTと表示
    fonto = pg.font.Font(None, 80)
    tmr = "START"
    BLUE = ("blue")
    txt = fonto.render(str(tmr), True, BLUE)
    scr.sfc.blit(txt, (725, 450))
    pg.display.update()
    sleep(0.5)

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return # 練習2

        # 練習4
        kkt.update(scr)

        # 練習7
        bkd1.update(scr)
        bkd2.update(scr)
        bkd3.update(scr)

        # 画面にGAME OVERと表示
        # 練習8
        if kkt.rct.colliderect(bkd1.rct): # こうかとんrctが爆弾rctと重なったら
            # こうかとんrctが爆弾rctと重なったら画面にGAME OVERと表示
            fonto = pg.font.Font(None, 80)
            tmr = "GAME OVER"
            RED = ("red")
            txt = fonto.render(str(tmr), True, RED)
            scr.sfc.blit(txt, (660, 450))
            pg.display.update()
            sleep(1)
            pg.quit()
            sys.exit()

        if kkt.rct.colliderect(bkd2.rct): # こうかとんrctが爆弾rctと重なったら
            #こうかとんrctが爆弾rctと重なったらGAME OVERを表示
            fonto = pg.font.Font(None, 80)
            tmr = "GAME OVER"
            RED = ("red")
            txt = fonto.render(str(tmr), True, RED)
            scr.sfc.blit(txt, (660, 450))
            pg.display.update()
            sleep(1)
            pg.quit()
            sys.exit()

        if kkt.rct.colliderect(bkd3.rct): # こうかとんrctが爆弾rctと重なったら
            #こうかとんrctが爆弾rctと重なったらGAME OVERを表示
            fonto = pg.font.Font(None, 80)
            tmr = "GAME OVER"
            RED = ("red")
            txt = fonto.render(str(tmr), True, RED)
            scr.sfc.blit(txt, (660, 450))
            pg.display.update()
            sleep(1)
            pg.quit()
            sys.exit()

        pg.display.update() # 練習2
        clock.tick(1000)


def sound():
    pg.mixer.init(frequency=44100)
    pg.mixer.music.load("ex05/data/忘れえぬ季節.mp3")
    pg.mixer.music.play(1)
    while main():
        break
    pg.mixer.music.stop()
    return 0


if __name__ == "__main__":
    pg.init()
    sound()
    main()
    pg.quit()
    sys.exit()