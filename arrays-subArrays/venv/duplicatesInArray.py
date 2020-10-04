

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    i = 0
    j = i
    for i in range (len(nums)):

        if(nums[j+1]) == nums[j]:
            nums.remove(j)
            j = i
        


    return (nums)


def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = removeDuplicates(nums)
    for k in result:
        print (k)



if __name__ == "__main__":
    main()