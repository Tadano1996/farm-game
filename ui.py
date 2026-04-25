import pygame

VEGETABLE_TYPES = [
    {"name": "カブ", "color": (255, 255, 255), "buy": 10, "sell": 25, "time": 5},
    {"name": "トマト", "color": (255, 50, 50), "buy": 50, "sell": 150, "time": 10},
    {"name": "ナス", "color": (150, 50, 200), "buy": 100, "sell": 450, "time": 30}
]

class UI:
    def __init__(self):
        self.font = pygame.font.SysFont("msgothic", 24)

    def draw(self, screen, money, inventory, dishes, current_type_index, player_rect, shipping_box_rect):
        screen.blit(self.font.render(f"所持金: {money}円", True, (255, 255, 255)), (20, 20))

        if player_rect.colliderect(shipping_box_rect):
            screen.blit(self.font.render("Enterで選択中の野菜を売却", True, (255, 255, 0)), (450, 470))

        pygame.draw.rect(screen, (0, 0, 0, 100), (580, 10, 200, 150))
        screen.blit(self.font.render(f"選択: {VEGETABLE_TYPES[current_type_index]['name']}", True, (255, 255, 0)), (600, 20))

        y_offset = 60
        for name, count in inventory.items():
            color = (255, 255, 255) if VEGETABLE_TYPES[current_type_index]["name"] != name else (255, 255, 0)
            screen.blit(self.font.render(f"{name}: {count}個", True, color), (600, y_offset))
            y_offset += 30

        # 料理表示
        y_offset += 20
        screen.blit(self.font.render("料理", True, (255,255,0)), (600, y_offset))
        y_offset += 30

        for name, count in dishes.items():
            screen.blit(self.font.render(f"{name}: {count}個", True, (200,255,200)), (600, y_offset))
            y_offset += 30