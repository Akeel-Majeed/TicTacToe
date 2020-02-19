#import libraries
import pygame
import math
import tkinter.messagebox
from tkinter import *

#setup class:
#method 1) setting up the game set_screen
#method 2) drawing the grid

class Setup:

    def draw_tiles(self):

        """displays the game grid"""

        #horizontal lines
        pygame.draw.line(screen, (0, 0, 0), (100, 200), (400, 200))
        pygame.draw.line(screen, (0, 0, 0), (100, 300), (400, 300))

        #vertical lines
        pygame.draw.line(screen, (0, 0, 0), (200, 100), (200, 400))
        pygame.draw.line(screen, (0, 0, 0), (300, 100), (300, 400))

    def set_screen(self):

        """initlise pygame and set up the screen"""

        #we need the screen variable for other functions
        global screen
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        screen.fill((255, 255, 255))
        pygame.display.set_caption("Tic Tac Toe by Akeel Majeed")
        logo = pygame.image.load('circle.png')
        pygame.display.set_icon(logo)

game = Setup()
game.set_screen()

#tile class:
#attr. 1) a centre (to check for click)
#attr. 2) a status (if claimed or not claimed by a player)
#method 1) a go to position (to blit)

class Tile:
    def __init__(self, centre, go_to_position, status):

        """initlise tile values and go to values (co-ordinates)"""

        self.centre = centre
        self.go_to_position = go_to_position
        self.status = status

t1 = Tile((150, 150), (120, 120), "not claimed")
t2 = Tile((250, 150), (220, 120), "not claimed")
t3 = Tile((350, 150), (320, 120), "not claimed")
t4 = Tile((150, 250), (120, 220), "not claimed")
t5 = Tile((250, 250), (220, 220), "not claimed")
t6 = Tile((350, 250), (320, 220), "not claimed")
t7 = Tile((150, 350), (120, 320), "not claimed")
t8 = Tile((250, 350), (220, 320), "not claimed")
t9 = Tile((350, 350), (320, 320), "not claimed")

#we need these variables to iterate over them
#list all of the tiles
tiles = [t1, t2, t3, t4, t5, t6, t7, t8 ,t9]

#possible ways to win
possibilities = [
[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]
]

#list with all the tiles to draw lines through if someone has won
line_set = [
[t1.centre, t3.centre], [t4.centre, t6.centre], [t7.centre, t9.centre],
[t1.centre,  t7.centre], [t2.centre, t8.centre], [t3.centre, t9.centre],
[t1.centre , t9.centre], [t3.centre, t7.centre]
]

#player class:
#attr. 1) their coordinates
#attr. 2) their image
#attr. 3) their username (through input)
#attr. 4) boolean if a player have won
#attr. 5) max amount of moves they can have
#method 1) their image to blit onto screen

class Player:

    def __init__(self, image, max):

        """initlising player attributes"""

        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.image = image
        self.username = input("What is your username?\n")
        self.tiles_claimed = []
        self.win = False
        self.max = max
        self.has_gone = False

    def display_player(self):

        """displays the player onto the screen"""

        """1) check if player has clicked mouse
           2) go through tiles
           3) check if click has been registered in a tile
           4) check if tile has not been claimed already
           5) check if no one has won yet
           6) check if player has placed max moves
           7) check if player has gone yet"""

        i = 0

        check_win()

#player one blitting mechanics
        if pygame.mouse.get_pressed()[0]:
            for tile in tiles:
                if check_click(player_one.x, player_one.y, tile.centre[0], tile.centre[1]):
                    if tile.status == "not claimed":
                        if not player_one.win and not player_two.win:
                            if len(player_one.tiles_claimed) < player_one.max:
                                    if len(player_one.tiles_claimed) < player_one.max:
                                        if not player_one.has_gone:
                                            screen.blit(player_one.image, tile.go_to_position)
                                            player_one.tiles_claimed.append(i + 1)
                                            tile.status = "claimed"
                                            player_one.has_gone = True
                                            player_two.has_gone = False
                                        else:
                                            pass
                                            #pass - do nothing
                else:
                    i += 1

#player two blitting mechanics
        elif pygame.mouse.get_pressed()[2]:
            for tile in tiles:
                if check_click(player_two.x, player_two.y, tile.centre[0], tile.centre[1]):
                    if tile.status == "not claimed":
                        if not player_one.win and not player_two.win:
                            if len(player_two.tiles_claimed) < player_two.max:
                                if len(player_two.tiles_claimed) < player_two.max:
                                    if not player_two.has_gone:
                                        screen.blit(player_two.image, tile.go_to_position)
                                        player_two.tiles_claimed.append(i + 1)
                                        tile.status = "claimed"
                                        player_two.has_gone = True
                                        player_one.has_gone = False
                                    else:
                                        pass
                                        #pass - do nothing
                else:
                    i += 1

#declaring the two players
player_one = Player(pygame.image.load('circle.png'), 5)
player_two = Player(pygame.image.load('cancel.png'), 4)

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

def check_win():

    """checks if a player has won and draws line"""

    line_drawn = False

    i = 0
    j = 0

#player one
    for claim in possibilities:
        if all(i in player_one.tiles_claimed for i in claim):
            if line_drawn == False:
                player_one.win = True
                pygame.draw.line(
                screen, (0, 128, 0), (line_set[i][0][0], line_set[i][0][1]), (line_set[i][-1][0], line_set[i][-1][1]),
                5
                )
                line_drawn = True
            else:
                pass
        else:
            i += 1

#player two
    for claim in possibilities:
        if all(j in player_two.tiles_claimed for j in claim):
            if line_drawn == False:
                player_two.win = True
                pygame.draw.line(
                screen, (0, 128, 0), (line_set[j][0][0], line_set[j][0][1]), (line_set[j][-1][0], line_set[j][-1][1]),
                5
                )
                line_drawn = True
            else:
                pass
        else:
            j += 1

#font to display on the screen who has won
font = pygame.font.Font('freesansbold.ttf', 16)
def text():

    """displays the winner message on top left"""

    #possible messages
    message_one = font.render(player_one.username + " has won!", True, (0, 0, 0))
    message_two = font.render(player_two.username + " has won!", True, (0, 0, 0))
    message_three = font.render("It is a tie!", True, (0, 0, 0))

    check_win()

    if player_one.win:
        screen.blit(message_one, (10, 10))
    elif player_two.win:
        screen.blit(message_two, (10, 10))
    elif len(player_one.tiles_claimed) + len(player_two.tiles_claimed) == 9:
        screen.blit(message_three, (10, 10))

def check_click(x, y, tx, ty):

    """checks if a click has been registered in a desired location"""

    distance = math.sqrt(math.pow(x - tx, 2) + (math.pow(y - ty, 2)))
    if distance < 27:
        return True
    else:
        return False

def refresh():

    """refreshes all player one and player two mouse coordinates"""

#refreshing player one coordinates
    player_one.x = pygame.mouse.get_pos()[0]
    player_one.y = pygame.mouse.get_pos()[1]

#refreshing player two coordinates
    player_two.x = pygame.mouse.get_pos()[0]
    player_two.y = pygame.mouse.get_pos()[1]

#asking for players' usernames
player_one.username
player_two.username

intro_message()

#main loop
run = True
while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game.draw_tiles()

    player_one.display_player()
    player_two.display_player()

    refresh()

    text()

    pygame.display.update()

pygame.quit()
