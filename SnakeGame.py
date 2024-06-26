# random => A library in python to get random values
# curses => A library used for interface or to make our snake appear in terminal
import random
import curses

screen = curses.initscr()

curses.curs_set(0)


screen_height, screen_width = screen.getmaxyx()

window = curses.newwin(screen_height, screen_width, 0, 0)

window.keypad(True)
window.timeout(130)

snakeX = screen_width // 6
snakeY = screen_height // 4

snake = [
  [snakeY , snakeX], #Head
  [snakeY , snakeX -1], #Stomach
  [snakeY , snakeX -2] #Tail
]

Food = [screen_height // 2 , screen_width // 2] 
window.addch(Food[0], Food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if  next_key == -1 else next_key

    if (snake [0][0] in [0, screen_height -1] or snake[0][1] in [0, screen_width -1] or snake[0] in snake[1:]):
        curses.endwin()
        print("Game Over")
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == Food:

        Food = None

        while Food is None:
            new_Food = [
            random.randint(1, screen_height -1),
            random.randint(1, screen_width -1)
          ]

            Food = new_Food if new_Food not in snake else None

        window.addch(Food[0], Food[1], curses.ACS_PI)
    else:
        Tail = snake.pop()     
    window.addch(Tail[0], Tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_DIAMOND)
