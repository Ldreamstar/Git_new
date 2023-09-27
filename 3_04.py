# python写一个链表可以完成增删改查的操作

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 在链表末尾添加一个节点
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # 检查链表是否为空:如果链表为空
            self.head = new_node
            return
        current = self.head
        while current.next:  # 如果当前节点的下一个节点不空
            current = current.next
        current.next = new_node

    # 在指定位置插入一个节点
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(position - 1):
            if current is None:
                raise IndexError("插入位置超出链表长度")  # raise 关键字用于引发异常。IndexError 是Python的内置异常类之一，通常用于表示索引超出范围的错误。
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # 删除第一个匹配的节点
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # 修改第一个匹配的节点的值
    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next

    # 查找节点是否存在
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # 打印链表内容
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# 示例用法
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.display()  # 输出: 1 -> 2 -> 3 -> None

    linked_list.insert(4, 1)
    linked_list.display()  # 输出: 1 -> 4 -> 2 -> 3 -> None

    linked_list.delete(2)
    linked_list.display()  # 输出: 1 -> 4 -> 3 -> None

    linked_list.update(4, 5)
    linked_list.display()  # 输出: 1 -> 5 -> 3 -> None

    print(linked_list.search(3))  # 输出: True
    print(linked_list.search(6))  # 输出: False
