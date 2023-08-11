# Enter a number and have the program generate e up to that many decimal places.
# Keep a limit to how far the program will go.


def return_decimals(dp):
    e_decimals = '7182818284590452353602874'
    print('e is equal to: \n** 2.{} ** to {} decimal places'.format(e_decimals[1:dp], dp))


def get_decimals():
    while True:
        try:
            decimals = int(input('How many decimal places would you like to see?\n--->>  '))
        except ValueError:
            print('This is an invalid entry')
        else:
            if decimals not in range(1, 25):
                print('This is an invalid entry. Enter a number from 1 to 25')
            else:
                break
    return decimals


print('Welcome, This program generates e up to the decimal points you input [1-25] decimal places.')
play_again = ''
while True:
    decimal_places = get_decimals()
    return_decimals(decimal_places)
    play_again = input('Do you want to do it again? y or n\n--->>  ')
    while play_again not in ['y', 'n']:
        print('This is an invalid input enter either y or n')
        play_again = input('Do you want to do it again? y or n')
    if play_again == 'y':
        continue
    else:
        print('Program ending...')
        break

# Took me 35 minutes to write
