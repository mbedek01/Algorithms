
def subString(s):
    length = len(s)
    arr = []
    
    if len(s) == 1:
        return s

    for p in range(1, length + 1):

        for i in range(length - p + 1):

            j = i + p - 1
            str = ""
            for k in range(i, j + 1):

                str = str + s[k]
            arr.append(str)

    # sort array lexographically
    arr.sort()
    arr_length = len(arr)
    # retrieve the last substring from the sorted array of substrings
    maxSubstring = arr[arr_length - 1]
    return maxSubstring



def main():
    print("Hello world!")
    s = "baca"
    result = subString(s)
    print (result)


if __name__ == "__main__":
        main()