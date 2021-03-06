
import random # randrange()
import time   # sleep()

# Lotto Number Maker (1-45)

# lotto = []
# for i in range(1, 46):
#     lotto.append(i)


lotto = [i for i in range(1,46)]

# print(lotto)

# Print List

# for i in range(len(lotto)):
#     print('{0:2d} '.format(lotto[i]), end='')
#     if (i + 1) % 10 == 0:
#         print()
# print('\n' + '=' * 30)
    
    
# Lotto Randomizer Manual

for i in range(1000000):
    r = random.randrange(1,45)
    # temp = lotto[0]
    # lotto[0] = lotto[r]
    # lotto[r] = temp
    # Tuple style <->
    lotto[0], lotto[r] = lotto[r], lotto[0]

for i in range(len(lotto)):
    print('{0:2d} '.format(lotto[i]), end='')
    if (i + 1) % 10 == 0:
        print()
print('\n' + '=' * 30)

print('First 6 numbers: ', end='')
for i in range(6):
    print(f'{lotto[i]} ', end='')
    time.sleep(1)
    
print(f'Bonus: {lotto[6]}')

#