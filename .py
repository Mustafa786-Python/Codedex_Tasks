tries = 0
guess = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess a number: "))
  tries += 1
  if tries == 5:
      print("You are out of turn")

if guess == 6:
  print("You got it!")
