import pygame
import time
from player import Player
from field_manager import FieldManager
from ui import UI

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50

VEGETABLE_TYPES = [
    {"name": "カブ", "color": (255, 255, 255), "buy": 10, "sell": 25, "time": 5},
    {"name": "トマト", "color": (255, 50, 50), "buy": 50, "sell": 150, "time": 10},
    {"name": "ナス", "color": (150, 50, 200), "buy": 100, "sell": 450, "time": 30}
]

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WASD移動 / Spaceで植える / Enterで収穫・売却")

player = Player()
field_manager = FieldManager()
ui = UI()

money = 100
inventory = {"カブ": 0, "トマト": 0, "ナス": 0}
current_type_index = 0

shipping_box_rect = pygame.Rect(700, 500, 80, 80)

clock = pygame.time.Clock()
running = True

while running:
    player_rect = player.get_rect()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: current_type_index = 0
            if event.key == pygame.K_2: current_type_index = 1
            if event.key == pygame.K_3: current_type_index = 2

            if event.key == pygame.K_SPACE:
                money = field_manager.plant(player, current_type_index, money)

            if event.key == pygame.K_RETURN:
                if player_rect.colliderect(shipping_box_rect):
                    veg_name = VEGETABLE_TYPES[current_type_index]["name"]
                    if inventory[veg_name] > 0:
                        inventory[veg_name] -= 1
                        money += VEGETABLE_TYPES[current_type_index]["sell"]
                else:
                    field_manager.harvest(player, inventory) 

    player.handle_movement()

    screen.fill((150, 200, 100))
    field_manager.draw(screen)

    pygame.draw.rect(screen, (139, 69, 19), shipping_box_rect)
    ui.font.render("出荷箱", True, (255, 255, 255))
    screen.blit(ui.font.render("出荷箱", True, (255, 255, 255)), (705, 530))

    player.draw(screen)
    ui.draw(screen, money, inventory, current_type_index, player_rect, shipping_box_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()