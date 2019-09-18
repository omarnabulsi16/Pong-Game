import sys, pygame
from time import sleep

# function to move paddles down when down arrow key is clicked
def check_keydown_events(event, midpaddle1, toppaddle1, bottompaddle1):
    if event.key == pygame.K_LEFT:
        toppaddle1.moving_left = True
        bottompaddle1.moving_left = True
    elif event.key == pygame.K_RIGHT:
        toppaddle1.moving_right = True
        bottompaddle1.moving_right = True
    elif event.key == pygame.K_UP:
        midpaddle1.moving_up = True
    elif event.key == pygame.K_DOWN:
        midpaddle1.moving_down = True

# function to move paddles up when up arrow key is clicked
def check_keyup_events(event, midpaddle1, toppaddle1, bottompaddle1):
    if event.key == pygame.K_LEFT:
        toppaddle1.moving_left = False
        bottompaddle1.moving_left = False
    elif event.key == pygame.K_RIGHT:
        toppaddle1.moving_right = False
        bottompaddle1.moving_right = False
    elif event.key == pygame.K_UP:
        midpaddle1.moving_up = False
    elif event.key == pygame.K_DOWN:
        midpaddle1.moving_down = False

# function to check if user has clicked the x button to quit the game and check mouse clicks
def check_events(settings, play_button, midpaddle1, toppaddle1, bottompaddle1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, midpaddle1, toppaddle1, bottompaddle1)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, midpaddle1, toppaddle1, bottompaddle1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, play_button, mouse_x, mouse_y)

# function to see if the play button was clicked
def check_play_button(settings, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        settings.game_start = True

# function to update location of paddles and ball accordingly
def update_game(settings, ball, midpaddle1, toppaddle1, bottompaddle1, midpaddle2, toppaddle2, bottompaddle2):
    check_vertical_paddle_collision(settings, ball, midpaddle1, midpaddle2)
    check_horizontal_paddle_collision(settings, ball, toppaddle1, bottompaddle1, toppaddle2, bottompaddle2)
    ball.update()
    midpaddle1.update()
    toppaddle1.update()
    bottompaddle1.update()
    midpaddle2.update()
    toppaddle2.update()
    bottompaddle2.update()

# function to update scores on screen once the player or computer scores
def update_screen(screen, settings, ball, midpaddle1, toppaddle1, bottompaddle1, midpaddle2, toppaddle2, bottompaddle2,
                  score1, score2):
    screen.fill(settings.bg_color)
    pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(ball.screen_rect.centerx, 0, 1, settings.screen_height))
    score1.draw()
    score2.draw()
    midpaddle1.draw()
    toppaddle1.draw()
    bottompaddle1.draw()
    midpaddle2.draw()
    toppaddle2.draw()
    bottompaddle2.draw()
    ball.draw()
    pygame.display.flip()

# function to check if the ball has collided with any vertical paddles
def check_vertical_paddle_collision(settings, ball, midpaddle1, midpaddle2):
    a = pygame.sprite.collide_rect(ball, midpaddle1)
    b = pygame.sprite.collide_rect(ball, midpaddle2)
    if a or b:
        ball.speed *= settings.ball_speedup
        ball.run *= -1
        sound = pygame.mixer.Sound(r"C:\Users\omarn\Desktop\pickup.wav")
        pygame.mixer.music.load(r'C:\Users\omarn\Desktop\pickup.wav')
        pygame.mixer.music.play(1, 0.0)
        musicPlaying = True;

# function to check if the ball has collided with any horizontal paddles
def check_horizontal_paddle_collision(settings, ball, toppaddle1, bottompaddle1, toppaddle2, bottompaddle2):
    a = pygame.sprite.collide_rect(ball, toppaddle1)
    b = pygame.sprite.collide_rect(ball, bottompaddle1)
    c = pygame.sprite.collide_rect(ball, toppaddle2)
    d = pygame.sprite.collide_rect(ball, bottompaddle2)
    if a or b or c or d:
        ball.speed *= settings.ball_speedup
        ball.rise *= -1
        sound = pygame.mixer.Sound(r'C:\Users\omarn\Desktop\pickup.wav')
        pygame.mixer.music.load(r'C:\Users\omarn\Desktop\pickup.wav')
        pygame.mixer.music.play(1, 0.0)
        musicPlaying=True;

# function to increment scores to the side of player that scores on opponent
def check_score(settings, screen, ball, midpaddle1, toppaddle1, bottompaddle1, midpaddle2, toppaddle2, bottompaddle2,
                score1, score2):
    if (ball.rect.right >= ball.screen_rect.right or ball.rect.left <= ball.screen_rect.left
            or ball.rect.bottom >= ball.screen_rect.bottom or ball.rect.top <= ball.screen_rect.top):
        if ball.centerx > ball.screen_rect.centerx:
            score1.points += 1
            score1.prep_msg(str(score1.points))
        else:
            score2.points += 1
            score2.prep_msg(str(score2.points))
        settings.initialize_dynamic_settings()
        ball.reset_ball(settings)
        midpaddle1.center_paddle()
        toppaddle1.center_paddle()
        bottompaddle1.center_paddle()
        midpaddle2.center_paddle()
        toppaddle2.center_paddle()
        bottompaddle2.center_paddle()
        update_screen(screen, settings, ball, midpaddle1, toppaddle1, bottompaddle1, midpaddle2, toppaddle2,
                      bottompaddle2, score1, score2)

        # delays ball entering screen after someone scores
        sleep(3)

# function to make the computer move paddles by tracking the ball
def ai_directives(ball, midpaddle2, toppaddle2, bottompaddle2):
    if ball.rect.center < ball.screen_rect.center:
        if midpaddle2.rect.centery > midpaddle2.screen_rect.centery:
            midpaddle2.moving_up = True
        else:
            midpaddle2.moving_up = False
        if midpaddle2.rect.centery < midpaddle2.screen_rect.centery:
            midpaddle2.moving_down = True
        else:
            midpaddle2.moving_down = False
        if toppaddle2.rect.centerx < toppaddle2.screen_rect.centerx * 1.5:
            toppaddle2.moving_right = True
            bottompaddle2.moving_right = True
        else:
            toppaddle2.moving_right = False
            bottompaddle2.moving_right = False
        if toppaddle2.rect.centerx > toppaddle2.screen_rect.centerx * 1.5:
            toppaddle2.moving_left = True
            bottompaddle2.moving_left = True
        else:
            toppaddle2.moving_left = False
            bottompaddle2.moving_left = False
    else:
        if midpaddle2.rect.centery > ball.rect.centery:
            midpaddle2.moving_up = True
        else:
            midpaddle2.moving_up = False
        if midpaddle2.rect.centery < ball.rect.centery:
            midpaddle2.moving_down = True
        else:
            midpaddle2.moving_down = False
        if toppaddle2.rect.centerx < ball.rect.centerx:
            toppaddle2.moving_right = True
            bottompaddle2.moving_right = True
        else:
            toppaddle2.moving_right = False
            bottompaddle2.moving_right = False
        if toppaddle2.rect.centerx > ball.rect.centerx:
            toppaddle2.moving_left = True
            bottompaddle2.moving_left = True
        else:
            toppaddle2.moving_left = False
            bottompaddle2.moving_left = False
