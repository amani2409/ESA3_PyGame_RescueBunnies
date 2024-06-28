import pygame

from classes.variables import WIDTH, HEIGHT, WHITE, FONT, FONT_SM
from database import get_user, add_user, show_all_user_highscore


# https://www.makeuseof.com/start-menu-and-game-over-screen-with-pygame/
def draw_startScreen(user_data):
    background = pygame.image.load('Assets/images/start.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))

    pygame.display.set_caption('Start Menu')

    title = FONT.render(f'Hallo {user_data['username']}', True, WHITE)
    title_rect = title.get_rect(center=(WIDTH / 2, HEIGHT / 4))

    highscore = FONT.render(f'Highscore: {user_data['highscore']}', True, WHITE)
    highscore_rect = highscore.get_rect(center=(WIDTH / 2, HEIGHT / 3))

    all_highscore = FONT_SM.render('Show all Highscore [t]', True, WHITE)
    all_highscore_rect = all_highscore.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    start_button = FONT_SM.render('Start [g]', True, WHITE)
    start_button_rect = start_button.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))

    reset_button = FONT_SM.render('Reset [r]', True, WHITE)
    reset_button_rect = reset_button.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 150))

    quit_button = FONT_SM.render('Quit [q]', True, WHITE)
    quit_button_rect = quit_button.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 200))

    screen.blit(background, (0, 0))  # blit wird genutzt um eine Sache auf einen andere Sache/Oberfläche zu zeichnen
    screen.blit(title, title_rect)
    screen.blit(highscore, highscore_rect)
    screen.blit(all_highscore, all_highscore_rect)
    screen.blit(start_button, start_button_rect)
    screen.blit(reset_button, reset_button_rect)
    screen.blit(quit_button, quit_button_rect)
    pygame.display.update()


def draw_highscore_screen():
    background = pygame.image.load('Assets/images/start.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    pygame.display.set_caption('Highscore')
    title = FONT.render('Highscores Top 10', True, WHITE)
    title_rect = title.get_rect(center=(WIDTH / 2, 50))
    screen.blit(title, title_rect)

    all_highscores = show_all_user_highscore()

    dis = 100
    for i, data in enumerate(all_highscores):
        text = f'{i + 1}. {data[0]}: {data[1]}'
        text_surface = FONT_SM.render(text, True, WHITE)
        screen.blit(text_surface, (WIDTH / 2 - text_surface.get_width() / 2, dis))
        dis += 50

    back_button = FONT_SM.render('Back [b]', True, WHITE)
    back_button_rect = back_button.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(back_button, back_button_rect.topleft)

    pygame.display.update()


def draw_endScreen():
    background = pygame.image.load('Assets/images/lostscene.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))

    pygame.display.set_caption('End Screen')

    title = FONT.render('GameOver', True, WHITE)
    title_rect = title.get_rect(center=(WIDTH / 2, HEIGHT / 4))

    restart_button = FONT_SM.render('Restart [r]', True, WHITE)
    restart_button_rect = restart_button.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    home_button = FONT_SM.render('Home Screen [h]', True, WHITE)
    home_button_rect = home_button.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))

    quit_button = FONT_SM.render('Quit [q]', True, WHITE)
    quit_button_rect = quit_button.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 150))

    screen.blit(background, (0, 0))
    screen.blit(title, title_rect)
    screen.blit(restart_button, restart_button_rect)
    screen.blit(home_button, home_button_rect)
    screen.blit(quit_button, quit_button_rect)
    pygame.display.update()


def draw_nextLevel():
    background = pygame.image.load('Assets/images/background.png')

    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))

    pygame.display.set_caption('Winning Screen')
    title = FONT.render('Won: You made it!', True, WHITE)
    title_rect = title.get_rect(center=(WIDTH / 2, HEIGHT / 4))

    next_button = FONT_SM.render('next Level [n]', True, WHITE)
    next_button_rect = next_button.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    home_button = FONT_SM.render('Home Screen [h]', True, WHITE)
    home_button_rect = home_button.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))

    quit_button = FONT_SM.render('Quit [q]', True, WHITE)
    quit_button_rect = quit_button.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 150))

    screen.blit(background, (0, 0))
    screen.blit(title, title_rect)
    screen.blit(next_button, next_button_rect)
    screen.blit(home_button, home_button_rect)
    screen.blit(quit_button, quit_button_rect)
    pygame.display.update()


