import pygame
from classes.cookie_click import CookieClick
from classes.upgrade_cookie_click import UpgradeCookieClick
from classes.autoclick import Autoclick
from classes.business import Grandma, Owen, Kiln, Bakery, SweetShop, Donut, Cake, Cracker, SuperCake, GoldCake


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music/soundtrack.mp3')
pygame.mixer.music.play(-1)
click_sound = pygame.mixer.Sound('music/crunch.4.ogg')

WIDTH, HEIGHT = 1200, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 105, 180)
RED = (255, 0, 0)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Základní okno Pygame")
BACKGROUND = pygame.transform.scale(pygame.image.load("images/bg.png"), (WIDTH, HEIGHT))
COOKIE = pygame.transform.scale(pygame.image.load("images/cookie.png"), (200, 200))
COOKE_LOGO = pygame.transform.scale(pygame.image.load("images/sweet1.png"), (1000, 300))

font = pygame.font.Font(None, 70)
click_font = pygame.font.Font(None, 40)
button_font = pygame.font.Font(None, 35)

cookie_clicker = CookieClick(click_font)
upgrade_cookie_click = UpgradeCookieClick(WIDTH, HEIGHT, button_font, BLACK, PINK)

clock = pygame.time.Clock()

autoclick_obj = Autoclick(5000, cookie_clicker.handle_click, 20)


def draw_business_line(window, business, x_button_position, x_business_count_position, x_business_text_position,
                       x_price_text_position, y_position, cookies_count):
    business_button = pygame.Rect(x_button_position, y_position, 150, 40)

    if business.count == 0:
        if cookies_count >= business.base_price:
            pygame.draw.rect(window, PINK, business_button)
            pygame.draw.rect(window, BLACK, business_button, 3)
        else:
            pygame.draw.rect(window, RED, business_button)
            pygame.draw.rect(window, BLACK, business_button, 3)
    else:
        if cookies_count >= business.base_price * (business.count * business.multiplier) or business.count == 0:
            pygame.draw.rect(window, PINK, business_button)
            pygame.draw.rect(window, BLACK, business_button, 3)
        else:
            pygame.draw.rect(window, RED, business_button)
            pygame.draw.rect(window, BLACK, business_button, 3)

    if business.count == 0:
        price_text = button_font.render(
            f"{business.base_price} cookies", True, BLACK)
    else:
        price_text = button_font.render(f"{business.base_price * (business.count * business.multiplier)} cookies", True,
                                        BLACK)

    business_text = button_font.render(f"{business.name}", True, BLACK)

    business_count = button_font.render(f"{business.count} X", True, BLACK)
    window.blit(business_count, (x_business_count_position, y_position))
    window.blit(price_text, (x_price_text_position, y_position + 5))
    window.blit(business_text, (x_business_text_position, y_position + 5))
    return business_button


def total_cookies_per_second(businesses):
    total_cps = 0
    for business in businesses:
        total_cps += business.calculate_cps()
    return total_cps


grandma = Grandma()
owen = Owen()
kiln = Kiln()
bakery = Bakery()
sweet_shop = SweetShop()
donut = Donut()
cake = Cake()
cracker = Cracker()
super_cake = SuperCake()
gold_cake = GoldCake()

businesses = [grandma, owen, kiln, bakery, sweet_shop, donut, cake, cracker, super_cake, gold_cake]

running = True
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
grandma_button = draw_business_line(WINDOW, grandma, 200, 30, 220, 400, 700, cookie_clicker.cookies_count)
owen_button = draw_business_line(WINDOW, owen, 200, 30, 220, 400, 750, cookie_clicker.cookies_count)
kiln_button = draw_business_line(WINDOW, kiln, 200, 30, 220, 400, 800, cookie_clicker.cookies_count)
bakery_button = draw_business_line(WINDOW, bakery, 200, 30, 220, 400, 850, cookie_clicker.cookies_count)
sweet_shop_button = draw_business_line(WINDOW, sweet_shop, 800, 680, 820, 1000, 600, cookie_clicker.cookies_count)
donut_button = draw_business_line(WINDOW, donut, 800, 680, 820, 1000, 650, cookie_clicker.cookies_count)
cake_button = draw_business_line(WINDOW, cake, 800, 680, 820, 1000, 700, cookie_clicker.cookies_count)
cracker_button = draw_business_line(WINDOW, cracker, 800, 680, 820, 1000, 750, cookie_clicker.cookies_count)
super_cake_button = draw_business_line(WINDOW, super_cake, 800, 680, 820, 1000, 800, cookie_clicker.cookies_count)
gold_cake_button = draw_business_line(WINDOW, gold_cake, 800, 680, 820, 1000, 850, cookie_clicker.cookies_count)

