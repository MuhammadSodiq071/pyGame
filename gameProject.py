import pygame as game

game.init()

screen = game.display.set_mode((1224, 764))
game.display.set_caption('Game')
game.display.set_icon(game.image.load('images/player/player_icon.png').convert_alpha())
time = game.time.Clock()

start_text = game.font.Font('fonts/Tiny5-Regular.ttf', 80)
start_text = start_text.render('Start the Game', False, 'White')
start_text_poz = start_text.get_rect(center=(612, 330))
start_button = game.Surface((580, 80))
start_button.fill((193, 196, 199))
start_button_rect = start_button.get_rect(topleft=(320, 280))
start_button_poz = start_button.get_rect(center=(612, 330))
start_button_border = game.Surface((590, 90))
start_button_border.fill('Black')
start_button_border_poz = start_button_border.get_rect(center=(612, 330))

settings_text = game.font.Font('fonts/Tiny5-Regular.ttf', 80)
settings_text = settings_text.render('Settings', False, 'White')
settings_text_poz = start_text.get_rect(center=(720, 450))
settings_button = game.Surface((580, 80))
settings_button.fill((193, 196, 199))
settings_button_rect = settings_button.get_rect(topleft=(320, 410))
settings_button_poz = settings_button.get_rect(center=(612, 450))
settings_button_border = game.Surface((590, 90))
settings_button_border.fill('Black')
settings_button_border_poz = settings_button_border.get_rect(center=(612, 450))

bg = game.image.load('../../GUI/bg.jpg').convert()
bg = game.transform.scale(bg, (bg.get_width() * 2, bg.get_height() * 2))
bgx = 0

menu_music = game.mixer.Sound('sounds/super_mario_music.ogg')
menu_music.set_volume(0.5)

music = game.mixer.Sound('sounds/super_mario.mp3')
music.set_volume(0.5)

click = game.mixer.Sound('sounds/minecraft_click.ogg')

lost_bg = game.image.load('images/lost_bg.jpg').convert()
lost_bg = game.transform.scale(lost_bg, (lost_bg.get_width() * 2, lost_bg.get_height() * 2))

lose_text = game.font.Font('fonts/Tiny5-Regular.ttf', 80)
lose_text = lose_text.render('You have lost!', False, (193, 196, 199))
lose_text_poz = lose_text.get_rect(center=(612, 220))

restart_text = game.font.Font('fonts/Tiny5-Regular.ttf', 70)
restart_text = restart_text.render('Play again', False, 'White')
restart_text_poz = restart_text.get_rect(center=(612, 330))
restart_button = game.Surface((480, 80))
restart_button_rect = restart_button.get_rect(topleft=(372, 290))
restart_button.fill((193, 196, 199))
restart_button_poz = restart_button.get_rect(center=(612, 330))
restart_button_border = game.Surface((490, 90))
restart_button_border.fill('Black')
restart_button_border_poz = restart_button_border.get_rect(center=(612, 330))

menu_text = game.font.Font('fonts/Tiny5-Regular.ttf', 70)
menu_text = menu_text.render('Main menu', False, 'White')
menu_text_poz = menu_text.get_rect(center=(612, 500))
menu_button = game.Surface((480, 80))
menu_button_rect = menu_button.get_rect(topleft=(372, 460))
menu_button.fill((193, 196, 199))
menu_button_poz = menu_button.get_rect(center=(612, 500))
menu_button_border = game.Surface((490, 90))
menu_button_border.fill('Black')
menu_button_border_poz = menu_button_border.get_rect(center=(612, 500))

lost_music = game.mixer.Sound('sounds/mario_lost.mp3')
lost_music.set_volume(0.5)

player_walk_right = [
    game.image.load('images/player/player_right_1.png').convert_alpha(),
    game.image.load('images/player/player_right_2.png').convert_alpha(),
    game.image.load('images/player/player_right_3.png').convert_alpha(),
    game.image.load('images/player/player_right_4.png').convert_alpha(),
]
player_walk_left = [
    game.image.load('images/player/player_left_1.png').convert_alpha(),
    game.image.load('images/player/player_left_2.png').convert_alpha(),
    game.image.load('images/player/player_left_3.png').convert_alpha(),
    game.image.load('images/player/player_left_4.png').convert_alpha(),
]
player_anim_count = 0
player_speed = 20
player_x = 200
player_y = 503
jumping = False
jump_count = 8

fox = game.image.load('images/fox/fox_left_1.png').convert_alpha()
fox_timer = game.USEREVENT + 1
game.time.set_timer(fox_timer, 5000)
fox_list_in_game = []

bullet = game.image.load('images/bullet.png').convert_alpha()
bullets = []

bullet_sound = game.mixer.Sound('sounds/bullet.mp3')
bullet_sound.set_volume(1)

gameplay = 0
if gameplay == 0:
    menu_music.play(-1)

