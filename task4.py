import random

def roll_the_dice(code):
    dices = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    res = 0
    for d in dices:
        if d in code:
            try:
                code1 = code.split(d)
                d = int(d[1:])
                if code1[0] != '' and code1[1] == '':
                    x = int(code1[0])
                    for _ in range(x):
                        res += random.randint(1, d)
                elif code1[0] == '' and code1[1] != '':
                    z = int(code1[1])
                    res = random.randint(1, d) + z
                elif code1[0] != '' and code1[1] != '':
                    x = int(code1[0])
                    z = int(code1[1])
                    for _ in range(x):
                        res += random.randint(1, d)
                    res = res + z
                else:
                    res = random.randint(1, d)
            except ValueError:
                return 'Code error, try again!'
            break
    else:
        return 'Code error, try again!'

    return res


users_dice = input('Put a dice code: ')
print(roll_the_dice(users_dice))

while roll_the_dice(users_dice) == 'Code error, try again!':
    users_dice = input('Put a dice code: ')
    print(roll_the_dice(users_dice))
