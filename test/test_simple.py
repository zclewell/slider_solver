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

def test_simple_solver_start_pos(simple_solver):
    sliders = simple_solver.sliders
    _eval = simple_solver._eval

    dims = len(sliders)
    point = tuple([0 for i in range(dims)])
    target = _eval(point)
    start_pos = point

    actual = simple_solver.solve(target, start_pos=start_pos)
    assert target == _eval(actual)
    assert actual == point

def test_simple_solver_end_pos(simple_solver):
    sliders = simple_solver.sliders
    _eval = simple_solver._eval

    dims = len(sliders)
    point = tuple([0 for i in range(dims)])
    target = _eval(point)
    end_pos = tuple([sliders[i][-1] for i in range(dims)])

    actual = simple_solver.solve(target, end_pos=end_pos)
    assert target == _eval(actual)
    assert actual == point

def test_simple_solver_start_end_pos(simple_solver):
    sliders = simple_solver.sliders
    _eval = simple_solver._eval

    dims = len(sliders)
    point = tuple([0 for i in range(dims)])
    target = _eval(point)
    start_pos = point
    end_pos = tuple([sliders[i][-1] for i in range(dims)])

    actual = simple_solver.solve(target, start_pos=start_pos, end_pos=end_pos)
    assert target == _eval(actual)
    assert actual == point
    