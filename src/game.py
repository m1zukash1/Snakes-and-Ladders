from board import Board
from queue import Queue
from player import Player
import random
import copy

class Game:

    board: Board = Board()

    def __init__(self, player_count: int):
        if player_count > 3 or player_count <= 0:
            raise ValueError("Player count must be between 1 and 3")
        
        for i in range(player_count):
            self.board.player_queue.append(Player(i + 1))

        

    def turn(self):
        player: Player = self.board.player_queue.pop(0) #Get player from the start of the queue

        dice_number = random.randint(1, 3)
        where = player.position + dice_number

        print("Player id: ", player.id)
        print("Current player position: ", player.position)
        print("Rolled number on dice: ", dice_number)

        if where >= self.board.board.size:
            print("player", player.id, "won the game")
            exit()

        print("Where player went: ", where)

        match self.board.at(where).type:
            case "normal":
                print("Special type of the tile is normal. Player stays here")
                #player.position = where #TODO
                self.set_position(player, where)
            case "ladder":
                print("Special type of the tile is ladder. Player goes up to ", self.board.at(where).target, " position")
                #player.position = self.board.at(where).target #TODO
                self.set_position(player, self.board.at(where).target)
                pass
            case "snake":
                print("Special type of the tile is snake. Player goes down to ", self.board.at(where).target, " position")
                #player.position = self.board.at(where).target #TODO
                self.set_position(player, self.board.at(where).target)
                pass
        
        print("----------")
        self.board.player_queue.append(player) #Put player to the back of the queue


    def set_position(self, player: Player, position: int):
        for _player in self.board.player_queue:
            if player == _player:
                continue

            if position == _player.position:
                self.set_position(_player, _player.position - 1)
                print("Player landed on the tile on which player", _player.id, "was and that player was placed one tile below")
                
        player.position = position