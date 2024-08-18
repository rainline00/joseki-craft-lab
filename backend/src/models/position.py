from gqlalchemy import Node, Relationship


class Position(Node):
    def __init__(self, sfen, evaluation=None, best_move=None):
        super().__init__()
        self.sfen = sfen
        self.evaluation = evaluation
        self.best_move = best_move


class Move(Relationship):
    def __init__(self, start_position, end_position, move_string, count=1):
        super().__init__(start_node=start_position, end_node=end_position)
        self.move_string = move_string
        self.count = count
        self.count = count
