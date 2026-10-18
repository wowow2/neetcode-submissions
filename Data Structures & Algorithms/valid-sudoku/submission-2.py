class Solution:
    def _is_valid_group(self, cells: List[str]) -> bool:
        nums = [c for c in cells if c != "."]
        return len(nums) == len(set(nums))
    
    def _transpose_board(self, board: List[List[str]]):
        transposed = list(zip(*board))
        return transposed

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        transposed_board = self._transpose_board(board)
        for group in board + self._transpose_board(board):
            if not self._is_valid_group(group):
                return False
        
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                box = [board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]
                if not self._is_valid_group(box):
                    return False
        return True

        