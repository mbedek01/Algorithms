
# A string of length n has 2^n substrings including the empty string
# https://www.youtube.com/watch?v=RnlHPR0lyOE&ab_channel=WilliamFiset

import copy

def buildSubsequences(s):

    N = len(s)
    B = [0] * N
    bitStrings = []

    generateSubsequences(0, B, bitStrings, N)
    subsequences = set()

    for bitString in bitStrings:
        str = ""
        for i in range(0, len(bitString)):

            bit = bitString[i]
            if bit == 1:
                str = str + s[i]
            if(str != ""):
                subsequences.add(str)

    result = list(subsequences)
    res = sorted(result)
    return res


def generateSubsequences(i, B, bitstrings, N):
    # base case:
    if i == N:
        bitstrings.append(copy.deepcopy(B))
    else:
        B[i] = 0
        generateSubsequences(i+1, B, bitstrings, N)

        B[i] = 1
        generateSubsequences(i+1, B, bitstrings, N)



def main():
    print("Hello world!")
    s = "xyz"
    result = buildSubsequences(s)
    print (result)

    """
        for i in range(1, len(arr)-1):
        prev = arr[i-1]
        curr = arr[i]
        nxt = arr[i+1]
        print(prev, curr, nxt)

        if curr > prev:
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
    
    """


if __name__ == "__main__":
        main()