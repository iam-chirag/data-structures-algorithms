
class NQueens:

    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for _ in range(n)] for _ in range(n)]

    def get_table(self):
        return self.chess_table

    def check_col(self, col_index):
        for i in range(self.n):
            if self.chess_table[i][col_index] == 1:
                return False

        return True

    def check_row(self, row_index):
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False

        return True

    def check_cross_left_right(self, row_index, col_index):

        col = col_index
        for row in range(row_index -1, -1, -1):
            col -= 1
            if col < 0:
                break
            if self.chess_table[row][col] == 1:
                return False

        col = col_index
        for row in range(row_index - 1, -1, -1):
            col += 1
            if col >= self.n:
                break
            if self.chess_table[row][col] == 1:
                return False

        return True

    def check_cross_right_left(self, row_index, col_index):

        col = col_index
        for row in range(row_index + 1, self.n):
            col += 1
            if col >= self.n:
                break
            if self.chess_table[row][col] == 1:
                return False

        col = col_index
        for row in range(row_index + 1, self.n):
            col -= 1
            if col < 0:
                break
            if self.chess_table[row][col] == 1:
                return False

        return True

    def is_place_valid(self, row_index, col_index):

        check_row = self.check_row(row_index)
        if not check_row:
            return False

        check_col = self.check_col(col_index)
        if not check_col:
            return False

        check_col = self.check_cross_left_right(row_index, col_index)
        if not check_col:
            return False

        check_col = self.check_cross_right_left(row_index, col_index)
        if not check_col:
            return False

        return True

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(" Q ", end='')
                else:
                    print(" - ", end='')
            print("\n")

    def solve_problem(self, col_index = 0):
        if col_index == self.n:
            return True

        for row_index in range(self.n):
            if self.chess_table[row_index][col_index] == 1 or self.is_place_valid(row_index, col_index):
                self.chess_table[row_index][col_index] = 1
                if self.solve_problem(col_index + 1):
                    return True
                self.chess_table[row_index][col_index] = 0

        return False


all_ans = []
all_solution = []
no_of_queen = 8

for row in range(0, no_of_queen):
    for col in range(0, no_of_queen):
        print('================================================')
        print(f"Try with ROW: {row} COL: {col}")
        queens = NQueens(no_of_queen)
        queens.chess_table[row][col] = 1
        ans = queens.solve_problem()
        print(f"VALID {ans}")
        if ans:
            queens.print_queens()
            solution = queens.get_table()
            if solution not in all_solution:
                all_solution.append(solution)
                all_ans.append(ans)
            else:
                print(f"patent already exists")
        print('================================================')
        print('\n\n')

print(len(all_ans))
