import random
secret=random.randint(1,10)
guess=0
attempts=0
while guess!=secret:
    guess=int(input("Guess(1-10): "))
    attempts=attempts+1
    if guess<secret:
        print("Too Low")
    elif guess>secret:
        print("Too High")
print("Correct attempts: {}".format(attempts))