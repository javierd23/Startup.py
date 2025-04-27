


score = 0
smallest_score = None
largest_score = None


while score >= 0:

    score = int(input('score: '))
    if score <= 0:
        break

    if largest_score is None:
        largest_score = score
    elif score > largest_score:
        largest_score = score

    if smallest_score is None:
        smallest_score = score

    elif score < smallest_score:
        smallest_score = score

# print(f"this is the lowest score {smallest_score},and this is the highest score {largest_score}")


#this is to get only one score which is the highest.

score2 = 0
tolta_score2 = 0

while score2 >= 0:
    score2 = int(input('Score: '))
    if score2 >= 0:
        tolta_score2 += score2
    else:
        break

print(tolta_score2)



