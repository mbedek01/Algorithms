class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def mergeTwoLists(l1, l2):

    if l1==None:
        return l2
    elif l2==None:
        return l1

    dummy = ListNode(-1)
    head = dummy.next

    while l1 != None and l2 != None:
        if(l1.val < l2.val):
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next

    if l1 != None:
        dummy.next =l1
    elif l2 != None:
        dummy.next = l2

    return head







def main():
    print("Hello world!")


if __name__ == "__main__":
        main()