import random

PASSWORD_CHARS = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def gen_pass(length: int) -> str:
    """Generate a random password of the given length."""
    if length < 1:
        raise ValueError("Password length must be at least 1")

    return ''.join(random.choice(PASSWORD_CHARS) for _ in range(length))