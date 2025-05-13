from .fr import draw_boxes, draw_fox

def test_draw_boxes_works_as_expected():
  basic_state = [
      [None, "F", "R"],
      [None, "F", "R"],
      [None, "F", "R"],
  ]

  result = draw_boxes(basic_state)

  assert result == """-FR
-FR
-FR
"""

def test_grow_foxes():
  basic_state = [
      [None, None, None],
      [None, None, None],
      [None, None, None]
  ]

  result = draw_fox((1, 1), basic_state)

  assert result == [
      [None, None, None],
      [None, "F", None],
      [None, None, None],
  ]

def test_grow_foxes_2():
  basic_state = [
      [None, None, None],
      [None, "F", None],
      [None, None, None],
  ]

  result = draw_fox((1, 1), basic_state)

  assert result == [
      ["F", "F", "F"],
      ["F", "F", "F"],
      ["F", "F", "F"],
  ]

def test_grow_foxes_3():
  basic_state = [
      [None, None, None],
      [None, None, None],
      [None, None, "F"],
  ]

  result = draw_fox((2, 2), basic_state)

  assert result == [
      [None, None, None],
      [None, "F", "F"],
      [None, "F", "F"],
  ]
