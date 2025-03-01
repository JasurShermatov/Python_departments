# class Stack:
#     def __init__(self):
#         self.elements = []
#
#     def push(self, element):
#         return self.elements.append(element)
#
#     def pop(self):
#         return self.elements.pop()
#
#     def top(self):
#         return self.elements[-1]
#
#     def size(self):
#         return len(self.elements)
#
#     def empty(self):
#         return self.size() == 0
#
#
# def test_stack():
#     stack = Stack()
#     assert stack.size() == 0
#     assert stack.empty() == "True"
#
#     stack.push("Smith")
#     assert stack.size() == 1
#     assert stack.empty() == "False"
#     assert stack.top() == "Smith"
#
#     stack.push("Alice")
#     assert stack.size() == 2
#     assert stack.empty() == "False"
#     assert stack.top() == "Alice"
#
#     assert stack.pop() == "Alice"
#
#     assert stack.size() == 1
#     assert stack.empty() == "False"
#     assert stack.top() == "Smith"
#
#     assert stack.pop() == "Smith"
#     assert stack.size() == 0
#     assert stack.empty() == "True"
#
#
# if __name__ == "__main__":
#     stack = Stack()
#
#





# Queue uchun quyidagi funksiyalarni yozish kerak:
# enqueue: elementni queue ning oxiriga qo'shadi.
# dequeue: queue ning boshidan elementni olib tashlaydi va qaytaradi.
# front: queue ning birinchi elementini qaytaradi.
# size: queue dagi elementlar sonini qaytaradi.
# empty: queue bo'sh yoki yo'qligini tekshiradi.



class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if not self.empty():
            return self.elements.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def front(self):
        if not self.empty():
            return self.elements[0]
        else:
            raise IndexError("front from empty queue")

    def size(self):
        return len(self.elements)

    def empty(self):
        return self.size() == 0


def test_queue():
    queue = Queue()
    assert queue.size() == 0
    assert queue.empty() == True

    queue.enqueue("Smith")
    assert queue.size() == 1
    assert queue.empty() == False
    assert queue.front() == "Smith"

    queue.enqueue("Alice")
    assert queue.size() == 2
    assert queue.empty() == False
    assert queue.front() == "Smith"

    assert queue.dequeue() == "Smith"
    assert queue.size() == 1
    assert queue.empty() == False
    assert queue.front() == "Alice"

    assert queue.dequeue() == "Alice"
    assert queue.size() == 0
    assert queue.empty() == True


if __name__ == "__main__":
    test_queue()
    print("All tests passed!")

