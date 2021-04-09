import subprocess
import os


def flip_coin():
    try:
        command = "{}/scripts/flip_coin.sh".format(os.path.dirname(__file__))
        res = subprocess.check_output(command)
        res = res.decode('utf-8').strip('\n')
        if res == '1':
            msg = "Current Coin flip result is: One"
        elif res == '0':
            msg = "Current Coin flip result is: Two"
        else:
            msg = "Flip Coin returned the wrong value: {}".format(res)
        print('\n' + msg + '\n')
    except Exception as error:
        print("Failed to flip the coin with error: {0}".format(error.__doc__))
