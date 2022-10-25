from time import sleep
import pygame as pg
import sys
from random import randint

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

def main():
    # 練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    # 練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    # 練習5
    bomb_sfc= pg.Surface((20, 20)) # 空のSurface
    bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を投下させる
    pg.draw.circle(bomb_sfc,(255, 0, 0), (10, 10), 10) # 円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    # #爆弾追加
    bomb_sfc2 = pg.Surface((20, 20)) # 空のSurface
    bomb_sfc2.set_colorkey((0, 0, 0)) # 四隅の黒い部分を投下させる
    pg.draw.circle(bomb_sfc2,(255, 255, 0), (10, 10), 10) # 円を描く
    bomb_rct2 = bomb_sfc2.get_rect()
    bomb_rct2.centerx = randint(0, scrn_rct.width)
    bomb_rct2.centery = randint(0, scrn_rct.height)
    
    # 練習6
    vx, vy = +1, +1
    vx2, vy2 = +2, +2

    #画面にSTARTと表示
    fonto = pg.font.Font(None, 80)
    tmr = "START"
    BLUE = ("blue")
    txt = fonto.render(str(tmr), True, BLUE)
    scrn_sfc.blit(txt, (725, 450))
    pg.display.update()
    sleep(1)

    clock = pg.time.Clock() # 練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習2

        for event in pg.event.get():
            if event.type == pg.QUIT: return # 練習2

        # 練習4
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:    tori_rct.centery -= 1 
        if key_states[pg.K_DOWN]:  tori_rct.centery +=1
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]:  
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]:  
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1
        scrn_sfc.blit(tori_sfc, tori_rct) # 練習3

        yoko, tate = check_bound(bomb_rct, scrn_rct)
        yoko2, tate2 = check_bound(bomb_rct2, scrn_rct)
        vx *= yoko
        vy *= tate
        vx2 *= yoko2
        vy2 *= tate2
        bomb_rct.move_ip(vx, vy) # 練習6
        bomb_rct2.move_ip(vx2, vy2) # 爆弾追加
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5
        scrn_sfc.blit(bomb_sfc2, bomb_rct2) # 爆弾追加

        # 画面にGAME OVERと表示
        # 練習8
        if tori_rct.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
            # こうかとんrctが爆弾rctと重なったら画面にGAME OVERと表示
            fonto = pg.font.Font(None, 80)
            tmr = "GAME OVER"
            RED = ("red")
            txt = fonto.render(str(tmr), True, RED)
            scrn_sfc.blit(txt, (660, 450))
            pg.display.update()
            sleep(1)
            pg.quit()
            sys.exit()

        if tori_rct.colliderect(bomb_rct2): # こうかとんrctが爆弾rctと重なったら
            #こうかとんrctが爆弾rctと重なったらGAME OVERを表示
            fonto = pg.font.Font(None, 80)
            tmr = "GAME OVER"
            RED = ("red")
            txt = fonto.render(str(tmr), True, RED)
            scrn_sfc.blit(txt, (660, 450))
            pg.display.update()
            sleep(1)
            pg.quit()
            sys.exit()
            
        pg.display.update() # 練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()