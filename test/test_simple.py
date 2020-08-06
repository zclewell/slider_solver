import pytest

def test_simple_solver_min(simple_solver):
    sliders = simple_solver.sliders
    _eval = simple_solver._eval

    dims = len(sliders)
    point = tuple([0 for i in range(dims)])
    target = _eval(point)

    actual = simple_solver.solve(target)
    assert target == _eval(actual)
    assert actual == point

def test_simple_solver_max(simple_solver):
    sliders = simple_solver.sliders
    _eval = simple_solver._eval

    dims = len(sliders)
    point = tuple([len(sliders[i]) - 1 for i in range(dims)])
    target = _eval(point)

    actual = simple_solver.solve(target)
    assert target == _eval(actual)
    assert actual == point

def test_simple_solver_inexact(simple_solver):
    sliders = simple_solver.sliders
    _eval = simple_solver._eval

    dims = len(sliders)
    point =  tuple([len(sliders[i]) - 1 for i in range(dims)])
    best = _eval(point)
    target = best - 1

    actual = simple_solver.solve(target)
    assert best == _eval(point)
    assert actual == point    