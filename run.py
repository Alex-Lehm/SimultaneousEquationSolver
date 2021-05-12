from SimEqnSolver import SimultaneousEquationSolver


def demo():
    solver = SimultaneousEquationSolver()

    print("""Please enter values in the following format:
                                  ax + by = c1
                                  dx + ey = c2""")

    eqn1, eqn2 = [0, 0, 0], [0, 0, 0]

    eqn1[0] = int(input("Enter value a: "))
    eqn1[1] = int(input("Enter value b: "))
    eqn1[2] = int(input("Enter value c1: "))
    eqn2[0] = int(input("Enter value d: "))
    eqn2[1] = int(input("Enter value e: "))
    eqn2[2] = int(input("Enter value c2: "))

    solver.input_equations(eqn1, eqn2)
    solver.calculate_unknowns()

    print("""x = {}
    y = {}""".format(solver.x, solver.y))


if __name__ == "__main__":
    demo()
