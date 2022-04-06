import curses
import random
from curses import wrapper
import time

try:

    def main(stdscr):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        red = curses.color_pair(2)
        height, width = stdscr.getmaxyx()
        snake = [[1, 1], [1, 2], [1, 3]]
        direction = None
        old_direction = None
        curses.cbreak()
        stdscr.nodelay(1)
        win = curses.newwin(height - 4, width - 4, 2, 2)
        food = []
        global food_gotten
        food_gotten = 0
        global final_length
        final_length = 3
        runloops = 0
        def foodgen():
            randy = random.randint(0, height - 2)
            randx = random.randint(0, width - 2)
            food.append([randy, randx])



        while True:
            stdscr.clear()
            # stdscr.attron(red)
            # stdscr.border()
            # stdscr.attroff(red)
            stdscr.timeout(75)
            head = snake[-1]
            for piece in snake:
                posy = piece[0]
                posx = piece[1]
                stdscr.addstr(posy, posx, '\u2588', curses.color_pair(1))
            if runloops == 0:
                foodgen()
                stdscr.addstr(food[0][0], food[0][1], '\u2588', curses.color_pair(2))
            if head == food[0]:
                food_gotten += 1
                final_length += 3
                del food[0]
                foodgen()
                stdscr.addstr(food[0][0], food[0][1], '\u2588', curses.color_pair(2))
                snake.insert(0, [snake[0][0], snake[0][1]])
                snake.insert(0, [snake[0][0], snake[0][1]])
                snake.insert(0, [snake[0][0], snake[0][1]])
            for bit in snake[:-1]:
                if head == bit:
                    raise curses.error()
            key = stdscr.getch()
            if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
                old_direction = direction
                direction = key
            if direction == curses.KEY_RIGHT:
                if old_direction == curses.KEY_LEFT:
                    del snake[0]
                    snake.append([snake[-1][0], snake[-1][1]-1])
                    continue
                del snake[0]
                snake.append([snake[-1][0], snake[-1][1]+1])
            elif direction == curses.KEY_DOWN:
                if old_direction == curses.KEY_UP:
                    del snake[0]
                    snake.append([snake[-1][0]-1, snake[-1][1]])
                    continue
                del snake[0]
                snake.append([snake[-1][0]+1, snake[-1][1]])
            elif direction == curses.KEY_LEFT:
                if old_direction == curses.KEY_RIGHT:
                    del snake[0]
                    snake.append([snake[-1][0], snake[-1][1]+1])
                    continue
                del snake[0]
                snake.append([snake[-1][0], snake[-1][1]-1])
            elif direction == curses.KEY_UP:
                if old_direction == curses.KEY_DOWN:
                    del snake[0]
                    snake.append([snake[-1][0]+1, snake[-1][1]])
                    continue
                del snake[0]
                snake.append([snake[-1][0]-1, snake[-1][1]])
            stdscr.refresh()
    wrapper(main)
except curses.error:
    print(f"Your final score was: {food_gotten}")
    print(f"Your final length was: {final_length}")

# aw = width - 1
# ah = height - 1
#
# for x in range(width):
#     if x == 0:
#         stdscr.addstr(0, x,'\u250f', curses.color_pair(2))
#         stdscr.addstr(ah-1, x, '\u2517', curses.color_pair(2))
#     else:
#         stdscr.addstr(0, x,'\u2501', curses.color_pair(2))
#         stdscr.addstr(ah-1, x, '\u2501', curses.color_pair(2))
#
# for y in range(ah):
#     if y == 0:
#         stdscr.addstr(y, aw,'\u2513', curses.color_pair(2))
#     elif y == ah - 1:
#         stdscr.addstr(y, aw,'\u251b', curses.color_pair(2))
#     else:
#         stdscr.addstr(y, 0,'\u2503', curses.color_pair(2))
#         stdscr.addstr(y, aw,'\u2503', curses.color_pair(2))
