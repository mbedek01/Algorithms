
# Helper function to calculate the degree of a given array
def findDegree(arr):
    numCount = {}

    for num in arr:
        if num in numCount.keys():
            numCount[num] += 1
        else:
            numCount[num] = 1

    degree = 0
    highest_repeated = 0
    for item in numCount.items():
        if item[1] > degree:
            degree = item[1]
            highest_repeated = item[0]
    return degree

# find the shortest subarray by finding all possible subarrays first O(n^3)
def findShortestSubArray(nums):

    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1

    arr = []
    min_size = 50001
    length = len(nums)
    for i in range(0, length):
        for j in range(i, length):
            for k in range(i, j+1):
                arr.append(nums[k])
            print (arr)
            if findDegree(arr) == findDegree(nums):
                size = len(arr)
                if size < min_size:
                    min_size = size
            arr = []

    print (min_size)
    return min_size

"""
The final solution (optimal) with comments
"""
def findShortestSubarrayOptimal(nums):

    if len(nums) == 0 or len(nums)==1:
        return len(nums)

    numCount = {}
    left = {}
    right = {}
    n = len(nums)
    result = 50001      # initialized to max size of an input array specified in question

    # numCount: hashmap to store the number of occurences of a number
    # left : hashmap to store the index of first occurence of a number
    # right: hashmap to store the index of last occurence of a number

    for i in range(0, n):
        # if number already in hashmap, increment count, and rightmost index
        if nums[i] in numCount.keys():
            numCount[nums[i]] += 1
            right[nums[i]] = i          # index of last occurrence of recurring number
        else:
            # if first occurrence of number, set count=1, set left index == right index (only one occurrence so far)
            numCount[nums[i]] = 1
            left[nums[i]] = i           # index of first occurrence of first occurence of number
            right[nums[i]] = i          # index of last occurrence of first occurence of number

    degree = max(numCount.values())     # degree of array will be the max of occurences of each number
    print (degree)

    # iterate through count hashmap, find all counts == degree. Get the minimal subarray if there are more than 1
    # number with same degree
    for k in numCount.keys():
        if numCount[k] == degree:
            min_size = right[k] - left[k] + 1
            if min_size < result:
                result = min_size
    return result






def main():
    print ("Hello world")
    nums = [1,2,2,1,2,1,1,1,1,2,2,2]
    # res = findShortestSubArray(nums)
    res = findShortestSubarrayOptimal(nums)
    print (res)


if __name__ == "__main__":
    main()





