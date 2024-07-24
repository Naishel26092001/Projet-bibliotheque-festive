import pygame
from video import play_intro_video
from user_form import user_info_form
from genre_menu import genre_menu

def main():
    # Initialiser Pygame
    pygame.init()

    # Configuration des dimensions de l'écran
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bibliothèque Virtuelle")

    # Lecture de la vidéo d'introduction
    play_intro_video(screen, 'assets/intro.mp4')

    # Affichage du formulaire d'information utilisateur avec arrière-plan vidéo
    user_info_form(screen, 'assets/background.mp4')

    # Affichage du menu des genres avec arrière-plan vidéo
    genre_menu(screen, 'assets/background.mp4')

if __name__ == '__main__':
    main()
