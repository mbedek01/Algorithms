class Node:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.nxt = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def addToHead(self, node):
        node.prev = self.head
        node.nxt = self.head.nxt

        self.head.nxt.prev = node
        self.head.nxt = node

    def removeNode(self, node):
        prev = node.prev
        nxtNode = node.nxt

        prev.nxt = nxtNode
        nxtNode.prev = prev
        # node.nxt.prev = node.prev
        # node.prev.nxt = node.nxt

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        target = self.tail.prev
        self.removeNode(target)
        return target

    def get(self, key):
        node = self.cache.get(key)
        if not node:
            return -1
        else:
            self.moveToHead(node)
            return node.val

    def put(self, key, value):

        node = self.cache.get(key)
        if not node:
            newNode = Node()
            newNode.key = key
            newNode.val = value
            self.cache[key] = newNode
            self.addToHead(newNode)
            self.size += 1

            if self.size > self.capacity:
                tail = self.removeTail()
                del self.cache[tail.key]
                self.size -= 1

        else:
            node.val = value
            self.moveToHead(node)


def main():
    print("Hello world!")


if __name__ == "__main__":
        main()