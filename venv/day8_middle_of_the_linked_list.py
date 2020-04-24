"""day8_middle_of_the_linked_list.py
    Created by Aaron at 08-Apr-20"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # app1
        # count=1
        # while True:
        #     check=head
        #     for x in range(count):
        #         if check.next==None:
        #             return head
        #         check=check.next
        #     head=head.next
        #     count+=1

        # app2
        # a=[head]
        # while a[-1].next:
        #     a.append(a[-1].next)
        # return a[int(len(a)/2)]

        # app3
        a=head
        while a and a.next:
            head=head.next
            a=a.next.next
        return head

run=Solution()
a=[1,2]
a=[1]
a=[1,2,3,4,5]
tail=head=ListNode(a[0])
for x in range(1,len(a)):
    tail.next=ListNode(a[x])
    tail=tail.next
print(run.middleNode(head).val)
# app1 traverse with 1 pointer at origin another pointer to check end; space O(1)
# app2 traverse with list and return val;   time O(n) space O(n)
# app2 traverse with 2 pointer at same time but different speed; time O(n) space O(1)
