# Enter a number and have the program generate pi up to that many decimal places. Keep a limit to how far the program will go.

def length(dp):
    decimals = '141592653589793238462643'
    print('3.{}'.format(decimals[0:dp]))


print("This program generates pi up to a certain number of decimal places specified by you\nTHis program ends at 25 decimal places")
game_on = 1
while game_on == 1:
    decimal_places = 0
    while decimal_places not in range(1, 26):
        try:
            decimal_places = int(input('Enter the number of decimal places you want:\n--->>  '))
        except ValueError:
            print('This is an invalid input')
        else:
            if decimal_places > 25 or decimal_places < 1:
                print('This is an invalid input, program only goes from 1, up to 25 decimal places.')
    length(decimal_places)
    replay = ''
    while replay not in ['y', 'n']:
        replay = input('Do you want to play again? y or n\n--->>  ')
        if replay == 'y':
            continue
        elif replay == 'n':
            print('Program Ending...')
            game_on = 0
        else:
            print('This is an invalid input')
