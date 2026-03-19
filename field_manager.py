import pygame
import time

VEGETABLE_TYPES = [
    {"name": "カブ", "color": (255, 255, 255), "buy": 10, "sell": 25, "time": 5},
    {"name": "トマト", "color": (255, 50, 50), "buy": 50, "sell": 150, "time": 10},
    {"name": "ナス", "color": (150, 50, 200), "buy": 100, "sell": 450, "time": 30}
]

TILE_SIZE = 50

class FieldManager:
    def __init__(self):
        self.fields = []

    def plant(self, player, current_type_index, money):
        center_x = player.pos[0] + player.size//2
        center_y = player.pos[1] + player.size//2
        grid_x = (center_x // TILE_SIZE) * TILE_SIZE
        grid_y = (center_y // TILE_SIZE) * TILE_SIZE

        target_field = next((f for f in self.fields if f[0] == grid_x and f[1] == grid_y), None)
        if not target_field:
            veg = VEGETABLE_TYPES[current_type_index]
            if money >= veg["buy"]:
                money -= veg["buy"]
                self.fields.append([grid_x, grid_y, time.time(), current_type_index])
        return money

    def harvest(self, player, inventory):
        center_x = player.pos[0] + player.size//2
        center_y = player.pos[1] + player.size//2
        grid_x = (center_x // TILE_SIZE) * TILE_SIZE
        grid_y = (center_y // TILE_SIZE) * TILE_SIZE

        target_field = next((f for f in self.fields if f[0] == grid_x and f[1] == grid_y), None)
        if target_field:
            veg = VEGETABLE_TYPES[target_field[3]]
            if time.time() - target_field[2] >= veg["time"]:
                inventory[veg["name"]] += 1
                self.fields.remove(target_field)

    def draw(self, screen):
        current_time = time.time()
        for f in self.fields:
            elapsed = current_time - f[2]
            veg_info = VEGETABLE_TYPES[f[3]]
            pygame.draw.rect(screen, (100, 70, 20), (f[0], f[1], TILE_SIZE, TILE_SIZE))
            if elapsed >= veg_info["time"]:
                pygame.draw.circle(screen, veg_info["color"], (f[0] + 25, f[1] + 25), 18)
            elif elapsed >= veg_info["time"] * 0.66:
                pygame.draw.circle(screen, (34, 139, 34), (f[0] + 25, f[1] + 25), 12)
            elif elapsed >= veg_info["time"] * 0.33:
                pygame.draw.circle(screen, (124, 252, 0), (f[0] + 25, f[1] + 25), 6)