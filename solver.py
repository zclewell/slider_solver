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

    sliders = [range(10), range(5), range(3)]

    dims = len(sliders) # dimension
    lims = [s[-1] for s in sliders] # limits

    q = queue.Queue()
    q.put([0 for i in range(dims)])

    best = best_d = None

    while not q.empty():
        curr = q.get()

        if not best:
            best, best_d = curr, abs(target - point_sum(curr, sliders, dims))
        else:
            curr_d = target - point_sum(curr, sliders, dims)
            if curr_d < 0:
                continue # we passed the target
            if curr_d < best_d:
                best, best_d = curr, curr_d

        if best_d == 0:
            break

        for i in range(dims):
            new = curr
            new[i] = min(new[i] + 1, lims[i])
            q.put(new)

    print(best)
