from SimEqnSolver import SimultaneousEquationSolver as EqnSolver

# test function names refer to the equations - test_solver_1_2
# where 1 and 2 can be 'positive' or 'negative', 1 representing the first equation
# and 2 representing the second equation.
# Positive means there are no negatives in the equation, negative means there is at least one negative in the equation.


def test_main_positive_positive():
    solver = EqnSolver()
    solver.eqn1 = [5, 3, 41]
    solver.eqn2 = [2, 3, 20]

    solver.calculate_unknowns()

    assert solver.x == 7
    assert solver.y == 2

    solver.eqn1 = [1, 7, 64]
    solver.eqn2 = [1, 3, 28]

    solver.calculate_unknowns()

    assert solver.x == 1
    assert solver.y == 9


def test_main_positive_negative():
    solver = EqnSolver()
    solver.eqn1 = [5, 1, 11]
    solver.eqn2 = [3, -1, 9]

    solver.calculate_unknowns()

    assert solver.x == 2.5
    assert solver.y == -1.5


def test_main_negative_positive():
    solver = EqnSolver()
    solver.eqn1 = [2, -4, 14]
    solver.eqn2 = [4, 4, 4]

    solver.calculate_unknowns()

    assert solver.x == 3
    assert solver.y == -2


def test_main_negative_negative():
    solver = EqnSolver()
    solver.eqn1 = [4, -4, 24]
    solver.eqn2 = [1, -4, 3]

    solver.calculate_unknowns()

    assert solver.x == 7
    assert solver.y == 1

    solver.eqn1 = [-3, 1, 3]
    solver.eqn2 = [1, -2, 4]

    solver.calculate_unknowns()

    assert solver.x == -2
    assert solver.y == -3

    solver.eqn1 = [4, -1, 17]
    solver.eqn2 = [-1, 1, -2]

    solver.calculate_unknowns()

    assert solver.x == 5
    assert solver.y == 3


def test_main_erroneous():
    solver = EqnSolver()

    solver.eqn1 = [2, 3, 4]
    solver.eqn2 = [4, 6, 5]

    solver.calculate_unknowns()

    assert solver.x is None
    assert solver.y is None

    solver.eqn1 = [2, 3, 4]
    solver.eqn2 = [4, 6, 8]

    solver.calculate_unknowns()

    assert solver.x is None
    assert solver.y is None
