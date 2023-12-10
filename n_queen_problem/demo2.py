
class NQueens:

    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for _ in range(n)] for _ in range(n)]

    def get_ans(self):
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
        print(f"Check for 1 {row_index, col_index}")
        col = col_index
        for row in range(row_index, self.n):
            col += 1
            if col >= self.n:
                break
            if self.chess_table[row][col] == 1:
                return False

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
            print(f"\t Check for inside fun 1 {row, col}")
            if self.chess_table[row][col] == 1:
                return False

        return True

    def check_cross_right_left(self, row_index, col_index):
        print(f"Check for 2 {row_index, col_index}")
        col = col_index
        for row in range(row_index - 1, -1, -1):
            col -= 1
            if col < 0:
                break
            print(f"\t Check for inside fun 1 {row, col}")
            if self.chess_table[row][col] == 1:
                return False

        col = col_index
        for row in range(row_index + 1, self.n):
            col += 1
            if col >= self.n:
                break
            print(f"\t Check for inside fun 2 {row, col}")
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
no_of_queen = 4
queens = NQueens(no_of_queen)
queens.chess_table[1][1] = 1
ans = queens.solve_problem()
print(ans)
queens.print_queens()
