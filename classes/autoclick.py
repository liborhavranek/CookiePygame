import pygame
import random

pygame.mixer.init()
click_sound = pygame.mixer.Sound('music/crunch.4.ogg')


class Autoclick:
    autoclick_count = 0

    def __init__(self, click_speed, click_function, price):
        self.click_speed = click_speed
        self.click_function = click_function
        self.autoclick_speed = 5000
        self.price = price

    def cookie_clickable_space(self, WIDTH, HEIGHT, COOKIE):
        cookie_rect = COOKIE.get_rect(center=((WIDTH - COOKIE.get_width() + 200) // 2, (HEIGHT // 3) + 100))
        return cookie_rect

    def autoclick(self, WIDTH, HEIGHT, COOKIE):
        x = random.randint(self.cookie_clickable_space(WIDTH, HEIGHT, COOKIE).left, self.cookie_clickable_space(WIDTH, HEIGHT, COOKIE).right)
        y = random.randint(self.cookie_clickable_space(WIDTH, HEIGHT, COOKIE).top, self.cookie_clickable_space(WIDTH, HEIGHT, COOKIE).bottom)
        mouse_pos = (x, y)
        self.click_function(mouse_pos)
        click_sound.play()
        pygame.time.set_timer(pygame.USEREVENT, self.click_speed)

    def draw_button(self, WINDOW, cookies_count, WIDTH, HEIGHT, button_font, BLACK, PINK, RED):
        buy_button = pygame.Rect(200, 650, 150, 40)
        if cookies_count >= self.price:
            pygame.draw.rect(WINDOW, PINK, buy_button)
            pygame.draw.rect(WINDOW, BLACK, buy_button, 3)
        else:
            pygame.draw.rect(WINDOW, RED, buy_button)
            pygame.draw.rect(WINDOW, BLACK, buy_button, 3)
        buy_text = button_font.render(f"Autoclick", True, BLACK)
        WINDOW.blit(buy_text, (220, 660))
        autoclick_price_text = button_font.render(f"{self.price} cookies", True, BLACK)
        WINDOW.blit(autoclick_price_text, (400, 660))

    def handle_buy(self, cookie_clicker, WIDTH, HEIGHT, COOKIE):
        if cookie_clicker.cookies_count >= self.price:
            cookie_clicker.cookies_count -= self.price
            Autoclick.autoclick_count += 1
            autoclick_speed = 5000 // (2 * Autoclick.autoclick_count)
            self.click_speed = autoclick_speed
            self.price *= 5
            self.autoclick(WIDTH, HEIGHT, COOKIE)
