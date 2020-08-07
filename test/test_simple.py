import pytest
import copy

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
    assert actual == point    

def test_simple_solver_start_pos(simple_solver):
    simple_solver2 = copy.deepcopy(simple_solver)

    sliders = simple_solver.sliders
    _eval = simple_solver._eval

    dims = len(sliders)
    point = tuple([len(sliders[i]) - 1 for i in range(dims)])
    target = _eval(point)

    actual = simple_solver.solve(target)
    assert target == _eval(actual)
    assert actual == point

    actual2 = simple_solver2.solve(target, start_pos=point)
    assert target == _eval(actual2)
    assert actual2 == point

    assert simple_solver2.iterations < simple_solver.iterations

def test_simple_solver_start_pos_midpoint(simple_solver):
    simple_solver2 = copy.deepcopy(simple_solver)

    sliders = simple_solver.sliders
    _eval = simple_solver._eval

    dims = len(sliders)
    point = tuple([len(sliders[i]) - 1 for i in range(dims)])
    target = _eval(point)

    actual = simple_solver.solve(target)
    assert target == _eval(actual)
    assert actual == point

    midpoint = tuple([(len(sliders[i]) - 1)/2 for i in range(dims)])
    actual2 = simple_solver2.solve(target, start_pos=midpoint)
    assert target == _eval(actual2)
    assert actual2 == point

    assert simple_solver2.iterations < simple_solver.iterations