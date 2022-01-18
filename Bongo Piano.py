import pygame
import os

# Static Variables
    #Colors
BLACK    = (   0,   0,   0)
GRAY     = (  50,  50,  50)
GREY     = (  50,  50,  50)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 200,   0,   0)
BLUE     = (   0,   0, 255)

#Window
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
    

pygame.display.set_caption("Bongo Cat Piano")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 







# Main Program Loop 
class Main:
    def __init__(self):
        #Initialize Pygame
        pygame.init()
        pygame.font.init()

        #Window
        pygame.display.set_caption("Bongo Cat Piano")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.DOUBLEBUF)

        #Font
        self.font = pygame.font.SysFont(None, 26)

        #Act and Game_State System
        self.act = 0
        self.game_state = 0

        #Selector
        self.selector = 1

    def keysAndLife(self):
        self.act = 0
        die = False
        
    # Runs as the program runs
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                die = True

    # Game logic should go here
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    print("SPACE")
                    self.game_state += 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("User pressed a mouse button")

        return die
     
    # Drawing code should go here
    def drawText(self, text, coordinates, color =(255, 255, 255)):
        text = self.font.render(text, True, color)
        self.screen.blit(text, coordinates)

    def drawMenu(self):
        self.screen.fill(BLACK)
        prefix = [" ", " "]
        prefix[self.selector-1] = "> "
        self.drawText(prefix[0] + "Play", (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 40))
        self.drawText(prefix[1] + "Quit", (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 20))

    def drawGameplay(self):
        self.screen.fill(GRAY)
        self.drawText("MAKE GAMEPLAY LOL", (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

    def drawCutscene(self):
        self.screen.fill(GREY)
        self.drawText("COOL CUTSCENE HAPPENING!", (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

    def displayGameOver(self):
        self.screen.fill(RED)
        self.drawText("GAME OVER!!!", (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

if __name__ == "__main__":

    game = Main()
    quit = False
    while not quit:
        if game.game_state == 0:
            game.drawMenu()
        elif game.game_state == 1:
            game.drawGameplay()
        elif game.game_state == 2:
            game.drawCutscene()
        elif game.game_state == 3:
            game.drawGameOver()
        
    # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        quit = game.keysAndLife()

pygame.quit()
