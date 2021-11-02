##Programa toca um arquivo de audio!

import pygame
pygame.init()
pygame.mixer.music.load('xxx.ogg')
pygame.mixer.music.play()
pygame.event.wait()
 
