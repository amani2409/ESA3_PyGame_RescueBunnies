import pygame

from classes.variables import WIDTH, HEIGHT, WHITE
from database import get_user, add_user, show_all_user_highscore


# https://www.makeuseof.com/start-menu-and-game-over-screen-with-pygame/
def draw_startScreen(user_data):
    background = pygame.image.load('Assets/images/start.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))

    pygame.display.set_caption('Start Menu')
    font = pygame.font.SysFont('Arial', 50)
    title = font.render(f'Hallo {user_data['username']}', True, (255, 255, 255))
    highscore = font.render(f'Highscore: {user_data['highscore']}', True, (255, 255, 255))
    all_highscore = font.render('Show all Highscore [h]', True, (255, 255, 255))
    start_button = font.render('Start [s]', True, (255, 255, 255))
    quit_button = font.render('Quit [q]', True, (255, 255, 255))
    screen.blit(background, (0, 0))  # blit wird genutzt um eine Sache auf einen andere Sache/Oberfläche zu zeichnen
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 3 - title.get_height() / 2))
    screen.blit(highscore, (WIDTH / 2 - highscore.get_width() / 2, HEIGHT / highscore.get_height() / 2))
    screen.blit(start_button, (WIDTH / 2 - start_button.get_width() / 2, HEIGHT / 2 - start_button.get_height() / 2))
    screen.blit(all_highscore, (WIDTH / 2 - all_highscore.get_width() / 2, HEIGHT / 2 + start_button.get_height() / 2))
    screen.blit(quit_button, (WIDTH / 2 - quit_button.get_width() / 2, HEIGHT / 4 + start_button.get_height()))
    pygame.display.update()


def draw_highscore_screen():
    background = pygame.image.load('Assets/images/start.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    pygame.display.set_caption('Highscore')
    font = pygame.font.SysFont('Arial', 50)

    all_highscores = show_all_user_highscore()

    dis = 100
    for i, data in enumerate(all_highscores):
        text = f'{i + 1}. {data[0]}: {data[1]}'
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (WIDTH / 2 - text_surface.get_width() / 2, dis))
        dis += 50

    back_button = font.render('Back [b]', True, WHITE)
    back_button_rect = back_button.get_rect(topright=(WIDTH - 10, 10))
    screen.blit(back_button, back_button_rect.topleft)

    pygame.display.update()

def draw_endScreen():
    background = pygame.image.load('Assets/images/lostscene.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))
    pygame.display.set_caption('End Screen')
    font = pygame.font.SysFont('Arial', 50)
    title = font.render('GameOver', True, (255, 255, 255))
    restart_button = font.render('Restart [r]', True, (255, 255, 255))
    home_button = font.render('Home Screen [h]', True, (255, 255, 255))
    quit_button = font.render('Quit [q]', True, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 4 - title.get_height() / 2))
    screen.blit(restart_button,
                (WIDTH / 2 - restart_button.get_width() / 2, HEIGHT / 2 - restart_button.get_height() / 2))
    screen.blit(home_button, (WIDTH / 2 - home_button.get_width() / 2, HEIGHT / 2 + restart_button.get_height()))
    screen.blit(quit_button, (WIDTH / 2 - quit_button.get_width() / 2, HEIGHT / 4 + restart_button.get_height()))
    pygame.display.update()


def draw_nextLevel():
    background = pygame.image.load('Assets/images/background.png')

    screen = pygame.display.get_surface()
    screen.fill((0, 0, 0))

    pygame.display.set_caption('Winning Screen')
    font = pygame.font.SysFont('Arial', 50)
    title = font.render('Won: You made it!', True, (255, 255, 255))
    restart_button = font.render('Restart [r]', True, (255, 255, 255))
    next_button = font.render('next Level [n]', True, (255, 255, 255))
    home_button = font.render('Home Screen [h]', True, (255, 255, 255))
    quit_button = font.render('Quit [q]', True, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGHT / 4 - title.get_height() / 2))
    screen.blit(restart_button,
                (WIDTH / 2 - restart_button.get_width() / 2, HEIGHT / 2 - restart_button.get_height() / 2))
    screen.blit(home_button, (WIDTH / 2 - home_button.get_width() / 2, HEIGHT / 2 + restart_button.get_height()))
    screen.blit(next_button, (WIDTH / 2 - next_button.get_width() / 2, HEIGHT / 4 + restart_button.get_height()))
    screen.blit(quit_button, (WIDTH / 2 - quit_button.get_width() / 2, HEIGHT / 6 + restart_button.get_height()))
    pygame.display.update()


def draw_loginScreen():
    background = pygame.image.load('Assets/images/start.png')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Login')
    font = pygame.font.SysFont('Arial', 50)
    label_font = pygame.font.SysFont('Arial', 30)
    title = font.render('Enter your username and password!', True, WHITE)
    enter_button = font.render('Login [press Enter]!', True, WHITE)
    input_username = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 - 60, 200, 40)
    input_passwort = pygame.Rect(WIDTH / 2 - 100, HEIGHT / 2 + 20, 200, 40)

    username_label = label_font.render('Username:', True, WHITE)
    password_label = label_font.render('Password:', True, WHITE)

    color_active = pygame.Color(255, 255, 255)
    color_inactive = pygame.Color(0, 0, 0)

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
                    active_password = False
                elif input_passwort.collidepoint(event.pos):
                    active_username = False
                    active_password = True
                else:
                    active_username = False
                    active_password = False

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

        draw_username = label_font.render(username, True, WHITE)
        draw_passwort = font.render('*' * len(password), True, WHITE)

        input_username.w = max(200, draw_username.get_width() + 10)
        input_passwort.w = max(200, draw_passwort.get_width() + 10)

        screen.blit(draw_username, (input_username.x + 5, input_username.y + 5))
        screen.blit(draw_passwort, (input_passwort.x + 5, input_passwort.y + 5))

        screen.blit(username_label, (input_username.x, input_username.y - 32))
        screen.blit(password_label, (input_passwort.x, input_passwort.y - 32))

        pygame.draw.rect(screen, WHITE, input_username, 2)
        pygame.draw.rect(screen, WHITE, input_passwort, 2)

        screen.blit(enter_button,
                    (WIDTH / 2 - enter_button.get_width() / 2, input_passwort.y + input_passwort.height + 20))

        if error_message:
            error_label = label_font.render(error_message, True, (255, 0, 0))
            screen.blit(error_label,
                        (WIDTH / 2 - error_label.get_width() / 2, input_passwort.y + input_passwort.height + 70))

        pygame.display.flip()

    return user_data
