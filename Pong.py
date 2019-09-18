from time import sleep
from GameSettings import Settings
from StartScreen import *
from Paddles import *
from Ball import Ball
from Score import *
import GameFunctions as gameFunc


# start the game
def run_game():
    # screen initializations and menu screen
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    play_button = Button(screen, "Play")
    title = Title(screen, "Pong", 0)

    # game screen display settings
    while True:
        screen.fill(settings.bg_color)
        title.draw()
        play_button.draw()
        pygame.display.flip()
        midpaddle1 = MidPaddle1(settings, screen)
        toppaddle1 = TopPaddle1(settings, screen)
        bottompaddle1 = BottomPaddle1(settings, screen)
        midpaddle2 = MidPaddle2(settings, screen)
        toppaddle2 = TopPaddle2(settings, screen)
        bottompaddle2 = BottomPaddle2(settings, screen)
        ball = Ball(settings, screen)
        score1 = Score1(screen)
        score2 = Score2(screen)
        winner = Winner(screen)
        while settings.game_start is False:
            gameFunc.check_events(settings, play_button, midpaddle1, toppaddle1, bottompaddle1)
        gameFunc.update_screen(screen, settings, ball, midpaddle1, toppaddle1, bottompaddle1, midpaddle2, toppaddle2,
                         bottompaddle2, score1, score2)
        while score1.points < 3 and score2.points < 3:
            gameFunc.check_events(settings, play_button, midpaddle1, toppaddle1, bottompaddle1)
            gameFunc.ai_directives(ball, midpaddle2, toppaddle2, bottompaddle2,)
            gameFunc.check_score(settings, screen, ball, midpaddle1, toppaddle1, bottompaddle1, midpaddle2, toppaddle2,
                           bottompaddle2, score1, score2)
            gameFunc.update_game(settings, ball, midpaddle1, toppaddle1, bottompaddle1, midpaddle2, toppaddle2, bottompaddle2)
            gameFunc.update_screen(screen, settings, ball, midpaddle1, toppaddle1, bottompaddle1, midpaddle2, toppaddle2,
                             bottompaddle2, score1, score2)
        # show win screen after player scores 3 points and play win audio
        if score1.points == 3:
            winner.prep_msg("You won")
            winner.draw()
            sound = pygame.mixer.Sound('Victory.wav')
            pygame.mixer.music.load('Victory.wav')
            pygame.mixer.music.play(1, 0.0)
        # show lose screen when player loses and play lose audio
        else:
            winner.prep_msg("You lost")
            winner.draw()
            sound = pygame.mixer.Sound('lost.wav')
            pygame.mixer.music.load('lost.wav')
            pygame.mixer.music.play(1, 0.0)
        # 3 second delay before game start after clicking play from menu screen
        pygame.display.flip()
        sleep(3)
        settings.game_start = False
        pygame.mouse.set_visible(True)


# start game        
run_game()
