from random import randint


# Brute force
def calcTwoNumberSum(array, target):
    count = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            count += 1
            if array[i] + array[j] == target:
                return count
    return count


def calcTwoNumberSumBetter(a, target):
    i = 0
    j = len(a) - 1
    while i < j:
        sum2 = a[i] + a[j]
        if sum2 > target:
            j -= 1
        elif sum2 < target:
            i += 1
        else:
            return a[i], a[j]
    return 0,0


def calcThreeNumberSumBetter(a, target):
    a.sort()
    res = []
    for i in range(len(a)):
        first = a[i]
        x, y = calcTwoNumberSumBetter(a[i + 1:], target - first)
        if x != 0 and y != 0:
            res.append([first, x, y])
    return res


a = [2, 5, -3, 10, 6, -5, 0, 8]
target = 0
print(calcThreeNumberSumBetter(a, target))
# res = []
# for n in range(10000, 20000, 1000):
#     a = [randint(1, 1000) for i in range(n)]
#     targetSum = randint(1, 10000)
#     c1 = calcTwoNumberSum(a, targetSum)
#     c2 = calcTwoNumberSumBetter(a, targetSum)
#     res.append(c1 / c2)
#     print(c1/c2)
# print(res)