bullets_left = 10
running = True
while running:
    if gameplay == 0:
        screen.blit(bg, (bgx, 0))
        screen.blit(start_button, start_button_poz)
        screen.blit(start_text, start_text_poz)
        screen.blit(settings_button, settings_button_poz)
        screen.blit(settings_text, settings_text_poz)
        mouse = game.mouse.get_pos()
        keys = game.key.get_pressed()

        if settings_button_rect.collidepoint(mouse):
            screen.blit(settings_button_border, settings_button_border_poz)
            screen.blit(settings_button, settings_button_poz)
            screen.blit(settings_text, settings_text_poz)

        if start_button_rect.collidepoint(mouse) and game.mouse.get_pressed()[0] or keys[game.K_SPACE] or keys[game.K_KP_ENTER]:
            screen.blit(start_button_border, start_button_border_poz)
            screen.blit(start_button, start_button_poz)
            screen.blit(start_text, start_text_poz)
            click.play()
            gameplay = 2
            menu_music.stop()
            music.play(-1)

        if restart_button_rect.collidepoint(mouse):
            screen.blit(start_button_border, start_button_border_poz)
            screen.blit(start_button, start_button_poz)
            screen.blit(start_text, start_text_poz)

    if gameplay == 2:
        screen.blit(bg, (bgx, 0))
        screen.blit(bg, (bgx + 1224, 0))

        bgx -= 9
        if bgx == -1224:
            bgx = 0

        player_rect = player_walk_right[0].get_rect(topleft=(player_x - 20, player_y))

        # Foxes' going:
        if fox_list_in_game:
            for (i, el) in enumerate(fox_list_in_game):
                screen.blit(fox, el)
                el.x -= 15

                if el.x < -5:
                    fox_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = 1
                    lost_music.play()

        keys = game.key.get_pressed()

        # Player's walking:
        if keys[game.K_LEFT] or keys[game.K_a]:
            screen.blit(player_walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(player_walk_right[player_anim_count], (player_x, player_y))

        if keys[game.K_LEFT] and player_x > 30 or keys[game.K_a] and player_x > 30:
            player_x -= player_speed
        elif keys[game.K_RIGHT] and player_x < 1110 or keys[game.K_d] and player_x < 1110:
            player_x += player_speed

        if player_anim_count == 1:
            player_anim_count = 0
        else:
            player_anim_count += 1

        # Player's jumping:
        if not jumping:
            if keys[game.K_SPACE] or keys[game.K_w] or keys[game.K_UP]:
                jumping = True
        else:
            if jump_count >= -8 and not keys[game.K_s] or keys[game.K_DOWN] or keys[game.KMOD_SHIFT]:
                if jump_count > 0:
                    player_y -= jump_count ** 2 / 2
                else:
                    player_y += jump_count ** 2 / 2

                jump_count -= 1

            else:
                jumping = False
                jump_count = 8

        if keys[game.K_s] or keys[game.K_DOWN]:
            player_y = 503

        # Bullet's going:
        if bullets:
            for (index, element) in enumerate(bullets):
                screen.blit(bullet, (element.x + 45, element.y))
                element.x += 50

                if element.x > 1235 and bullets != 0:
                    bullets.pop(index)

                if fox_list_in_game:
                    for (i, el) in enumerate(fox_list_in_game):
                        if element.colliderect(el):
                            fox_list_in_game.pop(i)
                            bullets.pop(index)

    elif gameplay == 1:
        music.stop()
        screen.blit(lost_bg, (0, 0))
        screen.blit(lose_text, lose_text_poz)
        screen.blit(restart_button, restart_button_poz)
        screen.blit(restart_text, restart_text_poz)
        screen.blit(menu_button, menu_button_poz)
        screen.blit(menu_text, menu_text_poz)
        bullets_left = 0
        mouse = game.mouse.get_pos()
        keys = game.key.get_pressed()

        if restart_button_rect.collidepoint(mouse):
            screen.blit(restart_button_border, restart_button_border_poz)
            screen.blit(restart_button, restart_button_poz)
            screen.blit(restart_text, restart_text_poz)

        if menu_button_rect.collidepoint(mouse):
            screen.blit(menu_button_border, menu_button_border_poz)
            screen.blit(menu_button, menu_button_poz)
            screen.blit(menu_text, menu_text_poz)

        if restart_button_rect.collidepoint(mouse) and game.mouse.get_pressed()[0] or keys[game.K_SPACE] or keys[game.K_KP_ENTER]:
            screen.blit(restart_button_border, restart_button_border_poz)
            screen.blit(restart_button, restart_button_poz)
            screen.blit(restart_text, restart_text_poz)
            gameplay = 2
            player_x = 200
            fox_list_in_game.clear()
            bullets.clear()
            bullets_left = 10
            lost_music.stop()
            click.play()
            music.play(-1)

        if menu_button_rect.collidepoint(mouse) and game.mouse.get_pressed()[0] or keys[game.K_ESCAPE]:
            screen.blit(menu_button_border, menu_button_border_poz)
            screen.blit(menu_button, menu_button_poz)
            screen.blit(menu_text, menu_text_poz)
            gameplay = 0
            bgx = 0
            screen.blit(bg, (bgx, 0))
            player_x = 200
            fox_list_in_game.clear()
            bullets.clear()
            bullets_left = 10
            lost_music.stop()
            click.play()
            menu_music.play(-1)

    game.display.update()
    time.tick(8)

    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
            game.quit()

        elif event.type == fox_timer:
            fox_list_in_game.append(fox.get_rect(topleft=(1225, 568)))

        if gameplay and event.type == game.KEYUP and event.key == game.K_e and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 77)))
            bullets_left -= 1
            bullet_sound.play()
