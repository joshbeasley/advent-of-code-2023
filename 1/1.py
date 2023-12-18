file = open("calibration.txt", "r")
lines = file.readlines()

digits = {'one':1,
          'two':2, 
          'three':3, 
          'four':4, 
          'five':5, 
          'six':6, 
          'seven':7, 
          'eight':8, 
          'nine':9,
          '1':1,
          '2':2,
          '3':3,
          '4':4,
          '5':5,
          '6':6,
          '7':7,
          '8':8,
          '9':9}

total = 0
for line in lines:
  first = -1
  last = -1
  for key in digits.keys():
    if key in line and (first == -1 or line.index(key) < line.index(first)):
      first = key
      if last == -1:
        last = key
    if key in line and line.rfind(key) > line.rfind(last):
      last = key
    
  total += digits[first] * 10 + digits[last]

print(total)