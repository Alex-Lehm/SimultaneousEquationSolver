from formulae import lowest_common_multiple

# TODO: Remove any user input from this class. Should be handled elsewhere
# TODO: Add class and method docstrings


class SimultaneousEquationSolver:
    """Class to represent a dedicated object to solving (by elimination) linear, 2D simultaneous equations,
    for example:

    3x + 2y = 4

    2x + 3y = 6"""

    def __init__(self):
        """Constructor method, creates the following instance variables:

        x, y -- the calculated values of the unknowns
        eqn1, eqn2 -- lists holding the known values for each equation in the form [0]x + [1]y = [2]
        result -- the result of elimination between eqn1 and eqn2"""
        self.x, self.y = None, None
        self.eqn1 = [0, 0, 0]
        self.eqn2 = [0, 0, 0]
        self.result = [0, 0, 0]

    def input_equations(self, eqn1, eqn2):
        """Method to take user input for the known values"""

        self.eqn1 = eqn1
        self.eqn2 = eqn2

    def amend_values(self):
        """Method to prepare equations for the elimination step, and carry out elimination.
        Calculates the necessary multiplier for each equation."""

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

    def calculate_unknowns(self):
        """Method to calculate the unknown values using the result of elimination between the two
        equations.

        Throws a ZeroDivisionError if there are no or infinite solutions to the equations."""

        self.amend_values()

        # if there are no/infinite solutions, there will be a division by zero.
        # perhaps extend to state no or infinite solutions?
        try:
            # simple rearranging to solve y and x
            self.y = self.result[2] / self.result[1]
            self.x = (self.eqn1[2] - (self.eqn1[1] * self.y)) / self.eqn1[0]
        except ZeroDivisionError:
            return
