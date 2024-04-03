import pygame
import math

pygame.init()

size=[500,900]
screen=pygame.display.set_mode(size)
title= 'HANGMAN'
pygame.display.set_caption(title)

clock=pygame.time.Clock()
black=[0,0,0]
white=[255,255,255]

def tup_r(tup):
    temp_list=[]
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)

exit=False

while not(exit):
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True

    screen.fill(black)
    A=tup_r((0, size[1]*2/3))
    B=tup_r((size[0], size[1]*2/3))
    pygame.draw.line(screen, white, A, B, 3)
    C=(size[0]/6,A[1])
    D=(C[0],C[0])
    E=(size[0]/2,D[1])
    pygame.draw.line(screen, white, C, D, 3)
    pygame.draw.line(screen, white, D, E, 3)
    F=tup_r((E[0],E[1]+size[0]/6))
    pygame.draw.line(screen, white, F, E, 3)
    r_head=round(size[0]/12)
    G=(F[0], F[1]+r_head)
    pygame.draw.circle(screen, white, G, r_head, 3)
    H=(G[0], G[1]+r_head)
    I=(H[0], H[1]+r_head)
    pygame.draw.line(screen, white, H, I, 3)
    I_arm=r_head*2
    J=(I[0]-I_arm*math.cos(30*math.pi/180),I[1]+I_arm*math.sin(30*math.pi/180))
    K=(I[0]+I_arm*math.cos(30*math.pi/180),I[1]+I_arm*math.sin(30*math.pi/180))
    pygame.draw.line(screen, white, J, I, 3)
    pygame.draw.line(screen, white, K, I, 3)
    I_body=r_head*3
    L=(I[0],I[1]+I_body)
    pygame.draw.line(screen, white, L, I, 3)
    I_leg=r_head*3.5
    M=(L[0]-I_leg*math.cos(60*math.pi/180),L[1]+I_leg*math.sin(60*math.pi/180))
    N=(L[0]+I_leg*math.cos(60*math.pi/180),L[1]+I_leg*math.sin(60*math.pi/180))
    pygame.draw.line(screen, white, L, M, 3)
    pygame.draw.line(screen, white, L, N, 3)
    
    pygame.display.flip()

pygame.quit()