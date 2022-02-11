"""
--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
"""


def puzzle_part_one():

    def check_number_on_board(board, chosen_number):
        for row in board:
            if chosen_number in row:
                row[row.index(chosen_number)] = chosen_number + "*"
            
            # Check winning row
            if all('*' in number for number in row): # This row is the winner
                return True
            
        success = check_winning_column(board)
        return success

    def check_winning_column(board):
        for column in range(5):
            count = 0
            for row in range(5):
                if '*' in board[row][column]:
                    count += 1
            if count == 5: #This column in the winner
                return True

        return False


    puzzle_input = open("puzzle_input.txt", "r")
    chosen_numbers = []
    bingo_boards = {}
    i = 0
    for line in puzzle_input.readlines():
        if not chosen_numbers:
            chosen_numbers = line.rstrip('\n').split(",")
        else:
            if line == '\n':
                i += 1
                bingo_boards["board_{}".format(i)] = []
            else:
                line = line.rstrip('\n').split(" ")
                if 5 < len(line):
                    line = [value for value in line if value != ""] # Removes empty elements
                bingo_boards["board_{}".format(i)].append(line)
    
    try:
        for chosen_number in chosen_numbers:
            for board in bingo_boards:
                success = check_number_on_board(bingo_boards[board], chosen_number)
                if success:
                    raise StopIteration
    except StopIteration:
        count = 0
        for row in bingo_boards[board]:
            for number in row:
                count += int(number) if '*' not in number else 0

        final_result = count * int(chosen_number)
        return final_result

        


"""
--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""

def puzzle_part_two():

    def check_number_on_board(board, chosen_number):
        for row in board:
            if chosen_number in row:
                row[row.index(chosen_number)] = chosen_number + "*"
            
            # Check winning row
            if all('*' in number for number in row): # This row is the winner
                return True
            
        success = check_winning_column(board)
        return success

    def check_winning_column(board):
        for column in range(5):
            count = 0
            for row in range(5):
                if '*' in board[row][column]:
                    count += 1
            if count == 5: #This column in the winner
                return True

        return False


    puzzle_input = open("puzzle_input.txt", "r")
    chosen_numbers = []
    bingo_boards = {}

    winning_boards = []
    winning_numbers = []
    i = 0
    for line in puzzle_input.readlines():
        if not chosen_numbers:
            chosen_numbers = line.rstrip('\n').split(",")
        else:
            if line == '\n':
                i += 1
                bingo_boards["board_{}".format(i)] = []
            else:
                line = line.rstrip('\n').split(" ")
                if 5 < len(line):
                    line = [value for value in line if value != ""] # Removes empty elements
                bingo_boards["board_{}".format(i)].append(line)
    
    for chosen_number in chosen_numbers:
        for board in bingo_boards:
            if board not in winning_boards: # Validation to not mark a number in a winner board.
                success = check_number_on_board(bingo_boards[board], chosen_number)
                if success:
                    winning_boards.append(board)
                    winning_numbers.append(chosen_number)

    count = 0
    for row in bingo_boards[winning_boards[-1]]:
        for number in row:
            count += int(number) if '*' not in number else 0

    final_result = count * int(winning_numbers[-1])
    return final_result


print("Part One - Puzzle Answer: {}".format(puzzle_part_one()))
print("Part Two - Puzzle Answer: {}".format(puzzle_part_two()))