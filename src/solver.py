import queue

import numpy as np

class Solver:
    def __init__(self, sliders, _eval):
        self.sliders = sliders
        self._eval = _eval


    def solve(self, target):
        dims = len(self.sliders) # dimensions
        lims = [len(s) - 1 for s in self.sliders] # limits

        start_pos = tuple([0 for i in range(dims)])

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
                new[i] = min(new[i] + 1, lims[i])
                new = tuple(new)
                if new not in seen:
                    seen.add(new)
                    q.put(new)
        
        self.iterations = iterations
        self.best_d = best_d
        return best