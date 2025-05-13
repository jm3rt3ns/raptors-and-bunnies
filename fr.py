def draw_boxes(board):
  board_string = ""
  for row in board:
    row_string = ""
    for item in row:
      if item == "F":
        row_string += "F"
      elif item == "R":
        row_string += "R"
      else:
        row_string += "-"
    print(f"{row_string}")
    board_string += row_string + "\n"
  return board_string

def draw_fox(fox_location, game_state):
  # TODO: check for out of index exceptions

  x = fox_location[0]
  y = fox_location[1]
  pos_state = game_state[x][y]
  result = game_state
  if pos_state == None:
    result[x][y] = "F"
  elif pos_state == "F":
    # expand to all adjacent ones
    for xpos in range(min(0, x-1), min(x+2, len(result))):
      row_to_edit = result[xpos]
      for ypos in range(min(0, y-1), min(y+2, len(row_to_edit))):
        print(xpos, ypos)
        result[xpos][ypos] = "F"

  return result

def game_loop(state):
  # grow the rabbits into adjacent empty spaces based on growth rate

  # grow the foxes into adjacent empty spaces based on growth rate

  # foxes kill any adjacent rabbits

  # foxes die when they reach their max age
  pass

if __name__ == "__main__":
  # init a board

  # choose a random starting point for the fox

  # choose a random starting point for the rabbit

  # run the game loop
  game_loop([])
