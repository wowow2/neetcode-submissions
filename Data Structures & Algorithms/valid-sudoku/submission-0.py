class Solution:
    def _valid_rows(self, board: List[List[str]]) -> bool:
        for row in board:
            row = [cell for cell in row if cell != '.']
            if len(row) != len(set(row)):
                return False
        return True
                
    def _transpose_board(self, board: List[List[str]]) -> List[List[str]]:
        return [list(row) for row in zip(*board)]
    
    def _flatten_boxes(self, board: List[List[str]]) -> List[List[str]]:
        flattened_boxes = []
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = [board[i][j] for i in range(r, r+3) for j in range(c, c+3)]
                flattened_boxes.append(box)
            
        return flattened_boxes

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        transposed_board = self._transpose_board(board)
        flattened_boxes = self._flatten_boxes(board)
        
        return (self._valid_rows(board) and 
            self._valid_rows(transposed_board) and 
            self._valid_rows(flattened_boxes))