class Node:

    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def r_add(self, ptr, item):
        if ptr is None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.r_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.r_add(ptr.right, item)
        return ptr

    def add(self, item):
        self.root = self.r_add(self.root, item)

    def search(self, item):
        self.r_search(self.root, item)

    def r_search(self, ptr, item):
        if ptr is None:
            print(False)
        elif item == ptr.item:
            print(True)
        elif item < ptr.item:
            return self.r_search(ptr.left, item)
        else:
            return self.r_search(ptr.right, item)

    def in_order(self):
        self.r_order(self.root)

    def r_order(self, ptr):
        if ptr is not None:
            self.r_order(ptr.left)
            print(ptr.item)
            self.r_order(ptr.right)
        return

    def post_order(self):
        self.r_post(self.root)

    def r_post(self, ptr):
        if ptr is not None:
            self.r_post(ptr.left)
            self.r_post(ptr.right)
            print(ptr.item)
        return

    def pre_order(self):
        self.r_pre(self.root)

    def r_pre(self, ptr):
        if ptr is not None:
            print(ptr.item)
            self.r_pre(ptr.left)
            self.r_pre(ptr.right)
        return


def main():

    t = Tree()
    n = [5, 1, 9, 3, 7, 8, 6, 4, 2]
    for i in n:
        t.add(i)

    t.search(10)
    t.search(2)
    print("in order")
    t.in_order()

    print("post-order")
    t.post_order()

    print("pre-order")
    t.pre_order()


if __name__ == '__main__':
    main()
