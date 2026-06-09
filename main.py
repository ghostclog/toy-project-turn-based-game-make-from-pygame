import pygame
import sys

# 1. 파이게임 초기화 (필수)
pygame.init()

# 2. 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("나의 첫 파이게임") # 창 제목

# 3. 프레임 속도(FPS) 설정을 위한 시계 객체 생성
clock = pygame.time.Clock()

# 4. 메인 게임 루프
running = True
while running:
    # ----------------------------------------
    # [1] 이벤트 처리 부분
    # ----------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 우측 상단의 X 버튼을 눌렀을 때
            running = False

    # ----------------------------------------
    # [2] 게임 로직 업데이트 부분
    # ----------------------------------------
    # (예: 플레이어 위치 x += 5 등)

    # ----------------------------------------
    # [3] 화면 그리기 부분
    # ----------------------------------------
    # 화면을 흰색(RGB: 255, 255, 255)으로 지우기
    screen.fill((255, 255, 255)) 
    
    # (여기에 캐릭터나 배경을 그리는 코드가 들어갑니다)

    # 작업한 내용을 실제 화면에 업데이트 (필수)
    pygame.display.flip() 

    # ----------------------------------------
    # 초당 프레임 수(FPS)를 60으로 고정
    clock.tick(60)

# 5. 게임 루프 종료 후 파이게임 종료
pygame.quit()
sys.exit()