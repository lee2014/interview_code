#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2018/12/2'


# Run 48 ms
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        int_row_table = [[0 for _ in range(9)] for _ in range(9)]
        int_col_table = [[0 for _ in range(9)] for _ in range(9)]
        int_box_table = [[0 for _ in range(9)] for _ in range(9)]

        def sub_box_id(x, y):
            pre_x = x / 3
            pre_y = y / 3

            return pre_x * 3 + pre_y

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == '.':
                    continue
                else:
                    v = int(v) - 1

                if int_row_table[i][v] == 1:
                    return False

                if int_col_table[j][v] == 1:
                    return False

                box_id = sub_box_id(i, j)
                if int_box_table[box_id][v] == 1:
                    return False

                int_row_table[i][v] = 1
                int_col_table[j][v] = 1
                int_box_table[box_id][v] = 1

        return True


if __name__ == "__main__":
    test = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print Solution().isValidSudoku(test)
