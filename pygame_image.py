import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    bg_img_2=pg.transform.flip(bg_img,True,False)
    kk_img=pg.image.load("ex01-20230613/fig/3.png")
    kk_img=pg.transform.flip(kk_img,True,False)
    kk_rt=pg.transform.rotozoom(kk_img,10,1.0)
    kk_rt_1=pg.transform.rotozoom(kk_img,2,1.0)
    kk_rt_2=pg.transform.rotozoom(kk_img,4,1.0)
    kk_rt_3=pg.transform.rotozoom(kk_img,6,1.0)
    kk_rt_4=pg.transform.rotozoom(kk_img,8,1.0)
    
    kk_lst=[kk_img,kk_rt_1,kk_rt_2,kk_rt_3,kk_rt_4,kk_rt,kk_rt_4,kk_rt_3,kk_rt_2,kk_rt_1]

    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_2,[1600-x,0])
        screen.blit(bg_img,[3200-x,0])
        screen.blit(kk_lst[tmr%9],[300,200])
        
        pg.display.update()
        tmr += 1 
        
        
        

        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()