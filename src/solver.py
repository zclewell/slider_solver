import queue

import numpy as np

class Solver:
    def __init__(self, sliders, _eval):
        self.sliders = sliders
        self._eval = _eval


    def solve(self, target, start_pos=None, end_pos=None):
        dims = len(self.sliders) # dimensions
        lims = [len(s) - 1 for s in self.sliders] # limits

        if start_pos == None:
            start_pos = tuple([0 for i in range(dims)])

        if end_pos == None:
            end_pos = lims

        q = queue.Queue()
        q.put(start_pos)
        seen = set(start_pos)

        best = best_d = None
        iterations = 0

        while not q.empty():
            curr = q.get()
            iterations += 1

            val = self._eval(curr)
            dist = abs(target - val)
            if not best:
                best, best_d = curr, dist
            else:
                if dist < best_d:
                    best, best_d = curr, dist
                if val > target:
                    continue # we passed the target

            if best_d == 0:
                break

            for i in range(dims):
                new = list(curr)
                new[i] = min(new[i] + 1, lims[i], end_pos[i])
                new = tuple(new)
                if new not in seen:
                    seen.add(new)
                    q.put(new)
        
        self.iterations = iterations
        self.best_d = best_d
        return best




def point_sum(point, sliders, dims=None):
    if not dims:
        dims = len(point)

    v = 1
    for i in range(dims):
        v *= sliders[i][point[i]]

    return v

if __name__ == '__main__':
    sliders = [range(1,10), range(1,5), range(1,3)]
    _eval = lambda p: point_sum(p, sliders, len(sliders))

    solver = Solver(sliders, _eval)

    target = 33
    best = solver.solve(target)

    print('Target: {} Actual: {} Indices: {} Distance: {} Iterations: {}'.format(target, _eval(best), best, solver.best_d, solver.iterations))