def draw_loginScreen():
    background = pygame.image.load('Assets/images/start.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Login')
    title = FONT.render('Enter your username and password!', True, WHITE)
    enter_button = FONT.render('Login [press Enter]!', True, WHITE)
    input_username = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 - 60, 200, 40)
    input_passwort = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 20, 200, 40)

    username_label = FONT_SM.render('Username:', True, WHITE)
    password_label = FONT_SM.render('Password:', True, WHITE)

    color_active = pygame.Color(30, 160, 15)
    color_inactive = pygame.Color(255, 255, 255)

    color_user = color_inactive
    color_pw = color_inactive

    active_username = False
    active_password = False

    username = ''
    password = ''
    user_data = None
    error_message = ''

    running = True
    # https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_username.collidepoint(event.pos):
                    active_username = True
                    color_user = color_active
                    active_password = False
                    color_pw = color_inactive

                elif input_passwort.collidepoint(event.pos):
                    active_username = False
                    color_user = color_inactive
                    active_password = True
                    color_pw = color_active
                else:
                    active_username = False
                    color_user = color_inactive
                    active_password = False
                    color_pw = color_inactive

            if event.type == pygame.KEYDOWN:
                if active_username:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active_password:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode
                    if event.key == pygame.K_RETURN:
                        user_data = get_user(username, password)
                        if user_data:
                            if user_data['password'] == password:
                                running = False
                        else:
                            add_user(username, password)
                            user_data = get_user(username, password)
                            if user_data:
                                running = False
                            else:
                                error_message = f'Password is incorrect for user {username}'
                                username = ''
                                password = ''

        screen.fill((30, 30, 30))
        screen.blit(background, (0, 0))
        screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 4 - title.get_height() / 2))

        draw_username = FONT_SM.render(username, True, WHITE)
        draw_passwort = FONT.render('*' * len(password), True, WHITE)

        input_username.w = max(200, draw_username.get_width() + 10)
        input_passwort.w = max(200, draw_passwort.get_width() + 10)

        screen.blit(draw_username, (input_username.x + 5, input_username.y + 5))
        screen.blit(draw_passwort, (input_passwort.x + 5, input_passwort.y + 5))

        screen.blit(username_label, (input_username.x, input_username.y - 32))
        screen.blit(password_label, (input_passwort.x, input_passwort.y - 32))

        pygame.draw.rect(screen, color_user, input_username, 2)
        pygame.draw.rect(screen, color_pw, input_passwort, 2)

        screen.blit(enter_button,
                    (WIDTH / 2 - enter_button.get_width() / 2, input_passwort.y + input_passwort.height + 20))

        if error_message:
            error_label = FONT_SM.render(error_message, True, (255, 0, 0))
            screen.blit(error_label,
                        (WIDTH / 2 - error_label.get_width() / 2, input_passwort.y + input_passwort.height + 70))

        pygame.display.flip()

    return user_data


def draw_gamecompleted_screen():
    background = pygame.image.load('Assets/images/start.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))

    pygame.display.set_caption('Game Completed')

    title = FONT.render('You finished.', True, WHITE)
    title_rect = title.get_rect(center=(WIDTH / 2, HEIGHT / 4))
    title2 = FONT.render('Do you want to resett all and restart?', True, WHITE)
    title2_rect = title2.get_rect(center=(WIDTH / 2, HEIGHT / 3))

    restart_button = FONT_SM.render('Reset highscore and Restart [r]', True, WHITE)
    restart_button_rect = restart_button.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    home_button = FONT_SM.render('Home Screen [h]', True, WHITE)
    home_button_rect = home_button.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))

    quit_button = FONT_SM.render('Quit [q]', True, WHITE)
    quit_button_rect = quit_button.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 150))

    screen.blit(background, (0, 0))
    screen.blit(title, title_rect)
    screen.blit(title2, title2_rect)
    screen.blit(restart_button, restart_button_rect)
    screen.blit(home_button, home_button_rect)
    screen.blit(quit_button, quit_button_rect)
    pygame.display.update()
