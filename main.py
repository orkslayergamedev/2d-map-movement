import os

x_pos = 0
y_pos = 0

width = 5
height = 5

game_map_revealed = ((".", ".", ".", ".", "."),
                     (".", ".", ".", ".", "."),
                     (".", ".", ".", ".", "."),
                     (".", ".", ".", ".", "."),
                     (".", ".", ".", ".", "."))

game_map = [["X", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]]


def clear_terminal() -> None:
    """Clear the terminal."""
    os.system('cls')


def draw_map() -> None:
    """Draw the map inside a box."""
    print(".-----.")
    for line in game_map:
        print("|", end="")
        for tile in line:
            print(tile, end="")
        print("|")
    print("'-----'")


def move_player(move_input: str, x: int, y: int) -> tuple[int, int]:
    """Move the player if the inputs and conditions are valid."""
    if move_input == "w" and y > 0:
        y -= 1
    elif move_input == "s" and y < height - 1:
        y += 1
    elif move_input == "a" and x > 0:
        x -= 1
    elif move_input == "d" and x < width - 1:
        x += 1
    return x, y


while True:
    clear_terminal()
    draw_map()

    choice = input("")

    # switch the tile on your position to the one on the revealed map
    game_map[y_pos][x_pos] = game_map_revealed[y_pos][x_pos]

    # move your player
    x_pos, y_pos = move_player(move_input=choice, x=x_pos, y=y_pos)

    # draw an X to your current position
    game_map[y_pos][x_pos] = "X"
