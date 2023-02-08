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
    pass

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
    pass

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
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
