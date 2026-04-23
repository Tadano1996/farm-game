import pygame
from player import Player
from field_manager import FieldManager
from ui import UI
from cooking_manager import CookingManager

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("農業＋料理ゲーム")

player = Player()
field_manager = FieldManager()
ui = UI()
cooking = CookingManager()

money = 100
inventory = {"カブ": 0, "トマト": 0, "ナス": 0}
dishes = {"カブサラダ": 0, "トマトサラダ": 0, "ナスサラダ": 0}

current_type_index = 0
game_state = "farm"

shipping_box_rect = pygame.Rect(700, 500, 80, 80)

clock = pygame.time.Clock()
running = True

while running:
    player_rect = player.get_rect()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "farm":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_state = "cooking"

                if event.key == pygame.K_1: current_type_index = 0
                if event.key == pygame.K_2: current_type_index = 1
                if event.key == pygame.K_3: current_type_index = 2

                if event.key == pygame.K_SPACE:
                    money = field_manager.plant(player, current_type_index, money)

                if event.key == pygame.K_RETURN:
                    if player_rect.colliderect(shipping_box_rect):
                        veg = ["カブ", "トマト", "ナス"][current_type_index]
                        if inventory[veg] > 0:
                            inventory[veg] -= 1
                            money += 50
                        dish = veg + "サラダ"
                        if dishes[dish] > 0:
                            dishes[dish] -= 1
                            money += 200
                    else:
                        field_manager.harvest(player, inventory)

        elif game_state == "cooking":
            result = cooking.handle_event(event, inventory, dishes)
            if result == "exit":
                game_state = "farm"

    if game_state == "farm":
        player.handle_movement()

    screen.fill((150, 200, 100))

    if game_state == "farm":
        field_manager.draw(screen)
        pygame.draw.rect(screen, (139, 69, 19), shipping_box_rect)
        screen.blit(ui.font.render("出荷箱", True, (255,255,255)), (705,530))
        player.draw(screen)
        ui.draw(screen, money, inventory, current_type_index, player_rect, shipping_box_rect)

    elif game_state == "cooking":
        cooking.draw(screen)

    pygame.display.flip()
    clock.tick(60)