while running:
    total_cps = total_cookies_per_second(businesses)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if grandma_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = grandma.buy_button(cookie_clicker.cookies_count)
            elif owen_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = owen.buy_button(cookie_clicker.cookies_count)
            elif kiln_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = kiln.buy_button(cookie_clicker.cookies_count)
            elif bakery_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = bakery.buy_button(cookie_clicker.cookies_count)
            elif sweet_shop_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = sweet_shop.buy_button(cookie_clicker.cookies_count)
            elif donut_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = donut.buy_button(cookie_clicker.cookies_count)
            elif cake_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = cake.buy_button(cookie_clicker.cookies_count)
            elif cracker_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = cracker.buy_button(cookie_clicker.cookies_count)
            elif super_cake_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = super_cake.buy_button(cookie_clicker.cookies_count)
            elif gold_cake_button.collidepoint(mouse_pos):
                cookie_clicker.cookies_count = gold_cake.buy_button(cookie_clicker.cookies_count)

            elif autoclick_obj.cookie_clickable_space(WIDTH, HEIGHT, COOKIE).collidepoint(mouse_pos):
                cookie_clicker.handle_click(mouse_pos)
                click_sound.play()
            else:
                cookie_clicker.cookies_count, cookie_clicker.cookies_per_click = upgrade_cookie_click.handle_click(
                    mouse_pos, cookie_clicker.cookies_count, cookie_clicker.cookies_per_click)

                if autoclick_obj.price <= cookie_clicker.cookies_count:
                    autoclick_obj.handle_buy(cookie_clicker, WIDTH, HEIGHT, COOKIE)

        elif event.type == pygame.USEREVENT:
            autoclick_obj.autoclick(WIDTH, HEIGHT, COOKIE)

        elif event.type == pygame.USEREVENT +1:
            cookie_clicker.cookies_count += total_cps
            text = font.render(f"COOKIES {cookie_clicker.cookies_count}", True, BLACK)

    text = font.render(f"COOKIES {cookie_clicker.cookies_count}", True, BLACK)
    cps_text = font.render(f"CPS {total_cps}", True, BLACK)
    autoclick_text = button_font.render(f" {Autoclick.autoclick_count} X", True, BLACK)

    WINDOW.blit(BACKGROUND, (0, 0))
    WINDOW.blit(COOKIE, ((WIDTH - COOKIE.get_width()) / 2, HEIGHT / 3))
    WINDOW.blit(COOKE_LOGO, ((WIDTH - COOKE_LOGO.get_width()) / 2, 0))
    WINDOW.blit(text, ((WIDTH - text.get_width()) / 2, 150))
    WINDOW.blit(cps_text, (530, 230))
    WINDOW.blit(autoclick_text, (25, 650))

    draw_business_line(WINDOW, grandma, 200, 30, 220, 400, 700, cookie_clicker.cookies_count)
    draw_business_line(WINDOW, owen, 200, 30, 220, 400, 750, cookie_clicker.cookies_count)
    draw_business_line(WINDOW, kiln, 200, 30, 220, 400, 800, cookie_clicker.cookies_count)
    draw_business_line(WINDOW, bakery, 200, 30, 220, 400, 850, cookie_clicker.cookies_count)
    draw_business_line(WINDOW, sweet_shop, 800, 680, 820, 1000, 600, cookie_clicker.cookies_count)
    draw_business_line(WINDOW, donut, 800, 680, 820, 1000, 650, cookie_clicker.cookies_count)
    draw_business_line(WINDOW, cake, 800, 680, 820, 1000, 700, cookie_clicker.cookies_count)
    draw_business_line(WINDOW, cracker, 800, 680, 820, 1000, 750, cookie_clicker.cookies_count)
    draw_business_line(WINDOW, super_cake, 800, 680, 820, 1000, 800, cookie_clicker.cookies_count)
    draw_business_line(WINDOW, gold_cake, 800, 680, 820, 1000, 850, cookie_clicker.cookies_count)

    autoclick_obj.draw_button(WINDOW, cookie_clicker.cookies_count, WIDTH, HEIGHT, button_font, BLACK, PINK, RED)
    upgrade_cookie_click.draw_button(WINDOW, cookie_clicker.cookies_count)
    upgrade_cookie_click.draw_upgrade_click_text(WINDOW)
    upgrade_cookie_click.draw_upgrade_price(WINDOW)
    upgrade_cookie_click.draw_click_multipler(WINDOW)

    cookie_clicker.update_active_texts(WINDOW)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
