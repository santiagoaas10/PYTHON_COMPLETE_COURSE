def testing_errors():
    user_input = 'd'
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid.')
    finally:
        n_square = n ** 2
        return n_square

value = testing_errors()
print(value)