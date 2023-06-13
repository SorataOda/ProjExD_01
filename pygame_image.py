import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    bg_img_fl=pg.transform.flip(bg_img,True,False)
    kk_img=pg.image.load("ex01-20230613/fig/3.png")
    kk_img=pg.transform.flip(kk_img,True,False)
    kk_rt=pg.transform.rotozoom(kk_img,10,1.0)
    
    kk_lst=[kk_img,kk_rt]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_lst[tmr%2],[300,200])
        
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()