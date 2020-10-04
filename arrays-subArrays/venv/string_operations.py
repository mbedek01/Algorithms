
def largestTimeFromDigits(A):

    # A.sort(reverse=True)
    max = 0
    max_str = ""
    numList = []
    for i in A:
        for j in A:

            num_str = str(i) + str(j)
            num = int(str(i) + str(j))
            if (num > max) & (num < 24):
                max = num
                max_str = num_str
            else:
                numList.append(num_str)
    if max_str == "":
        return ""
    else:
        d1 = max_str[0]
        d2 = max_str[1]
    mints = ""
    for num in numList:
        d3 = num[0]
        d4 = num[1]
        if (d3 != d1) & (d3 != d2) & (d4 != d1) & (d4 != d2) & (int(num) < 60):
            mints = num

    if mints == "":
        return ""
    result = max_str + ":" + mints
    return result





def main():
    A = [5,6,2,3]
    result = largestTimeFromDigits(A)

    print (result)



if __name__ == "__main__":
    main()