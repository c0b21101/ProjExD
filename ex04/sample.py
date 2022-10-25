import pygame as pg
import sys

def main():
    pg.display.set_caption("初めてのPyGame") # タイトルバー「初めての…」を表示する
    scrn_sfc = pg.display.set_mode((800,600)) # 800x600の画面Surfaceを生成する

    tori_sfc = pg.image.load("fig/6.png") # Surface
    tori_rct = tori_sfc.get_rect() # Rect
    tori_rct.center = 700, 400
    # スクリーンにこうかとんを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct)

    pg.display.update()

    clock = pg.time.Clock() # 時間計測用のオブジェクト
    clock.tick(1) # 1fpsの時を刻む


if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()