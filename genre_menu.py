import pygame
import cv2
import sys
from genres.humour import show_humour_books
from video import play_background_video

def genre_menu(screen, background_video_path):
    """Affiche le menu des genres avec une vidéo de fond et gère les sélections de genre."""
    font_large = pygame.font.Font(None, 48)
    
    # Définir les genres et leurs images associées
    genres = ['Humour', 'Drame']
    genre_images = ['assets/humour.png', 'assets/drame.png']
    genre_functions = {
        'Humour': show_humour_books,
        # Ajoutez d'autres genres et leurs fonctions correspondantes ici
    }
    
    # Charger les images des genres une fois
    loaded_genre_images = [pygame.image.load(img_path) for img_path in genre_images]
    loaded_genre_images = [pygame.transform.scale(img, (40, 40)) for img in loaded_genre_images]

    # Lire la vidéo de fond
    cap, screen_width, screen_height = play_background_video(screen, background_video_path)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True  # Quitter le menu des genres
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for idx, genre in enumerate(genres):
                    button = pygame.Rect(150, 100 + idx * 100, 500, 50)
                    if button.collidepoint(event.pos) and genre in genre_functions:
                        genre_functions[genre](screen)
                        break

        if done:
            break

        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.transpose(frame)
        frame = cv2.flip(frame, 1)
        frame_surface = pygame.surfarray.make_surface(frame)
        screen.blit(pygame.transform.scale(frame_surface, (screen_width, screen_height)), (0, 0))

        for idx, genre in enumerate(genres):
            button = pygame.Rect(150, 100 + idx * 100, 500, 50)
            pygame.draw.rect(screen, (0, 0, 0), button, 2)
            genre_label = font_large.render(genre, True, (0, 0, 0))
            screen.blit(genre_label, (button.x + 10, button.y + 10))
            screen.blit(loaded_genre_images[idx], (button.x + 450, button.y + 5))

        pygame.display.flip()

    cap.release()
