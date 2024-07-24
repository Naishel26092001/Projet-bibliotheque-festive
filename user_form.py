import pygame
import sys
import cv2
from video import play_background_video

def user_info_form(screen, background_video_path):
    font = pygame.font.Font(None, 36)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color_name = color_inactive
    color_age = color_inactive
    active_name = False
    active_age = False
    name = ''
    age = ''
    input_box_name = pygame.Rect(300, 200, 200, 40)
    input_box_age = pygame.Rect(300, 300, 200, 40)
    done = False

    cap, screen_width, screen_height = play_background_video(screen, background_video_path)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_name.collidepoint(event.pos):
                    active_name = not active_name
                else:
                    active_name = False
                if input_box_age.collidepoint(event.pos):
                    active_age = not active_age
                else:
                    active_age = False
                color_name = color_active if active_name else color_inactive
                color_age = color_active if active_age else color_inactive
            if event.type == pygame.KEYDOWN:
                if active_name:
                    if event.key == pygame.K_RETURN:
                        active_name = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode
                if active_age:
                    if event.key == pygame.K_RETURN:
                        active_age = False
                    elif event.key == pygame.K_BACKSPACE:
                        age = age[:-1]
                    else:
                        age += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = pygame.Rect(350, 400, 100, 50)
                if button.collidepoint(event.pos):
                    if name and age:
                        done = True

        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.transpose(frame)
        frame = cv2.flip(frame, 1)
        frame_surface = pygame.surfarray.make_surface(frame)
        screen.blit(pygame.transform.scale(frame_surface, (screen_width, screen_height)), (0, 0))

        welcome_text = font.render("Bienvenue à la Bibliothèque Virtuelle", True, (255, 255, 255))
        screen.blit(welcome_text, (screen_width // 2 - welcome_text.get_width() // 2, 50))

        txt_surface_name = font.render(name, True, color_name)
        txt_surface_age = font.render(age, True, color_age)
        screen.blit(txt_surface_name, (input_box_name.x+5, input_box_name.y+5))
        screen.blit(txt_surface_age, (input_box_age.x+5, input_box_age.y+5))
        pygame.draw.rect(screen, color_name, input_box_name, 2)
        pygame.draw.rect(screen, color_age, input_box_age, 2)
        label_name = font.render("Rentre ton nom:", True, (0, 0, 0))
        label_age = font.render("Rentre ton âge:", True, (0, 0, 0))
        screen.blit(label_name, (300, 170))
        screen.blit(label_age, (300, 270))
        save_button = font.render("Entrer", True, (0, 0, 0))
        button = pygame.Rect(350, 400, 100, 50)
        pygame.draw.rect(screen, (0, 0, 0), button, 2)
        screen.blit(save_button, (button.x + 10, button.y + 10))
        pygame.display.flip()

    cap.release()
