import pygame
import sys
import time
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    surface = pygame.Surface((300,300))
    surface2 = pygame.Surface((30,30))
    surface2.fill((0,0,255))
    surface
    screen.blit(surface,surface.get_rect())
    screen.fill((255,255,255), screen.get_rect())
    x = 0
    y = 0
    flag = True
    pygame.draw.rect(surface2,(255, 0, 230),((x,y),(10,10)),1)
    rect = surface2.get_rect()
    while True:
        # surface.fill((255,155,200),surface.get_rect())
        surface2.fill((0,0,255))
        surface.blit(surface2, rect)
        if flag:
            surface.blit(surface2, rect)
            flag = False

        # surface.fill((255,255,255))
        # pygame.draw.rect(surface,(255, 0, 230), ((0, 0), (self._width, self._height)), 1)
        
        x +=1
        y +=1
        time.sleep(1)
        screen.blit(surface,rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                rect.width = rect.width + 10
                rect.height = rect.height + 10
                print(rect.width, rect.height)
                print(surface2.get_size() , id(surface2))
                surface2 = pygame.transform.smoothscale(surface2,(rect.height, rect.width))
                print(surface2.get_size() , id(surface2))
                # surface2 = pygame.Surface((rect.width,rect.height))
                # pygame.transform.



