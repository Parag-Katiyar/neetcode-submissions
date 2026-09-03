# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    import heapq

    # Custom comparator for ListNode based on value
    class Wrapper:

      def __init__(self, node: ListNode):
        self.node = node

      def __lt__(self, other):
        return self.node.val < other.node.val

    min_heap = []
    for l in lists:
      if l:
        heapq.heappush(min_heap, Wrapper(l))

    dummy = ListNode(0)
    curr = dummy

    while min_heap:
      wrapper = heapq.heappop(min_heap)
      node = wrapper.node
      curr.next = node
      curr = curr.next

      if node.next:
        heapq.heappush(min_heap, Wrapper(node.next))

    return dummy.next
