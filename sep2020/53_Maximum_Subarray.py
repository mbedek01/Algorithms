
def maxSubArray(nums):
    n = len(nums)
    max = float('-inf')
    max_array = []

    for i in range(0, n):
        arr = []
        prev_sum = float('-inf')
        curr_sum = 0
        max_sum = float('-inf')
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum < prev_sum:
                max_sum = prev_sum
                if max_sum > max:
                    max = max_sum
                break
            else:
                prev_sum = curr_sum
                arr.append(nums[j])
    max_array.append(arr)

    for item in max_array:
        print (item)
    return max



def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = maxSubArray(nums)
    print ("Result is", result)





if __name__ == "__main__":
    main()