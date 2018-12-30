#!/bin/python3

from functools import reduce


# Complete the minimumBribes function below.

def trace_one_position(result, state):
    counter = 0
    diff = state['sticker'] - (state['position'] + 1)

    if diff > 2:
        result['chaotic'] = True

    if result['chaotic']:
        return result

    if state['sticker'] is not result['tracer'][state['position']]:
        end_point = result['tracer'].index(state['sticker'], state['position'])
        for i in range(end_point, state['position'], -1):
            result['tracer'][i] = result['tracer'][i - 1]
            counter += 1
        result['tracer'][state['position']] = state['sticker']
        result['counter'] += counter
    return result


def minimumBribes(q):
    too_chaotic = 'Too chaotic'
    tracer = [i+1 for i in range(len(q))]

    result = reduce(trace_one_position,
                    [{'sticker': q[p], 'position': p} for p in range(len(q))],
                    {'counter': 0, 'tracer': tracer, 'chaotic': False})

    return result['counter'] if not result['chaotic'] else too_chaotic


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        # minimumBribes(q)
        print('\n')
        print(str(minimumBribes(q)))

    # fptr.close()
