# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def define_fibonacci(n):
    number = 1
    total = 0
    sequence = []
    for num in range(0, n):
        total += number
        number = total
        sequence.append(total)
    return str(sequence)


print('This is a fibonacci sequence program, Enter a number and it will generate the fibonacci sequence up to that number\n')
while True:
    try:
        end = int(input('What do you want your sequence to go up to?\n--->>  '))
    except ValueError:
        print('THis is an invalid input ')
    else:
        fibonacci_sequence = define_fibonacci(end)
        print(fibonacci_sequence)
    replay = input('Do you want to run the program again? [y or n]\n--->>  ')
    while replay not in ['y', 'n']:
        print('This is an invalid entry, [y or n]')
        replay = input('Do you want to run the program again? [y or n]\n--->>  ')
    if replay == 'y':
        continue
    else:
        print('Program ending...')
        break
