import pygame
import random

VEG_NAMES = ["カブ", "トマト", "ナス"]

class CookingManager:
    def __init__(self):
        self.font = pygame.font.SysFont("msgothic", 30)
        self.active = False
        self.current = 0
        self.bar_pos = 0
        self.bar_speed = 5
        self.target = random.randint(100, 500)
        self.result = ""

    def start(self):
        self.active = True
        self.bar_pos = 0
        self.target = random.randint(100, 500)
        self.result = ""

    def handle_event(self, event, inventory, dishes):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "exit"
            
            if event.key == pygame.K_1:
                if inventory["カブ"] > 0:
                    self.current = 0
                    self.start()

            if event.key == pygame.K_2:
                if inventory["トマト"] > 0:
                    self.current = 1
                    self.start()

            if event.key == pygame.K_3:
                if inventory["ナス"] > 0:
                    self.current = 2
                    self.start()

            if event.key == pygame.K_SPACE and self.active:
                veg = VEG_NAMES[self.current]

                inventory[veg] -= 1

                # 成功判定
                if abs(self.bar_pos - self.target) < 30:
                    dishes[veg + "サラダ"] += 1
                    self.result = "成功！"
                else:
                    self.result = "失敗..."                

                self.active = False

    def draw(self, screen):
        screen.fill((50, 50, 50))

        screen.blit(self.font.render("料理画面（ESCで戻る）", True, (255,255,255)), (200, 50))
        screen.blit(self.font.render("1〜3で食材選択 → SPACEでタイミング", True, (255,255,255)), (120, 100))

        # ↓↓↓ バーはこっち ↓↓↓
        if self.active:
            self.bar_pos += self.bar_speed
            if self.bar_pos > 600:
                self.bar_pos = 0

            # バー
            pygame.draw.rect(screen, (255,255,255), (100,300,600,20))

            # 成功ゾーン
            pygame.draw.rect(screen, (0,255,0), (100+self.target, 300, 30, 20))

            # 動くバー
            pygame.draw.rect(screen, (255,0,0), (100+self.bar_pos, 300, 10, 20))

        # ↓↓↓ 結果表示は外 ↓↓↓
        if self.result:
            screen.blit(self.font.render(self.result, True, (255,255,0)), (300, 200))