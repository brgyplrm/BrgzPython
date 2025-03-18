# Boolean return True
#any string returns TRUE except empty
bool("abc")

#any int returns TRUE except 0
bool(123)

#any list, dict, or tuple returns TRUE except empty
bool(["apple", "cherry", "banana"])

# Boolean returns false
#bool(False) 
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

class myclass():
  def __len__(self):
    return 1

myobj = myclass()
print(bool(myobj))

# Functions that returns Booleans 
def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# Checker if a object is an integer/float/str or not
x = 200
print(isinstance(x, int))
