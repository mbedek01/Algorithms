def staircase(s):

    res = ""
    arr = s.split(":")
    t = arr[2][2] + arr[2][3]
    sec = arr[2][0] + arr[2][1]
    arr.pop(2)
    arr.append(sec)
    arr.append(t)
    #for i in arr:
     #   print(i)

    if arr[3] == "PM":
        # print (arr[0])
        if arr[0] > "12":
            arr[0] = str(int(arr[0]) + 12)
    elif arr[3] == "AM":
        if arr[0] == "12":
            arr[0] = "00"

    res = res + arr[0] + ":" + arr[1] + ":" + arr[2]
    return res



def main():
    s = "12:05:45AM"
    res = staircase(s)
    print(res)


if __name__ == "__main__":
    main()