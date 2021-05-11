from main import SimultaneousEquationSolver

if __name__ == "__main__":
    solver = SimultaneousEquationSolver()
    solver.input_values()
    solver.calculate_unknowns()

    print("""x = {}
    y = {}""".format(solver.x, solver.y))
