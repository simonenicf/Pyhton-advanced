import pygame

class Player():
    
    lives = 0
    points = 0
    speed = 5
    sprite = pygame.image.load("../art/spr_Player.png")
    rect = sprite.get_rect()
    