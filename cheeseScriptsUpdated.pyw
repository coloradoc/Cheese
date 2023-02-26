import pygame
import os
import time
import random
from PIL import Image


# Get the user's home directory and the desktop folder
home_dir = os.path.expanduser(r"C:\Users\FRC")
desktop_dir = os.path.join(home_dir, "Desktop")

# Set the directory containing the images
image_dir = r"cheese"

# Iterate over the files in the directory
for filename in os.listdir(image_dir):
    # Filter out non-image files
    if not filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        continue

    # Load the image
    image_path = os.path.join(image_dir, filename)
    image = Image.open(image_path)

    # Save the image to the desktop folder
    desktop_path = os.path.join(desktop_dir, filename)
    image.save(desktop_path)

    # Optional: print a message indicating that the file was saved
    print(f"Saved {filename} to desktop")


def program():
    pygame.init()
    w=pygame.display.set_mode((0,0))

    g=True
    cheese_dir=r"C:\Users\FRC\Desktop\Cheese-main\dataset\cheese"
    imgs = [pygame.transform.scale(pygame.image.load(cheese_dir+"/"+img),(w.get_width(),w.get_height())) for img in os.listdir(cheese_dir)]
    while g:
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        imgs = [pygame.transform.scale(pygame.image.load(cheese_dir+"/"+img),(mouse_x,mouse_y)) for img in os.listdir(cheese_dir)]

        print(mouse_x)
        counter = -1
        for img in imgs:
            counter+= 1
            print(counter)
        for img in imgs:
            time.sleep(.05)
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            w.blit(imgs[random.randint(0, counter)],(mouse_x,mouse_y))
            pygame.display.update()
            #time.sleep(2*random.random())

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    g=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:

                        pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_0:
                        g=False
                        pygame.quit()

                        
            
            if not g:
                break

    pygame.quit()

def do():
    try:
        program()
    except:
        print("ERROR")
        pass

while True:
    do()



