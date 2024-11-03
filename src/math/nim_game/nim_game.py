from nim_engine import put_stones, get_bunches, is_gameover, take_from_bunch
from termcolor import cprint, colored

put_stones()
current_player = 1

while True:
    cprint('Current Position:', color='green')
    cprint(get_bunches(), color='green')
    player_color = 'blue' if current_player == 1 else 'yellow'
    cprint('Player {}\'s Turn'.format(current_player))
    try:
        from_bunch = int(input(colored('From which bunch?')))
        quantity = int(input(colored('How many stones?')))
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting.")
        break
    except ValueError:
        cprint('Invalid input! Please enter a number.', color='red')
        continue

    bunches = get_bunches()
    if from_bunch < 1 or from_bunch > len(bunches):
        cprint('Invalid bunch number!', color='red')
        continue
    if quantity > bunches[from_bunch - 1]:
        cprint('You can\'t take more stones than there are in the bunch!', color='red')
        continue
    if quantity <= 0:
        cprint('You must take at least one stone!', color='red')
        continue

    step_succeed = take_from_bunch(position=from_bunch, quantity=quantity)
    if step_succeed:
        current_player = 2 if current_player == 1 else 1
    else:
        cprint('Invalid move!', color='red')
    if is_gameover():
        break

cprint('Player {} wins!'.format(current_player), color='red')