

def maxSubArrayBruteForce(myList):

    n = len(myList)
    maxSum = float("-inf")
    lo = 0
    hi = 0
    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum += myList[j]
            if (sum > maxSum):
                maxSum = sum
                lo = i
                hi = j
    return [maxSum, lo, hi]

def main():
    myList = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    result = maxSubArrayBruteForce(myList)
    for k in result:
        print (k)

if __name__ == "__main__":
    main()