def hello():
    print("Hello!")

def pack(a,b,c):
  return [a,b,c]

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("No lunch")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello()
print(pack("a","b","c"))
eat_lunch(["pasta","carrots","apple","juice"])