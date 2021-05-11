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
        pass

    def calculate(self):
        pass
