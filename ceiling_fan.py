class CeilingFan:
    def __init__(self):
        self.current_speed = 0
        self.current_direction = 'clockwise'

    def cycle_speeds(self):
        if self.current_speed != 3:
            self.current_speed += 1
        else:
            self.current_speed = 0

    def reverse_direction(self):
        if self.current_direction == 'clockwise':
            self.current_direction = 'counter-clockwise'
        else:
            self.current_direction = 'clockwise'
