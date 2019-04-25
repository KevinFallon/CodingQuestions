
# 15.2 N-Queens problem
def n_queens(board):
  # don't need to check if in same column
  def is_safe(board, row, column):
    # if not in same row
    # if not in diagonal with another '1'
    if 1 in board[row]:
      return False

    for r,c in zip(range(row,-1,-1), range(column,-1,-1)):
      if 1 == board[r][c]:
        return False

    for r,c in zip(range(row, len(board[0]), 1), range(column, -1, -1)):
      if 1 == board[r][c]:
        return False
    return True

  def place(board, row, column):
    board[row][column] = 1

  def remove(board, row, column):
    board[row][column] = 0

  def queens_helper(board, column):
    if column == len(board):
      for row in board:
        print(row)
      print('-------------------')
    else:
      for row in range(0, len(board)):
        if is_safe(board, row, column):
          # choose
          place(board, row, column)
          # explore
          queens_helper(board, column+1)
          # unchoose
          remove(board, row, column)
  queens_helper(board, 0)


board = [
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
]
# n_queens(board)
