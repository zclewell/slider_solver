import queue

import numpy as np

def point_sum(point, sliders, dims=None):
    if not dims:
        dims = len(point)

    v = 1
    for i in range(dims):
        v *= sliders[i][point[i]]

    return v

if __name__ == '__main__':
    target = 33

    sliders = [range(1,10), range(1,5), range(1,3)]

    dims = len(sliders) # dimension
    lims = [len(s) for s in sliders] # limits

    q = queue.Queue()
    first = tuple([0 for i in range(dims)])
    q.put(first)
    seen = set(first)

    best = best_d = None
    iterations = 0

    while not q.empty():
        curr = q.get()
        iterations += 1

        if not best:
            best, best_d = curr, abs(target - point_sum(curr, sliders, dims))
        else:
            val = point_sum(curr, sliders, dims)
            curr_d = abs(target - val)
            if curr_d < best_d:
                best, best_d = curr, abs(curr_d)
            if val > target:
                continue # we passed the target

        if best_d == 0:
            break

        for i in range(dims):
            new = list(curr)
            new[i] = min(new[i] + 1, lims[i] - 1)
            new = tuple(new)
            if new not in seen:
                seen.add(new)
                q.put(new)

    print('Required {} iterations'.format(iterations))
    print(best, point_sum(best, sliders, dims))
