
# Refer to Leetcode for the best solution (using List + Hashmap) or my submitted java solution
# however, this also works (not optimal)

def isValid(s):

    # We are not using list[] as a data structure for stack as list operations for push and pop will need O(n) time
    # Also, as the stack grows, because lists are contiguous in memory, we could run out of contiguous space and
    #       the operations may need a lot of time

    # deque data structure allows O(1) time for push and pop
    from collections import deque

    stack = deque()
    res = False

    if s==None or len(s)==1:
        return res

    for par in s:
        if par=='(' or par=='{' or par=='[':
            stack.append(par)
            res = False                     # for s = "[]{}("
        elif par==')':
            if len(stack)==0:
                res = False
                return res
            else:
                if stack.pop() == '(':
                    res = True
                else:
                    res = False
                    return res
        elif par=='}':
            if len(stack)==0:
                res = False
                return res
            else:
                if stack.pop() == '{':
                    res = True
                else:
                    res = False
                    return res

        elif par==']':
            if len(stack)==0:
                res = False
                return res
            else:
                if stack.pop()=='[':
                    res = True
                else:
                    res = False
                    return res

    if(len(stack)!=0):
        return False                # eg: s = "([]"
    return res





def main():
    print("Hello world!")
    s = "([]){"
    res = isValid(s)
    print (res)


if __name__ == "__main__":
        main()