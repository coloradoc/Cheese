import pygame
import os
import time

pygame.init()
w=pygame.display.set_mode((0,0))

g=True
accel = 0
cheese_dir="cheeses"
imgs = [pygame.transform.scale(pygame.image.load(cheese_dir+"/"+img),(w.get_width(),w.get_height())) for img in os.listdir(cheese_dir)]
while g:
    for img in imgs:
        w.blit(img,(0,0))
        pygame.display.update()
        time.sleep(max(2-accel, 0.005))
        accel += 0.005

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                g=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    g=False
                if event.key==pygame.K_SPACE:
                    time.sleep(2)
                    
        
        if not g:
            break

pygame.quit()
