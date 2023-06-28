import pygame
from pygame.locals import *

# 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 캐릭터 초기 위치
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

# 캐릭터 이동 속도
player_speed = 5

# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 화면 전체 맵 크기
map_width = 2000
map_height = 2000

# 맵 스크롤 오프셋 초기화
offset_x = 0
offset_y = 0

# 도트 크기와 간격
dot_size = 2
dot_spacing = 10

# 도트 색상
dot_color = (0, 255, 255)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player_y -= player_speed
    if keys[K_DOWN]:
        player_y += player_speed
    if keys[K_LEFT]:
        player_x -= player_speed
    if keys[K_RIGHT]:
        player_x += player_speed

    # 캐릭터 위치 제한
    if player_x < SCREEN_WIDTH // 2:
        player_x = SCREEN_WIDTH // 2
    if player_x > map_width - SCREEN_WIDTH // 2:
        player_x = map_width - SCREEN_WIDTH // 2
    if player_y < SCREEN_HEIGHT // 2:
        player_y = SCREEN_HEIGHT // 2
    if player_y > map_height - SCREEN_HEIGHT // 2:
        player_y = map_height - SCREEN_HEIGHT // 2

    # 맵 스크롤 계산
    offset_x = SCREEN_WIDTH // 2 - player_x
    offset_y = SCREEN_HEIGHT // 2 - player_y

    # 화면 업데이트
    screen.fill((0, 0, 0))  # 검은색 배경

    # 맵 그리기 (실제로는 맵 이미지 등을 사용)
    pygame.draw.rect(screen, (255, 255, 200), (offset_x, offset_y, map_width, map_height))

    # 도트 그리기
    for x in range(offset_x, offset_x + SCREEN_WIDTH, dot_spacing):
        for y in range(offset_y, offset_y + SCREEN_HEIGHT, dot_spacing):
            pygame.draw.circle(screen, dot_color, (x, y), dot_size)

    # 캐릭터 그리기
    pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 30)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()