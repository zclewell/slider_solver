# Slider Solver
[![codecov](https://codecov.io/gh/zclewell/slider_solver/branch/master/graph/badge.svg)](https://codecov.io/gh/zclewell/slider_solver)
[![Build Status](https://travis-ci.com/zclewell/slider_solver.svg?branch=master)](https://travis-ci.com/zclewell/slider_solver)

:construction: Under construction!

## Purpose
You have a computer connected to a television and both have a volume control. You want to set the volume to a given value, which volume slider do you increase? By how much? This is an example of a simple problem that this project aims to solve.

You supply one or more series of discrete values (computer volume settings and television volume settins), an evaluation function (computer volume multiplied by television volume), and a target (deisred volume) and this project will return a set of indices corresponding to which values to use to get as close as possible to the target.

## Limitations
Currently we assume that an increase in value in any slider also increases the output of the supplied evaluation function. This allows us to use a breadth first search to find a target value faster.

## Testing
We use `pytest` in order to validate our functions simply run:
```bash
pytest-3
```
In the root directory to test on your machine.

## Objects
### Solver
Assumes supplied sliders are sorted
#### Constructor
```python
solver.Solver(sliders, _eval)
```
##### sliders
`iterable` object containing one or more `iterable` objects.
##### eval
function used to find the value of a given set of indices
#### solve
```python
solve(target, start_pos=None, end_pos=None)
```
##### target
Desired value to solve for
##### start_pos (Optional)
`iterable` that is known to have a value less than target
##### end_pos (Optional)
`iterable` that is known to have a value greater than target
### UnsortedSolver
Aassumes supplied sliders are unsorted
#### Constructor
```python
solver.UnsortedSolver(sliders, _eval)
```
##### sliders
`iterable` object containing one or more `iterable` objects.
##### eval
function used to find the value of a given set of indices
#### solve
```python
solve(target, start_pos=None, end_pos=None)
```
##### target
Desired value to solve for
##### start_pos (Optional)
`iterable` that is known to have a value less than target
##### end_pos (Optional)
`iterable` that is known to have a value greater than target



