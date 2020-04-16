import pygame
import math
import sys
import random
import tkinter.messagebox
from tkinter import *

def main():
    def set_screen():

        """Initilises pygame and draws window."""

        global screen
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        screen.fill((255, 255, 255))
        pygame.display.set_caption("Tic Tac Toe by Akeel Majeed")
        logo = pygame.image.load('C:/Users/akeel/Downloads/circle.png')
        pygame.display.set_icon(logo)

    set_screen()
    
    def draw_grid():

        """Draws the TicTacToe grid."""

        # horizontal lines
        pygame.draw.line(screen, (0, 0, 0), (100, 200), (400, 200))
        pygame.draw.line(screen, (0, 0, 0), (100, 300), (400, 300))

        # vertical lines
        pygame.draw.line(screen, (0, 0, 0), (200, 100), (200, 400))
        pygame.draw.line(screen, (0, 0, 0), (300, 100), (300, 400))
    

    class Tile:
        def __init__(self, CENTRE, BLIT_POS, status):

            """

            Tile attributes.
            :param CENTRE: the centre of the tile
            :param BLIT_POS: the position to blit player's image (ie. circle or square) to
            :param status: the current status of the tile (ie. claimed or not claimed)

            """

            self.CENTRE     = CENTRE
            self.BLIT_POS  = BLIT_POS
            self.status     = status

    
    t1 = Tile((150, 150), (120, 120), "not claimed")
    t2 = Tile((250, 150), (220, 120), "not claimed")
    t3 = Tile((350, 150), (320, 120), "not claimed")
    t4 = Tile((150, 250), (120, 220), "not claimed")
    t5 = Tile((250, 250), (220, 220), "not claimed")
    t6 = Tile((350, 250), (320, 220), "not claimed")
    t7 = Tile((150, 350), (120, 320), "not claimed")
    t8 = Tile((250, 350), (220, 320), "not claimed")
    t9 = Tile((350, 350), (320, 320), "not claimed")

    class Player:
        def __init__(self, IMAGE, turn, BUTTON):

            """

            Player attributes.
            :param IMAGE: player's image (ie. circle or cross)
            :param turn: boolean indicating whose turn it is
            :param BUTTON: player's button to press

            """

            self.IMAGE          = IMAGE
            self.turn           = turn
            self.BUTTON         = BUTTON
            self.mouse_pos      = pygame.mouse.get_pos()
            self.tiles_claimed  = []
        
        def refresh_pos(self):

            """Refreshes player mouse coordinates."""

            self.mouse_pos = pygame.mouse.get_pos()
        
        def clicked(self):

            """
            
            Checks if player clicked their assigned button.
            :return: boolean if player has pressed their assigned button
            
            """

            return pygame.mouse.get_pressed()[self.BUTTON]
        
        def clicked_tile(self, tx, ty):

            """
            
            Checks if player clicked a tile.
            :param tx: tile x coordinate
            :param ty: tile y coordinate
            :return: boolean if player has clicked a tile
            
            """

            if self.clicked():
                distance = math.sqrt(math.pow(self.mouse_pos[0] - tx, 2) + (math.pow(self.mouse_pos[1] - ty, 2)))
                if distance < 27:
                    return True
                else:
                    return False
        
        def won(self, reset = False):

            """
            
            Checks if player has won.
            :param reset: boolean; if True won returns False
            :return: if player has won or not
            
            """

            global LINE # line to draw if player has won

            # possible ways to win
            POSSIBILITIES = [
            [t1, t2, t3], [t4, t5, t6], [t7, t8, t9], [t1, t4, t7],
            [t2, t5, t8], [t3, t6, t9], [t1, t5, t9], [t3, t5, t7],
            ]

            for possibilty in POSSIBILITIES:
                if reset:
                    return False
                if all(i in self.tiles_claimed for i in possibilty):
                    LINE = POSSIBILITIES.index(possibilty)
                    draw_line(LINE)
                    return True
            return False

    player_one = Player(pygame.image.load('C:/Users/akeel/Downloads/circle.png'), True, 0) # 0 --> left click
    player_two = Player(pygame.image.load('C:/Users/akeel/Downloads/cancel.png'), False, 2) # 2 --> right click

    def display(player):
        
        """
        
        Displays player icon (ie. circle or cross) onto screen.
        :param player: player object
        
        """

        global TILES

        TILES = [t1, t2, t3, t4, t5, t6, t7, t8, t9]

        # check if anyone has won
        player_one.won()
        player_two.won()

        for tile in TILES:
            tx, ty = tile.CENTRE[0], tile.CENTRE[1] # 0 --> x, 1 --> y
            if player.clicked_tile(tx, ty):
                if tile.status == "not claimed":
                    if not player_one.won() and not player_two.won():
                        if player.turn:
                            screen.blit(player.IMAGE, tile.BLIT_POS)
                            player.tiles_claimed.append(tile)
                            tile.status = "claimed"
                            if player == player_one:
                                player_one.turn = False
                                player_two.turn = True
                            elif player == player_two:
                                player_one.turn = True
                                player_two.turn = False
                            
    
    def draw_line(line):
        
        """
        
        Draws a line if player has won.
        :param line: line to draw
        
        """

        # list with all the tiles to draw lines through if someone has won
        LINES = [
        [t1.CENTRE, t3.CENTRE], [t4.CENTRE, t6.CENTRE], [t7.CENTRE, t9.CENTRE], [t1.CENTRE, t7.CENTRE],
        [t2.CENTRE, t8.CENTRE], [t3.CENTRE, t9.CENTRE], [t1.CENTRE, t9.CENTRE], [t3.CENTRE, t7.CENTRE],
        ]

        pygame.draw.line(
        screen, (0, 128, 0), (LINES[LINE][0][0], LINES[LINE][0][1]),
        (LINES[LINE][-1][0], LINES[LINE][-1][1]),
        5) # 5 --> thickness of line
    
    def intro_message():

        """displays the intro message"""

        root = Tk()
        root.attributes('-topmost', True)
        root.withdraw()
        tkinter.messagebox.showinfo(
        "Tic Tac Toe by Akeel Majeed", "Welcome to tic tac toe!\nPlay with a friend!"
        )
        try:
            root.destroy
        except:
            pass

    def text():

        """displays the winner message on top left"""

        # font to render text
        FONT = pygame.font.Font('freesansbold.ttf', 16)

        # possible messages
        MESSAGE_ONE = FONT.render("circle has won! Press Q to quit or R to play again!", True, (0, 0, 0))
        MESSAGE_TWO = FONT.render("cross has won! Press Q to quit or R to play again!", True, (0, 0, 0))
        MESSAGE_THREE = FONT.render("It is a tie! Press Q to quit or R to play again!", True, (0, 0, 0))

        if player_one.won():
            screen.blit(MESSAGE_ONE, (10, 10))
        elif player_two.won():
            screen.blit(MESSAGE_TWO, (10, 10))
        elif len(player_one.tiles_claimed) + len(player_two.tiles_claimed) == 9:
            screen.blit(MESSAGE_THREE, (10, 10))

    def reset(player_one, player_two, screen, TILES):

        """
        
        Resets players attributes and redraws screen.
        :param player_one: Player instance
        :param player_two: Player instance
        :param screen: game screen
        :param TILES: list of all the tiles (9 total)
        
        """

        screen.fill((255, 255, 255))

        player_one.tiles_claimed, player_two.tiles_claimed = [], []

        player_one.won(reset = True), player_two.won(reset = True)

        player_one.turn, player_two.turn = True, False

        for tile in TILES:
            tile.status = "not claimed" # map doesnt work for some reason
            
    # display intro message
    intro_message()

    # main loop
    while True:

        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset(player_one, player_two, screen, TILES)
                    
        
        draw_grid()

        player_one.refresh_pos()
        player_two.refresh_pos()

        display(player_one)
        display(player_two)

        text() 

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()