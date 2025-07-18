from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_rc(square: int) ->Tuple[int, int]:
            quot, rem = divmod(square - 1, n)
            row = n - 1 - quot
            col = rem if quot% 2 == 0 else n - 1 - rem
            return row, col

        visited = set()
        q = deque()
        q.append((1, 0))

        while q:
            square, moves = q.popleft()
            if square == n*n:
                return moves
            for i in range(1,7):
                next_square = square + i
                if next_square > n * n:
                    continue
                r, c  = get_rc(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))
                
        return -1
