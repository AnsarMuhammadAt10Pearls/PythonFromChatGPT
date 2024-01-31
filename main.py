import pygame
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 960, 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors - Vibrant Color Palette
background_color = (34, 49, 63)
progress_colors = [
    (231, 76, 60), (26, 188, 156), (46, 204, 113),
    (52, 152, 219), (155, 89, 182), (241, 196, 15),
    (230, 126, 34)
]
white = (255, 255, 255)
grey = (189, 195, 199)

# Onboarding steps and their progress
steps = [
    'Sign Up', 'Verification', 'Tutorial', 'Welcome',
    'Profile Setup', 'Preferences', 'Complete'
]
progress = [0] * len(steps)  # Progress for each step

# Roboto font for a modern look
font_path = "C:\\Users\\ansar.muhammad\\Documents\\Roboto\\Roboto-Regular.ttf"
font = pygame.font.Font(font_path, 24)

# Set the pygame window title
pygame.display.set_caption('Comprehensive Customer Onboarding Workflow')

# Clock to control animation speed
clock = pygame.time.Clock()

def draw_progress_bar(position, progress, color):
    """Draws a smooth progress bar on the screen."""
    pygame.draw.rect(screen, grey, position)  # Draw the background of the progress bar
    inner_pos = (position[0] + 5, position[1] + 5, (position[2] - 10) * progress, position[3] - 10)
    pygame.draw.rect(screen, color, inner_pos, border_radius=5)  # Draw the inner progress part with rounded corners

def draw_details(step_index, progress, scale):
    """Draw additional details for each step with animations."""
    radius = int(25 * scale)
    if step_index < len(steps) - 1:
        x = 50 + step_index * 90 + int(progress * 70)
        y = 380

        # Clear the previous text by filling the background at the text position
        screen.fill(background_color, (50 + step_index * 90 - radius, y + radius + 5, 400, 30))

        pygame.draw.circle(screen, progress_colors[step_index], (x, y), radius)

        # Fading effect for text
        alpha = int(255 * progress) if progress <= 1 else 255
        detailed_texts = [
            "Fill out personal info", "Check your email",
            "Learn how to use our platform", "Get started with your account",
            "Set up your profile", "Choose your preferences",
            "Enjoy our services"
        ]
        text_surf = font.render(detailed_texts[step_index], True, white).convert_alpha()
        text_surf.set_alpha(alpha)
        screen.blit(text_surf, (50 + step_index * 90 - radius, y + radius + 5))

def draw_step(step_index, progress):
    """Draws the step including its progress bar, label, and additional details with animation."""
    screen.fill(background_color)  # Clear the screen

    # Draw the previous step's text with a fading effect
    if step_index > 0:
        prev_text = font.render(steps[step_index - 1], True, white)
        prev_text_rect = prev_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        prev_alpha = int(255 * (1 - progress))
        prev_text.set_alpha(prev_alpha)
        screen.blit(prev_text, prev_text_rect)

    # Draw the current step's text
    text = font.render(steps[step_index], True, white)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)

    # Draw additional lines for "Setup Profile" step
    if step_index == 4:
        line1 = font.render("Create a captivating profile", True, white)
        line1_rect = line1.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(line1, line1_rect)

        line2 = font.render("Add your details and preferences", True, white)
        line2_rect = line2.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
        screen.blit(line2, line2_rect)

        line3 = font.render("Personalize your experience", True, white)
        line3_rect = line3.get_rect(center=(screen_width // 2, screen_height // 2 + 150))
        screen.blit(line3, line3_rect)

    # Progress bar positions: x, y, width, height
    bar_position = (50 + step_index * 90, 100, 70, 15)
    draw_progress_bar(bar_position, progress, progress_colors[step_index])

    # Scale for the circle animation
    scale = 1.0 + 0.5 * progress
    draw_details(step_index, progress, scale)

# Main loop
running = True
step_index = 0  # Current step

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update and draw each step and its details with animations
    draw_step(step_index, progress[step_index])

    # Animate progress for the current step
    progress[step_index] += 0.005  # Adjust the speed of progress filling
    if progress[step_index] >= 1:
        progress[step_index] = 1  # Cap at 100%
        if step_index < len(steps) - 1:  # Wait before moving to the next step
            pygame.time.wait(1000)  # Pause for effect
            step_index += 1
        else:
            # Reset or conclude the animation when all steps are complete
            pygame.time.wait(2000)  # Pause for effect
            progress = [0] * len(steps)
            step_index = 0

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
sys.exit()
