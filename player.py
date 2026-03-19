import pygame

WIDTH, HEIGHT = 800, 600

class Player:
    def __init__(self):
        self.pos = [400, 300]
        self.size = 40
        self.speed = 5

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.pos[0] -= self.speed
        if keys[pygame.K_d]: self.pos[0] += self.speed
        if keys[pygame.K_w]: self.pos[1] -= self.speed
        if keys[pygame.K_s]: self.pos[1] += self.speed

        if self.pos[0] < 0: self.pos[0] = 0
        if self.pos[0] > WIDTH - self.size: self.pos[0] = WIDTH - self.size
        if self.pos[1] < 0: self.pos[1] = 0
        if self.pos[1] > HEIGHT - self.size: self.pos[1] = HEIGHT - self.size

    def get_rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, (50, 50, 255), (self.pos[0], self.pos[1], self.size, self.size))