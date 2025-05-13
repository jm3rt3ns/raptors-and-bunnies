from fr import draw_boxes

def test_draw_boxes_works_as_expected():
  basic_state = [
      [None, "F", "R"],
      [None, "F", "R"],
      [None, "F", "R"],
  ]

  result = draw_boxes(basic_state)

  assert result == """
-FR
-FR
-FR
  """

