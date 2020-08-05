import pytest
from src import solver

@pytest.fixture
def simple_solver():
    sliders = [range(1,10) for i in range(2)]
    _eval = lambda x : x[0] * x[1]

    return solver.Solver(sliders, _eval)



