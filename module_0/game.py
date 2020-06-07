import numpy as np


def game_core_v1(number):
    """Just guessing the number randomly (not using information about the selected number anyhow).
    Function accepts the number to guess and
    returns the number of attempts were made to complete the guess."""

    count = 0

    while True:
        count += 1
        predict = np.random.randint(1, 101)

        if number == predict:
            return count


def game_core_v2(number):
    """Taking random number. Then increase or decrease it depending on the direction to correct.
    Function accepts the number to guess and
    returns the number of attempts were made to complete the guess."""

    count = 1
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


def game_core_v3(number):
    """Taking random number. Then use binary search to guess the number.
    Function accepts the number to guess and
    returns the number of attempts were made to complete the guess."""

    count = 1
    low_limit = 1
    high_limit = 100
    predict = np.random.randint(low_limit, high_limit + 1)

    while number != predict:
        count += 1
        if number > predict:
            low_limit = predict + 1
        elif number < predict:
            high_limit = predict - 1
        predict = low_limit + (high_limit - low_limit) // 2

    return count


def game_core_v4(number):
    """Use binary search to guess the number.
    Function accepts the number to guess and
    returns the number of attempts were made to complete the guess."""

    count = 1
    low_limit = 1
    high_limit = 100
    predict = low_limit + (high_limit - low_limit) // 2

    while number != predict:
        count += 1
        if number > predict:
            low_limit = predict + 1
        elif number < predict:
            high_limit = predict - 1
        predict = low_limit + (high_limit - low_limit) // 2

    return count


def score_game(game_core):
    """launch the game 1000 times and evaluate AI performance (average number of attempts to guess)"""

    count_ls = []
    np.random.seed(1)  # making experiment deterministic and reproducible

    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# score_game(game_core_v1)
# score_game(game_core_v2)
# score_game(game_core_v3)
score_game(game_core_v4)
