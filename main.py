from formulae import lowest_common_multiple


class SimultaneousEquationSolver:

    def __init__(self):
        self.x, self.y = None, None
        self.eqn1 = [0, 0, 0]
        self.eqn2 = [0, 0, 0]
        self.result = [0, 0, 0]

    def input_values(self):
        print("""Please enter values in the following format:
                          ax + by = c1
                          dx + ey = c2""")

        self.eqn1[0] = int(input("Enter value a: "))
        self.eqn1[1] = int(input("Enter value b: "))
        self.eqn1[2] = int(input("Enter value c1: "))
        self.eqn2[0] = int(input("Enter value d: "))
        self.eqn2[1] = int(input("Enter value e: "))
        self.eqn2[2] = int(input("Enter value c2: "))

    def amend_values(self):
        # calculate what to multiply the equations by for elimination
        lcm = lowest_common_multiple(self.eqn1[0], self.eqn2[0])
        multiplier1 = lcm / self.eqn1[0]
        multiplier2 = lcm / self.eqn2[0]

        # use the calculated multipliers
        self.eqn1[0] *= multiplier1
        self.eqn1[1] *= multiplier1
        self.eqn1[2] *= multiplier1

        self.eqn2[0] *= multiplier2
        self.eqn2[1] *= multiplier2
        self.eqn2[2] *= multiplier2

        # eliminate values and store in self.result list
        if self.eqn1[0] * self.eqn2[0] > 0:  # checks if they are the same sign (for Same Sign Subtract)
            for i in range(3):
                self.result[i] = self.eqn1[i] - self.eqn2[i]
        else:
            for i in range(3):
                self.result[i] = self.eqn1[i] + self.eqn2[i]

    def calculate(self):
        self.amend_values()

        # if there are no/infinite solutions, there will be a division by zero.
        # perhaps extend to state no or infinite solutions?
        try:
            # simple rearranging to solve y and x
            self.y = self.result[2] / self.result[1]
            self.x = (self.eqn1[2] - (self.eqn1[1] * self.y)) / self.eqn1[0]
        except ZeroDivisionError:
            return
