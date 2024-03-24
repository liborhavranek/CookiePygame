import pygame


class UpgradeCookieClick:
    def __init__(self, WIDTH, HEIGHT, button_font, BLACK, PINK):
        self.click_button = pygame.Rect(200, 600, 150, 40)
        self.click_button_active = True
        self.click_button_price = 10
        self.button_font = button_font
        self.click_button_text = button_font.render("Click x2", True, BLACK)
        self.click_button_price_text = button_font.render(f"{self.click_button_price} cookies", True, BLACK)
        self.BLACK = BLACK
        self.PINK = PINK
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.RED = (255, 0, 0)
        self.upgrade_click_text = button_font.render(f"Vylepšení", True, BLACK)
        self.cookies_per_click = 1
        self.click_multipler_text = button_font.render(f"{self.cookies_per_click} X", True, BLACK)

    def handle_click(self, mouse_pos, cookies_count, cookies_per_click):
        if self.click_button.collidepoint(mouse_pos) and cookies_count >= self.click_button_price:
            cookies_count -= self.click_button_price
            self.click_button_price *= 5
            cookies_per_click *= 2
            self.click_button_price_text = self.button_font.render(f"{self.click_button_price} cookies", True,
                                                                   self.BLACK)
            self.click_multipler_text = self.button_font.render(f"{cookies_per_click} X", True, self.BLACK)
        return cookies_count, cookies_per_click

    def draw_button(self, WINDOW, cookies_count):
        if not self.is_maxed_out() and cookies_count >= self.click_button_price:
            pygame.draw.rect(WINDOW, self.PINK, self.click_button)
            pygame.draw.rect(WINDOW, self.BLACK, self.click_button, 3)  # Ohraničení
            WINDOW.blit(self.click_button_text, (220, 610))
        else:
            pygame.draw.rect(WINDOW, self.RED, self.click_button)
            pygame.draw.rect(WINDOW, self.BLACK, self.click_button, 3)  # Ohraničení
            if self.click_button_active:
                text = self.button_font.render("Click x2", True, self.BLACK)
            else:
                text = self.button_font.render("Maximálně upgradováno", True, self.BLACK)
            WINDOW.blit(text, (220, 610))

    def draw_upgrade_click_text(self, WINDOW):
        WINDOW.blit(self.upgrade_click_text, (550, 550))

    def is_maxed_out(self):
        return not self.click_button_active

    def draw_upgrade_price(self, WINDOW):
        WINDOW.blit(self.click_button_price_text, (400, 610))

    def draw_click_multipler(self, WINDOW):
        WINDOW.blit(self.click_multipler_text, (30, 610))
