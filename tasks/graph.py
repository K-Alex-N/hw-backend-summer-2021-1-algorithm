from collections import deque
from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:

        def recursive_loop(n: Node, visited: list):
            for neighbour in n.outbound:
                if neighbour not in visited:
                    visited.append(neighbour)
                    recursive_loop(neighbour, visited)

        visited = [self._root]
        recursive_loop(self._root, visited)
        return visited

    def bfs(self) -> list[Node]:
        queue = deque([self._root])
        visited = [self._root]

        while queue:
            for neighbour in queue.popleft().outbound:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return visited
