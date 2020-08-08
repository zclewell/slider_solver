import pytest
from src import solver

@pytest.fixture
def simple_solver():
    sliders = [range(1,10) for i in range(2)]
    _eval = lambda x, sliders=sliders : sliders[0][int(x[0])] * sliders[1][int(x[1])]

    return solver.Solver(sliders, _eval)



