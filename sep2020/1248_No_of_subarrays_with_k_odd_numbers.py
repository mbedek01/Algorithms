
# Gives number of subarrays with "atmost" k odd integers --> means k or less odd integers

def evenSubarray(nums, k):
    N = len(nums)
    count = 0
    subArrays = []

    # first we find out all possible subarrays
    for i in range(0, N):
        for j in range(i, N):
            arr = []
            for p in range(i, j+1):
                arr.append(nums[p])
            subArrays.append(arr)

    print (subArrays)

    # check for each subarray, determine if it has k or less odd numbers --> if yes, increment count
    for arr in subArrays:
        print (arr)
        if len(arr) < k:
            continue
        else:
            odd = 0
            for num in arr:
                if(num % 2 == 1):
                    odd += 1
            if odd <= k:
                count += 1

    return count




"""
    numCopy = []
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            numCopy.append(0)
        elif nums[i] % 2 == 1:
            numCopy.append(1)

    # count number of subarrays with k odd numbers
    count, sum = 0, 0
    map = {0: 1}
    for i in range(0, len(numCopy)):
        sum += numCopy[i]
        if (sum - k) in map.keys():
            count += map.get(sum-k)
            if sum in map.keys():
                map[sum] += 1
            else:
                map[sum] = 0

    return count
"""




def main():
    print("Hello world!")
    nums = [1,2,3,4]        # [1,0,1,0]
    k = 1
    res = evenSubarray(nums, k)
    print (res)


    """
        # initialize two pointers
        l, r = 0, -1
        count = 0
        odd = 0
        N = len(nums)

        while r < N-1:
            r+=1
            if nums[r] % 2 == 1:
                odd += 1

            if odd == k:
                left = 1
                right = 1

                # increase right till next number is even
                # stop when you find odd number or when you reach end of array
                while r < N-1 and nums[r+1] % 2 == 0:
                    right += 1
                    r += 1

                while l <= r and nums[l] % 2 == 0:
                    left += 1
                    l += 1

                count += left * right
                l += 1
                odd -= 1

        return count

        """


if __name__ == "__main__":
        main()