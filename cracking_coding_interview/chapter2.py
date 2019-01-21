from collections import defaultdict


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append_to_tail(self, data):
        new_end = Node(data)
        old_end = self
        while old_end.next is not None:
            old_end = old_end.next
        old_end.next = new_end


def delete_node(head, d):
    current_node = head

    if current_node.data == d:
        return current_node.next

    while current_node.next is not None:
        if current_node.next.data == d:
            current_node.next = current_node.next.next
            return head
        current_node = current_node.next
    return head


def question1():
    title = 'Remove Dups'
    question = 'Write code to remove duplicates from an unsorted linked list.'

    def remove_dups1(head):
        data_count = defaultdict(int)
        current_node = head

        data_count[current_node.data] += 1

        while current_node.next is not None:
            data_count[current_node.next.data] += 1
            if data_count[current_node.next.data] > 1:
                current_node.next = current_node.next.next
        return head

    question = 'How would you solve this problem if a temporary buffer is not allowed?'

    def remove_dups2(head):
        current_node = head
        runner_node = head.next

        while current_node.next is not None:


print('abc')







































