

from random import randint

target = randint(1,10)

attempt = 0


while True:
    attempt= attempt+1
    
    number = int(input("guess the number : "))

    if number == target:

        print(f"attempt{attempt}")

        print("congrats")

        break

   

   