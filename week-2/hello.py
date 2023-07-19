
correctAnswers = ["your name", "name", "my name"]

attempts = 0

while attempts < 2:
    x = input("type answer: ")
    x.lower()

    if (x in correctAnswers):
        print("\nTroll: 'Well done, small one. You have passed the test. You may proceed, but be careful, you may not succeed.'")
        break
    else:
        if (attempts == 0):
            print("\nSorry, little one. That is incorrect. One more chance or you'll never advance.")
            # -1 life
            # check game over
        if (attempts == 1):
            print("\nMy, my, little one... You have failed the test, you can no longer progress. \nThe shadow demon caught up to you, killing you where you stand from behind. This was the end for Harvey Staker.")
            # lose all lives
            # check game over
    
    attempts += 1
