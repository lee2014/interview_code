"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


# Run 20 ms
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m = len(matrix)

        if m == 0:
            return []

        n = len(matrix[0])

        head_x = head_y = 0
        tail_x = m - 1
        tail_y = n - 1
        result = []
        while head_x <= tail_x and head_y <= tail_y:
            i = head_x
            j = head_y
            while i < tail_x or j < tail_y:
                result.append(matrix[i][j])
                if j < tail_y:
                    j += 1
                else:
                    i += 1

            result.append(matrix[i][j])

            j = tail_y - 1
            while i > head_x and j >= head_y:
                result.append(matrix[i][j])
                if j > head_y:
                    j -= 1
                else:
                    i -= 1

            head_x += 1
            head_y += 1
            tail_x -= 1
            tail_y -= 1

        return result


if __name__ == "__main__":
    solution = Solution()

    test1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print solution.spiralOrder(test1)

    test2 = [
        [1]
    ]
    print solution.spiralOrder(test2)

    test3 = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12]
    ]
    print solution.spiralOrder(test3)

    test4 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    print solution.spiralOrder(test4)

    test5 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
    print solution.spiralOrder(test5)

    test6 = [range(i, i+4) for i in range(1, 13, 4)]
    print solution.spiralOrder(test6)

    test7 = [[1], [2]]
    print solution.spiralOrder(test7)

    test8 = [[6, 7, 8, 9]]
    print solution.spiralOrder(test8)
