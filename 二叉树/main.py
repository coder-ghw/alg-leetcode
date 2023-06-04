# %%
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self) -> str:
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

def list_to_LN(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LN(arr[1:]))

def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

# %%
t1 = [1,3,5,7,9]
ln1 = list_to_LN(t1)
print(ln1)

# %%
# 递归遍历单链表，倒序打印链表元素
def traverse(head: ListNode) -> None:
    if head is None:
        return
    # 前序位置
    print(head.val)
    traverse(head.next)
    # 后序位置
    # print(head.val)

traverse(ln1)

# %%
