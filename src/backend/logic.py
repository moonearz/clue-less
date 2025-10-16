from .constants import CHARACTERS, WEAPONS, ROOMS

class Game:
     def __init__(self, players):
        self.players = players
        self.solution = None
        self.cards = CHARACTER + WEAPONS + ROOMS
        self.board = None

    def start_game(self):
        """Deal the cards, set solution"""
        pass

    def make_suggestion(self, player, suspect, weapon, room):
        pass

    def make_accusation(self, player, suspect, weapon, room):
        """Check if a player's accusation matches the solution"""
        pass


        
