"""Puzzle game.

Puzzle game task.

https://github.com/mvysotskyi/puzzle_task
"""

def get_horizontal(board: list[str], row: int, begin: int, end: int) -> list[int]:
    """
    Function returns list of numbers in row 'row'
    at range ['begin', 'end'].
    >>> get_horizontal(["**** ****",\
                    "***1 ****",\
                    "**  3****",\
                    "* 4 1****",\
                    "     9 5 ",\
                    " 6  83  *",\
                    "3   1  **",\
                    "  8  2***",\
                    "  2  ****"], 6, 0, 8)
    [3, 1]
    """
    result = []
    for sym in range(begin, end + 1):
        if board[row][sym].isnumeric():
            result.append(int(board[row][sym]))

    return result

def get_vertical(board: list[str], col: int, begin: int, end: int) -> list[int]:
    """
    Function returns list of numbers in column 'col'
    at range ['begin', 'end'].
    >>> get_vertical(["**** ****",\
                    "***1 ****",\
                    "**  3****",\
                    "* 4 1****",\
                    "     9 5 ",\
                    " 6  83  *",\
                    "3   1  **",\
                    "  8  2***",\
                    "  2  ****"], 4, 3, 8)
    [1, 8, 1]
    """
    result = []
    for sym in range(begin, end + 1):
        if board[sym][col].isnumeric():
            result.append(int(board[sym][col]))

    return result

def validate_board(board: list[str]) -> bool:
    """
    Function validates board in accordance with the rules.
    >>> validate_board(["**** ****",\
                    "***1 ****",\
                    "**  3****",\
                    "* 4 1****",\
                    "     9 5 ",\
                    " 6  83  *",\
                    "3   1  **",\
                    " 18  2***",\
                    "  2  ****"])
    False
    """
    ref_set = {num for num in range(1, 10)}

    for idx in range(9):
        col = get_vertical(board, idx, 0, 8)
        row = get_horizontal(board, idx, 0, 8)

        if len(col) != len(set(col)) or len(row) != len(set(row)):
            return False

        if not ref_set.issuperset(col) or not ref_set.issuperset(row):
            return False

    for idx in range(0, 5):
        col = get_vertical(board, idx, 4 - idx, 8 - idx)
        row = get_horizontal(board, 8 - idx, idx, idx + 4)

        central = {int(board[8 - idx][idx])} if board[8 - idx][idx].isnumeric() else set()

        if set(col) & set(row) != central:
            return False

    return True

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
