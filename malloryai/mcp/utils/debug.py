from sys import stderr


def debug_log(message):
    print(f"{message}", file=stderr, flush=True)
