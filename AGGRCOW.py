def findminDist(stalls, cows):
    maxDist = -1
    low = stalls[0]
    high = stalls[-1]

    while high > low:
        mid = (low + high) // 2
        if fits(mid, stalls, cows) == 1:
            if mid > maxDist:
                maxDist = mid
            low = mid + 1
        else:
            high = mid
    return maxDist


def fits(mid, stalls, cows):
    cow_count = 0
    prev = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - prev >= mid:
            prev = stalls[i]
            cow_count += 1
            if cow_count == cows - 1:
                return 1

    return 0


if __name__ == "__main__":
    t = int(input().strip())

    while t > 0:
        n, c = list(map(int, input().strip().split(' ')))
        list_stalls = []
        for i in range(n):
            list_stalls.append(int(input().strip()))

        list_stalls = sorted(list_stalls)
        print(findminDist(list_stalls, c))

        t -= 1
