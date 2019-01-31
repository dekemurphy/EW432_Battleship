import pygame
from pygame.locals import *
import sys

import colors
import sprites
import utilities
import human
from game_board import GameBoard
import utilities

BLOCK_SIZE = 30
NBLOCKS = 11
TOP_MARGIN = 30
PADDING = 10


def main():
    pygame.init()

    screen: pygame.Surface = pygame.display.set_mode(((BLOCK_SIZE * NBLOCKS) * 2 + PADDING * 3,
                                                      BLOCK_SIZE * NBLOCKS + TOP_MARGIN + PADDING))
    #print((BLOCK_SIZE * NBLOCKS) * 2 + PADDING * 3)
    #print( BLOCK_SIZE * NBLOCKS + TOP_MARGIN + PADDING)
    screen.fill(colors.screen_bkgd)
    pygame.display.set_caption('USNA Battleship')
    sprites.initialize()

    # size of the game board figure based on BLOCK SIZE pixels
    board_dimension = (BLOCK_SIZE * NBLOCKS, BLOCK_SIZE * NBLOCKS)

    # "my" game board has my ships
    my_board: GameBoard = GameBoard(board_dimension)
    my_board.rect.top = TOP_MARGIN
    my_board.rect.left = PADDING

    # "their" game board has my guesses
    their_board: GameBoard = GameBoard(board_dimension)
    # position their_board PADDING pixels to the right of my_board
    their_board.rect.top = TOP_MARGIN
    their_board.rect.left = PADDING*2+my_board.rect.width

    # paint the board surface
    my_board.refresh()
    their_board.refresh()

    # --------- BEGIN YOUR CODE ----------
    # add titles above the game boards
    titleYou = utilities.create_text('You', 24, colors.foreground)
    titleThem = utilities.create_text('Them', 24, colors.foreground)
    # draw 'YOU' centered above my_board
    titleYouRect = titleYou.get_rect()
    titleYouRect.centerx = my_board.rect.centerx
    titleYouRect.centery = my_board.rect.top - PADDING*1.5
    screen.blit(titleYou, titleYouRect)
    # draw 'THEM' centered above their_board
    titleThemRect = titleThem.get_rect()
    titleThemRect.centerx = their_board.rect.centerx
    titleThemRect.centery = their_board.rect.top - PADDING*1.5
    screen.blit(titleThem, titleThemRect)
    # --------- END YOUR CODE ------------

    # create a human player
    player1 = human.Human()
    player1.initialize()
    player1.draw(my_board, their_board)

    # place the board on the screen
    their_board.draw(screen)
    my_board.draw(screen)

    while True:
        # wait for user to click 'X' button
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()