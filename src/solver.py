import queue

import numpy as np

class Solver:
    def __init__(self, sliders, _eval):
        self.sliders = sliders
        self._eval = _eval


    def solve(self, target, start_pos=None, end_pos=None):
        dims = len(self.sliders) # dimensions
        lims = [len(s) - 1 for s in self.sliders] # limits

        if not start_pos:
            start_pos = tuple([0 for i in range(dims)])

        if not end_pos:
            end_pos = tuple(lims)

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

            if best_d == 0:
                break

            for i in range(dims):
                # If val exceeds target than increasing any index cannot get us
                # closer to target
                if val < target:
                    new = list(curr)
                    new[i] = min(new[i] + 1, lims[i])

                    # If at least one index is less than the corresponding index in end pos
                    # then the value COULD be less than the value of end pos and must be
                    # considered
                    if any(map(lambda x: new[x] < end_pos[x], range(dims))) or \
                       all(map(lambda x: new[x] == end_pos[x], range(dims))):
                        new = tuple(new)
                        if new not in seen:
                            seen.add(new)
                            q.put(new)

                # Only need to look back if we didn't start at all 0's
                if any(map(lambda x: start_pos[x] != 0, range(dims))):
                    new = list(curr)
                    new[i] = max(new[i] - 1, 0)

                    # If at lest one index is greater than the corresponding index in start pos
                    # then the value COULD be greater than the value of start pos and must be
                    # considered
                    if any(map(lambda x: new[x] > start_pos[x], range(dims))):
                        new = tuple(new)
                        if new not in seen:
                            seen.add(new)
                            q.put(new)
                    
                    
        
        self.iterations = iterations
        self.best_d = best_d
        return best