import random


def just_wasting_time():
    for i in range(5):
        num = random.randint(0, 10)
        print(num)


just_wasting_time()


def just_wasting_time_two():
    total = 0
    while total < 102:
        print(total )
        total += 1


just_wasting_time_two()


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


r = random.randint(1, 9)
fortune = getAnswer(r)


print(fortune)


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('can not divide by zero please enter a number greater than zero.')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))



