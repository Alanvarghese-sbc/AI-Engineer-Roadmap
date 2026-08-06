secret = 7
attempt = 0

while True:
    guess = int(input("Guess : "))
    attempt+=1
    if guess == secret:
        print(f"Correct Guess in {attempt} attempt")
        break
    else:
        print("Try /////")