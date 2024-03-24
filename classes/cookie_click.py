import pygame


class CookieClick:
    def __init__(self, font):
        self.cookies_count = 0
        self.cookies_per_click_multipler = 1
        self.cookies_per_click = 1 * self.cookies_per_click_multipler
        self.active_texts = []
        self.font = font

    def add_active_text(self, pos_x, pos_y):
        click_text = self.font.render(f"+ {self.cookies_per_click}", True, (0, 0, 0))
        self.active_texts.append({
            'text': click_text,
            'pos_y': pos_y,
            'pos_x': pos_x,
            'timer': pygame.time.get_ticks()
        })

    def update_active_texts(self, WINDOW):
        for idx, active_text in enumerate(self.active_texts):
            WINDOW.blit(active_text['text'],
                        (active_text['pos_x'] - active_text['text'].get_width() / 2, active_text['pos_y'] / 3 + 200))

            if active_text['pos_y'] > -1500:
                active_text['pos_y'] -= 5

            if pygame.time.get_ticks() - active_text['timer'] > 1000:
                del self.active_texts[idx]

    def handle_click(self, mouse_pos):
        self.cookies_count += self.cookies_per_click
        self.add_active_text(mouse_pos[0], mouse_pos[1])
