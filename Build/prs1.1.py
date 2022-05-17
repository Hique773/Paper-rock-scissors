import random

def play():
    user = input("Qual a sua escolha? 'p' para pedra, 'pp' papel, 't' para tesoura\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\s a tie'

        # p > t, t > pp, pp > p

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # true se player ganhar
    # p > t, t > pp, pp > p
    if (player == 'p' and opponent == 't') or (player == 't' and opponent == 'pp') \
        or (player == 'pp' and opponent == 'p'):
        return True

print (play())