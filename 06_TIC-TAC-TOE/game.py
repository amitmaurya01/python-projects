class TicTacToe:
    def __init__(self) -> None:
        # we will use a single list to rep 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

        def print_board(self):
            # this is just getting the rows
            for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
                print('| '+' | '.join(row)+' |')

        @staticmethod
        def print_board_nums():
            # 0 | 1 | 2 etc (tells us what number corresponds to what box)
            number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                            for j in range(3)]
