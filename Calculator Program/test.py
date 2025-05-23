from main import addmultiplenumbers,multiplymultiplenumbers,isiteven,isitaninteger

def test_add_multiple_positive_integers():
  response = addmultiplenumbers([5,7,9])
  assert response == 21

def test_add_multiple_complicated_numbers():
  response = addmultiplenumbers([5,-7,9.3])
  response = round(response,1)
  assert response == 7.3

def test_multiply_multiple_positive_integers():
  response = multiplymultiplenumbers([4,5,6,7])
  assert response == 840

def test_multiply_multiple_complicated_numbers():
  response = multiplymultiplenumbers([4,-5,6.7])
  response = round(response, 0)
  assert response == -134

def test_is_six_even():
  response = isiteven(6)
  assert response == True

def test_is_minus_three_point_eight_even():
  response = isiteven(-3.8)
  assert response == False

def test_is_three_an_integer():
  response = isitaninteger(3)
  assert response == True

def test_is_seven_point_three_an_integer():
  response = isitaninteger(7.3)
  assert response == False