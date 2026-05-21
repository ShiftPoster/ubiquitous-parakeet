class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, nums: list[int]):
        ll = list(map(cls, nums))
        for i in range(len(ll) - 1):
            ll[i].next = ll[i + 1]
        return ll[0]

    def to_list(self) -> list[int]:
        pylist = []
        curr = self
        while True:
            val = curr.val
            pylist.append(val)
            if curr.next is None:
                break
            curr = curr.next
        return pylist
