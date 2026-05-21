from typing import Iterator

from .common import ListNode


def node_iter(nodes: list[ListNode]) -> Iterator[ListNode]:
    while nodes:
        vals = tuple(_.val for _ in nodes)
        i = vals.index(min(vals))
        curr = nodes.pop(i)
        yield curr
        if curr.next is not None:
            nodes.append(curr.next)


def merge_nodes(nodes: list[ListNode]) -> ListNode:
    gen = node_iter(nodes)
    start = next(gen)
    curr_node = start
    while True:
        try:
            next_node = next(gen)
        except StopIteration:
            next_node = None
        if next_node:
            curr_node.next = next_node
            curr_node = next_node
        else:
            break
    return start


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        _lists = [_ for _ in lists if _]
        return None if not _lists else merge_nodes(_lists)


def run(lists: list[ListNode | None]) -> ListNode | None:
    return Solution().mergeKLists(lists)
