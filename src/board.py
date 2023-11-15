from pyllist import dllist, dllistnode #Assigment requires to use this module ://
from player import Player
import json

class Node:

    def __init__(self, type: str = None, target: int = None):
        self.type = type
        self.target = target

class Board:

    board: dllist = dllist()

    player_queue: list = [] #I'd prefer `player_queue` in `Game` class, but assignment requires it here ://

    def __init__(self):
        with open('assets/board.json', 'r') as file:
            json_file = json.load(file)
        for i in json_file:
            self.board.append(Node(i["type"], i["target"]))

    def at(self, x: int):
        x -= 1
        return self.board[x]

    def insert(self, where: int, type: str = "normal", target: int = None):
        new_node: dllistnode = dllistnode(Node(type, target))
        node_at_pos: dllistnode = self.board.nodeat(where)
        self.board.insert(new_node, before=node_at_pos)

    def remove(self, where: int):
        node: dllistnode = self.board.nodeat(where)
        self.board.remove(node)

    def overwrite_type(self, where: int, type: str = "normal", target: int = None):
        node: dllistnode = self.board.nodeat(where)
        node.value.type = type
        node.value.target = target

    def purge(self):
        self.board = dllist()