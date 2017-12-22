class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_value):
        self.data = new_value

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def printL(self):
        current = self.head
        tmp = ""
        if self.head is not None:
            while current is not None:
                tmp += str(current.get_data()) + ", "
                current = current.get_next()
            return tmp
        else:
            tmp = "NIL"
            return tmp

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() == item:
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return True
            else:
                previous = current
                current = current.get_next()
        return False
