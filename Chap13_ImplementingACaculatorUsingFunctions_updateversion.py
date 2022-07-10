# SIMPLE+ CALCULATOR APP

def add(x, y):
    """" Adds two numbers """
    return x + y


def subtract(x, y):
    """ Subtracts two numbers """
    return x - y


def multiply(x, y):
    """ Multiples two numbers """
    return x * y


def divide(x, y):
    """Divides two numbers"""
    return x / y


def power(x, y):
    """Performs exponential (power) calculation on operators"""
    return x**y


def floor_divide(x, y):
    """Floor Division
    - The division of operands where the result is the quotient
    in which the digits after the decimal point are removed.
    But if one of the operands is negative, the result is floored, i.e.,
    rounded away from zero (towards negative infinity) −"""
    return x//y


def modulus(x, y):
    """Divides x operand by y operand and returns remainder"""
    return x % y


def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Menu Options are:')
        print('\t1. Add (+)')
        print('\t2. Subtract (-)')
        print('\t3. Multiply (*)')
        print('\t4. Divide (/)')
        print('\t5. Power (**)')
        print('\t6. Floor divide (//)')
        print('\t7. Modulus (%)')
        print('-----------------')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4', '5', '6', '7'):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 7)')
    print('-----------------')
    return user_selection


def check_input(x):
    try:
        a = float(x)
        return True
    except ValueError:
        print('The input must be an integer or float')
        return False


def get_float_input(message):
    value_as_string = input(message)
    while not check_input(value_as_string):
        value_as_string = input(message)
    return float(value_as_string)


def get_numbers_from_user():
    num1 = get_float_input('Input the first number: ')
    num2 = get_float_input('Input the second number: ')
    return num1, num2


def operation_result(menu_choice, n1, n2):
    if menu_choice == '1':
        return add(n1, n2)
    elif menu_choice == '2':
        return subtract(n1, n2)
    elif menu_choice == '3':
        return multiply(n1, n2)
    elif menu_choice == '4':
        return divide(n1, n2)
    elif menu_choice == '5':
        return power(n1, n2)
    elif menu_choice == '6':
        return floor_divide(n1, n2)
    elif menu_choice == '7':
        return modulus(n1, n2)


def check_if_user_has_finished():
    """Checks that the user wants to finish or not.
    Performs some verification of the input."""
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish (y/n): ')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
    return ok_to_finish


def main():
    finished = False
    while not finished:
        result = 0
        # Get the operation from the user
        menu_choice = get_operation_choice()
        # Get the numbers from the user
        n1, n2 = get_numbers_from_user()
        # Select the operation
        result = operation_result(menu_choice, n1, n2)
        print('Result: {:0.3f}'.format(result))
        print('=================')
        # Determine if the user has finished
        finished = check_if_user_has_finished()
    print('Bye')


main()
