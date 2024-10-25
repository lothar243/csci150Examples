from pprint import pprint

chessboard_state = [['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
                    ['♟']*8,
                    ['.']*8,
                    ['.']*8,
                    ['.']*8,
                    ['.']*8,
                    ['.']*8,
                    ['.']*8,
                    ['♙']*8,
                    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
                    ]

def print_board(chessboard):
    for row in chessboard:
        for piece in row:
            print(piece, end=" ")
        print()

if __name__ == "__main__":
    print_board(chessboard=chessboard_state)