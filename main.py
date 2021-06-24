import sys
from ceiling_fan import CeilingFan


def main():
    print('Welcome to ceiling fan simulator.')
    print('Generating fan...')
    fan = CeilingFan()
    print('Fan generated!')
    print_state(fan)
    print('When prompted, please enter the corresponding number and hit enter to pull one of the cords.')

    while True:  # Entering an infinite loop
        prompt()

        try:
            user_input = int(input())  # Tries to validate user input as int
            if 0 <= user_input <= 2:  # Makes sure user input is within the options in the prompt
                if user_input == 0:
                    break  # Closes the command line
                elif user_input == 1:
                    fan.reverse_direction()
                elif user_input == 2:
                    fan.cycle_speeds()

                print_state(fan)
            else:
                print('What you entered was not an option. Please try again. \n')
        except ValueError:
            print('What you entered was not an option. Please try again. \n')


def prompt():
    print('What would you like to do?')
    print('1 - Pull reverse cord.')
    print('2 - Pull speed cord.')
    print('0 - Exit the simulation.')


def print_state(fan):
    if fan.current_speed == 0:
        print('The fan is off. \n')
        return
    print('The fan is spinning {} at speed {}. \n'.format(fan.current_direction, fan.current_speed))


if __name__ == '__main__':
    main()
