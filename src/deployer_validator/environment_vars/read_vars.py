import os


def get_var(var_name):
    if var_name in os.environ:
        print(f'{var_name} value is {os.environ[var_name]}')
    else:
        print(f'{var_name} does not exist')


def print_all():
    print()
    print("Current Environment Variables:")
    print("==============================")
    for k, v in os.environ.items():
        print(f'{k}={v}')
