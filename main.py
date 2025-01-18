import pygame
from sys import exit
import config
import components
import population
import pygame.freetype


print(config)

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    pipes_spawn_time = 10
    font = pygame.freetype.SysFont(None, 30)

    while True:
        quit_game()

        config.window.fill((0, 0, 0))

        #spawn ground
        config.ground.draw(config.window)

        #spawn pipes
        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)


        #Spawn players
        if not population.extinct():
            population.update_live_players()
        else:
            config.pipes.clear()
            population.natural_selection()
            

        # Render generation number
        generation_text = f"Generation: {population.generation}"
        font.render_to(config.window, (10, config.ground.ground_level + 180), generation_text, (255, 255, 255))

        clock.tick(60)
        pygame.display.flip()


main()


