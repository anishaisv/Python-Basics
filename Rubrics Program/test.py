from main import trivia_fetch

# Test 1
def test_trivia_42():
  assert trivia_fetch(42)["number"] == 42

# Test 2
def test_trivia_1000():
  assert trivia_fetch(1000)["number"] == 1000




# !python -m pytest test.py
# What pytest Does:Searches your file (test_main.py) for any functions starting with test_
#  It then automatically calls that function. You don’t need to manually call test_trivia_42().pytest handles that for you.

