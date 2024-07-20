def calculate_difference(n, m, array):
    results = []
    for i in range(n):
        diff = abs(array[i] - array[(i + 1) % n])
        if diff > m:
            results.append('1')
        else:
            results.append('0')
    print(' '.join(results))

# Reading input
n, m = map(int, input().split())
array = list(map(int, input().split()))

# Calling the function
calculate_difference(n, m, array)
