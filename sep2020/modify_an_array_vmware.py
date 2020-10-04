
def modifyArray(arr):

    cost = 0
    min_val = min(arr)
    new_arr = []


    for i in range(0, len(arr)-1):
        prev = arr[i - 1]
        curr = arr[i]
        nxt = arr[i + 1]

        if i==0:
            if arr[i] == min_val:
                continue
            else:
                diff = abs(arr[i] - min_val)
                cost += diff
        elif curr > prev:
            continue
        elif curr == prev:
            continue
        elif curr < prev:
            a_diff = abs(curr - prev)
            curr = curr + a_diff
            cost += a_diff
        elif curr > nxt:
            b_diff = abs(nxt-curr)
            curr = curr - b_diff
            cost += b_diff
        else:
            cost += 0



    return cost





def main():
    print("Hello world!")
    #arr = [0,1,2,5,6,5,7]
    arr = [6,9,8,7,2,3,3]
    res = modifyArray(arr)
    print (res)


if __name__ == "__main__":
        main()