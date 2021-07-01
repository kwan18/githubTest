import turtle
wn = turtle.Screen()
wn.setup(400,400)
print('End variable: ')
end = input()
end = int(end)

t1 = turtle.Turtle()
wn.bgcolor("light yellow")
t1.pencolor("Green")
i = 0
while i < end:
  direction = input('Please input a direction [l, r, f, b]\n')
  if direction == 'l':
    t1.left(150)
  elif direction == 'r':
    t1.right(150)
  elif direction == 'f':
    t1.forward(150)
  elif direction == 'b':
    t1.backward(150)
  else:
    print("Please input a valid direction!")
  i = i + 1

