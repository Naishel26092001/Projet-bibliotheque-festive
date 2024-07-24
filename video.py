import cv2
import pygame
import sys

def play_intro_video(screen, video_path):
    cap = cv2.VideoCapture(video_path)
    screen_width, screen_height = screen.get_size()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.transpose(frame)
        frame = cv2.flip(frame, 1)
        frame_surface = pygame.surfarray.make_surface(frame)
        screen.blit(pygame.transform.scale(frame_surface, (screen_width, screen_height)), (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()
    cap.release()

def play_background_video(screen, video_path):
    cap = cv2.VideoCapture(video_path)
    screen_width, screen_height = screen.get_size()
    return cap, screen_width, screen_height