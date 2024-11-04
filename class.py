class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError("Start value must be within the min and max limits")

    def set_max(self, max_value):
        if max_value >= self.min_value:
            self.max_value = max_value
        else:
            raise ValueError("Max value must be greater than or equal to min value")

    def set_min(self, min_value):
        if min_value <= self.max_value:
            self.min_value = min_value
        else:
            raise ValueError("Min value must be less than or equal to max value")

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Maximum limit reached")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Minimum limit reached")

    def get_current(self):
        return self.current



counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # Should raise ValueError
except ValueError as e:
    print(e)  # Output: "Maximum limit reached"
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # Should raise ValueError
except ValueError as e:
    print(e)  # Output: "Minimum limit reached"
assert counter.get_current() == 7, 'Test4'
