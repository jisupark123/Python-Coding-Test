import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left: Node = None
        self.right: Node = None


def get_input():
    lst = []
    while True:
        try:
            lst.append(int(input()))
        except:
            return lst


def insert(new_node: Node):
    curr_node = root_node

    # 1. node와 비교
    # 2. 작으면
    # 2-1 왼쪽 자식이 없으면 왼쪽 자식으로 설정
    # 2-2 왼쪽 자식이 있으면 왼쪽 노드로 이동해서 1번으로
    # 3. 크면 (오른쪽, 나머지는 동일)
    while True:
        if new_node.key > curr_node.key:
            if curr_node.right == None:
                curr_node.right = new_node
                return
            curr_node = curr_node.right
        else:
            if curr_node.left == None:
                curr_node.left = new_node
                return
            curr_node = curr_node.left


lst = get_input()

root_node = Node(lst[0])

for num in lst[1:]:
    insert(Node(num))


def find(node: Node):
    if node == None:
        return
    find(node.left)
    find(node.right)
    print(node.key)


find(root_node)
