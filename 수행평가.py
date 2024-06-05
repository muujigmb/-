import pygame #파이 게임 모듈 임포트
import random
import time

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 
pygame.display.set_caption("두더지 잡기(강민,승민,영광)")

#변수

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 36)
score = 0
start_time = int(time.time()) #1970년 1월 1일 0시 0분 0초 부터 현제까지 초 
remain_second = 100
game_over = False

mole_image = pygame.image.load('1711408373324.jpg')
moles = []
bomb_image=pygame.image.load('영그랫.png')
bombs=[]

bomb2_image=pygame.image.load('승민이-후원해주세요.jpg')
bombs2=[]



for i in range(3):
    mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
    after_second = 2
    during_second = 1
    appear_time = int(time.time()) + after_second
    disappear_time = int(time.time()) + after_second + during_second
    moles.append((mole, appear_time, disappear_time))

for i in range(5):
    bomb = bomb_image.get_rect(left=random.randint(0, SCREEN_WIDTH - bomb_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - bomb_image.get_height()))
    after_second = 2
    during_second = 1
    appear_time = int(time.time()) + after_second
    disappear_time = int(time.time()) + after_second + during_second
    bombs.append((bomb, appear_time, disappear_time))

for i in range(5):
    bomb2 = bomb2_image.get_rect(left=random.randint(0, SCREEN_WIDTH - bomb2_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - bomb2_image.get_height()))
    after_second = 2
    during_second = 1
    appear_time = int(time.time()) + after_second
    disappear_time = int(time.time()) + after_second + during_second
    bombs2.append((bomb2, appear_time, disappear_time))

pygame.mixer.init()
pygame.mixer.music.load('bgm.ogg') #배경 음악
pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번
whack_sound = pygame.mixer.Sound('깡.ogg') #사운드
game_over_sound = pygame.mixer.Sound('게임오버.ogg')
game_clear_sound = pygame.mixer.Sound('게임클리어.ogg')

while True: #게임 루프
    screen.fill(BLACK) #단색으로 채워 화면 지우기

    #변수 업데이트

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
        print(event.pos[0], event.pos[1])
        for mole, appear_time, disappear_time in moles:
            if mole.collidepoint(event.pos):
                print(mole)
                moles.remove((mole, appear_time, disappear_time))
                mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
                after_second = 2
                during_second = 1
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                moles.append((mole, appear_time, disappear_time))
                score += 1
                whack_sound.play()


        for bomb, appear_time, disappear_time in bombs:
            if bomb.collidepoint(event.pos):
                print(bomb)
                bombs.remove((bomb, appear_time, disappear_time))
                bomb = bomb_image.get_rect(left=random.randint(0, SCREEN_WIDTH - bomb_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - bomb_image.get_height()))
                after_second = 2
                during_second = 1
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                bombs.append((bomb, appear_time, disappear_time))
                score -= 1
                whack_sound.play()


        for bomb2, appear_time, disappear_time in bombs2:
            if bomb2.collidepoint(event.pos):
                print(bomb2)
                bombs2.remove((bomb2, appear_time, disappear_time))
                bomb2 = bomb2_image.get_rect(left=random.randint(0, SCREEN_WIDTH - bomb2_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - bomb2_image.get_height()))
                after_second = 2
                during_second = 1
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                bombs2.append((bomb2, appear_time, disappear_time))
                score -= 2
                whack_sound.play()



    if not game_over:       
        current_time = int(time.time())
        remain_second = 100 - (current_time - start_time)

        if remain_second <= 0 or score <= -1:
            game_over = True
            for mole, appear_time, disappear_time in moles:
                current_time = int(time.time())
                if appear_time > current_time:  
                    moles.remove((mole, appear_time, disappear_time))

            for bomb, appear_time, disappear_time in bombs:
                current_time = int(time.time())
                if appear_time > current_time:  
                    bombs.remove((bomb, appear_time, disappear_time))
            
            for bomb2, appear_time, disappear_time in bombs2:
                current_time = int(time.time())
                if appear_time > current_time:  
                    bombs2.remove((bomb2, appear_time, disappear_time))
            pygame.mixer.music.stop()
            if score<=-1:
                game_over_sound.play()
            if score>=1:
                game_over_sound.stop()
                game_clear_sound.play()

        for mole, appear_time, disappear_time in moles:
            current_time = int(time.time())
            if current_time > disappear_time:  
                moles.remove((mole, appear_time, disappear_time))
                mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
                after_second = 2
                during_second = 1
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                moles.append((mole, appear_time, disappear_time))

        for bomb, appear_time, disappear_time in bombs:
            current_time = int(time.time())
            if current_time > disappear_time:  
                bombs.remove((bomb, appear_time, disappear_time))
                bomb = bomb_image.get_rect(left=random.randint(0, SCREEN_WIDTH - bomb_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - bomb_image.get_height()))
                after_second = 2
                during_second = 1
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                bombs.append((bomb, appear_time, disappear_time))

        for bomb2, appear_time, disappear_time in bombs2:
            current_time = int(time.time())
            if current_time > disappear_time:  
                bombs2.remove((bomb2, appear_time, disappear_time))
                bomb2 = bomb2_image.get_rect(left=random.randint(0, SCREEN_WIDTH - bomb2_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - bomb2_image.get_height()))
                after_second = 2
                during_second = 1
                appear_time = int(time.time()) + after_second
                disappear_time = int(time.time()) + after_second + during_second
                bombs2.append((bomb2, appear_time, disappear_time))

    #화면 그리기

    for mole, appear_time, disappear_time in moles:
        current_time = int(time.time())
        if  current_time >= appear_time:  
            screen.blit(mole_image, mole)

    for bomb, appear_time, disappear_time in bombs:
        current_time = int(time.time())
        if  current_time >= appear_time:  
            screen.blit(bomb_image, bomb)

    for bomb2, appear_time, disappear_time in bombs2:
        current_time = int(time.time())
        if  current_time >= appear_time:  
            screen.blit(bomb2_image, bomb2)

    score_image = small_font.render('점수 {}'.format(score), True, YELLOW)
    screen.blit(score_image, (10, 10))

    remain_second_image = small_font.render('남은 시간 {}'.format(remain_second), True, YELLOW)
    screen.blit(remain_second_image, remain_second_image.get_rect(right=SCREEN_WIDTH - 10, top=10))

    if game_over:
        if score<=-1:
            game_over_image = large_font.render('게임 종료', True, RED)
            screen.blit(game_over_image, game_over_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

        if score>=-1:
            game_clear_image = large_font.render('score : %d' %score, True, RED)
            screen.blit(game_clear_image, game_clear_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 