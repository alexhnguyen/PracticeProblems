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
        # use hashtable to check for duplicates
        data_count = defaultdict(int)
        current_node = head
        data_count[current_node.data] += 1

        while current_node is not None and current_node.next is not None:
            data_count[current_node.next.data] += 1
            if data_count[current_node.next.data] > 1:
                current_node.next = current_node.next.next
            current_node = current_node.next
        return None

    question = 'How would you solve this problem if a temporary buffer is not allowed?'

    def remove_dups2(head):
        # use a secondary pointer that "runs" ahead and checks for duplicates
        if head.next is None:
            return None

        current_node = head
        while current_node is not None:
            runner_node = current_node
            while runner_node.next is not None:
                if current_node.data == runner_node.next.data:
                    runner_node.next = runner_node.next.next
                else:
                    runner_node = runner_node.next
            current_node = current_node.next
        return None


def question2():
    title = 'Return Kth to Last'
    question = 'Implement an algorithm to find the kth to last element of a singly linked list.'

    def get_kth_to_last(head, k):
        pointer_array = []
        current_node = head
        while current_node is not None:
            pointer_array.append(current_node)
            current_node = current_node.next
        if len(pointer_array)-1 < k:
            return None
        return pointer_array[len(pointer_array)-k-1]


def question3():
    title = 'Delete Middle Node'
    question = 'Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, ' \
               'not necessarily the exact middle) of a singly linked list, given only access to that node.'

    def delete_middle_node(head, delete_node):
        if head == delete_node:
            return None
        if delete_node.next is None:  # is tail
            return None

        current_node = head
        while current_node.next is not None:
            if current_node.next == delete_node:
                current_node.next = current_node.next.next
                return None
            current_node = current_node.next
        return None


def question4():
    title = 'Partition'
    question = 'Write code to partition a linked list around a value x, such that all nodes less than x come before ' \
               'all nodes greater than or equal to x. If x is contained within the list, the values of x only need to ' \
               'be after the elements less than x (see below). The partition element x can appear anywhere in the ' \
               '"right partition"; it does not need to appear between the left and right partitions.'

    def array_into_linked_list(node_list):
        if len(node_list) == 0:
            return None, None
        else:
            head = node_list[0]
        for i, runner_node in enumerate(node_list[:-1]):
            runner_node.next = node_list[i + 1]
        tail = node_list[-1]
        tail.next = None
        return head, tail

    def get_partition_lists(head, x):
        large_partition = []
        small_partition = []
        current_node = head
        while current_node is not None:
            if current_node.data < x:
                small_partition.append(current_node)
            else:
                large_partition.append(current_node)
            current_node = current_node.next
        return large_partition, small_partition

    def combine_partition(large_partition, small_partition):
        head_small, tail_small = array_into_linked_list(small_partition)
        head_large, tail_large = array_into_linked_list(large_partition)
        if head_small is None:
            return head_large
        if head_large is None:
            return head_small
        tail_small.next = head_large
        return head_small

    def partition(head, x):
        large_partition, small_partition = get_partition_lists(head, x)
        return combine_partition(large_partition, small_partition)


def question5():
    title = 'Sum Lists'
    question = "You have two numbers represented by a linked list, where each node contains a single digit. " \
               "The digits are stored in reverse order, such that the 1 's digit is at the head of the list. " \
               "Write a function that adds the two numbers and returns the sum as a linked list."

    title = 'Follow up'
    question = 'Suppose the digits are stored in forward order. Repeat the above problem.'

    # A solution solving by converting between strings and integers

    def get_number_base10(head):
        current_node = head
        number_list = []
        while current_node is not None:
            number_list.append(str(current_node.data))
            current_node = current_node.next
        return ''.join(number_list)

    def get_sum(head1, head2, reverse):
        if reverse:
            number1 = int(get_number_base10(head1)[::-1])
            number2 = int(get_number_base10(head2)[::-1])
            number_sum = str(number1 + number2)[::-1]
        else:
            number1 = int(get_number_base10(head1))
            number2 = int(get_number_base10(head2))
            number_sum = str(number1 + number2)
        return number_sum

    def sum_list(head1, head2, reverse=True):
        number_sum = get_sum(head1, head2, reverse)
        new_head = new_current = Node(number_sum[0])
        for digit in number_sum[1:]:
            new_current.next = Node(int(digit))
            new_current = new_current.next
        return new_head

    # A solution without converting between strings and integers for a backwards list

    def carry_add(number1, number2, carry=0):
        number_sum = number1 + number2 + carry
        return number_sum % 10, number_sum // 10

    def add_mismatched_digits(current_node, old_node, multiplier, carry):
        while current_node is not None:
            digit_sum, carry = carry_add(current_node.data, 0, carry)
            new_node = Node(digit_sum)
            old_node.next = new_node
            old_node = new_node
            multiplier += 1
            current_node = current_node.next
        return None

    def sum_list_reverse(head1, head2):
        current_node1 = head1
        current_node2 = head2
        old_node = None
        head_node = None
        multiplier = 0
        carry = 0
        while current_node1 is not None and current_node2 is not None:
            digit_sum, carry = carry_add(current_node1.data, current_node2.data, carry=carry)
            new_node = Node(digit_sum)
            try:
                old_node.next = new_node
            except AttributeError:
                head_node = new_node
            old_node = new_node
            current_node1 = current_node1.next
            current_node2 = current_node2.next
            multiplier += 1

        # used when one list is longer than the other
        add_mismatched_digits(current_node1, old_node, multiplier, carry)
        add_mismatched_digits(current_node2, old_node, multiplier, carry)

        return head_node

    # A solution without converting between strings and integers for forwards list

    def get_data_array(head):
        data_array = []
        current_node = head
        while current_node is not None:
            data_array.append(current_node.data)
            current_node = current_node.next
        return data_array

    def sort_big_small(head1, head2):
        data_array1 = get_data_array(head1)
        data_array2 = get_data_array(head2)

        if len(data_array1) > len(data_array2):
            small_len = len(data_array2)
            big_len = len(data_array1)
            data_array_big = data_array1
            data_array_small = data_array2
        else:
            small_len = len(data_array1)
            big_len = len(data_array2)
            data_array_big = data_array2
            data_array_small = data_array1
        return data_array_big, big_len, data_array_small, small_len

    def sum_arrays(data_array_big, big_len, data_array_small, small_len):
        number_sum = 0
        for i in range(big_len - small_len):
            data1 = data_array_big[i]
            number_sum = (number_sum * 10) + data1
        for i in range(small_len):
            data1 = data_array_big[big_len - small_len + i]
            data2 = data_array_small[i]
            number_sum = (number_sum * 10) + data1 + data2
        return number_sum

    def make_linked_list(number_sum):
        old_node = None
        digit_num = 1
        carry = number_sum
        while digit_num != 0 and carry != 0:
            digit_num = carry % 10
            carry = carry // 10
            new_node = Node(digit_num)
            new_node.next = old_node
            old_node = new_node
        head_node = old_node
        return head_node

    def sum_list_forward(head1, head2):
        data_array_big, big_len, data_array_small, small_len = sort_big_small(head1, head2)
        number_sum = sum_arrays(data_array_big, big_len, data_array_small, small_len)
        head_node = make_linked_list(number_sum)
        return head_node


def question6():
    title = 'Palindrome'
    question = 'Implement a function to check if a linked list is a palindrome.'

    def is_palindrome(head):
        current_node = runner_node = head

        stack = []
        while runner_node is not None and runner_node.next is not None:
            stack.append(current_node.data)
            current_node = current_node.next
            runner_node = runner_node.next.next

        if runner_node is not None:
            # if length is odd, skip middle node
            current_node = current_node.next

        for value in stack[::-1]:
            if value != current_node.data:
                return False
            current_node = current_node.next
        return True


def question7():
    title = 'Intersection'
    question = 'Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. ' \
               'Note that the intersection is defined based on reference, not value.That is, if the kth node of the ' \
               'first linked list is the exact same node (by reference) as the jth node of the second linked list, ' \
               'then they are intersecting.'

    def get_pointer_array(head):
        pointer_array = []
        current_node = head
        while current_node is not None:
            pointer_array.append(current_node)
            current_node = current_node.next
        return pointer_array

    def intersection(head1, head2):
        # key idea is if intersecting, last nodes must be same
        # iterate backwards until the two current_nodes are not the same
        pointer_array1 = get_pointer_array(head1)
        pointer_array2 = get_pointer_array(head2)
        intersection_node = None
        for i in range(min(len(pointer_array1), len(pointer_array2))):
            current_node1 = pointer_array1[len(pointer_array1)-1-i]
            current_node2 = pointer_array2[len(pointer_array2)-1-i]
            if current_node1 == current_node2:
                intersection_node = current_node1
            else:
                return intersection_node
        return intersection_node


def question8():
    title = 'Loop Detection'
    question = 'Given a circular linked list, implement an algorithm that returns the node at the beginning of the ' \
               'loop.'

    # The book's hint is
    # To identify if there's a cycle, try the "runner" approach described on page 93.
    # Have one pointer move faster than the other.
    #
    # I solved the problem using a hash table,
    # then solve it using the suggested "runner" approach.

    def get_loop_head1(head):
        id_count = defaultdict(int)
        current_node = head
        while current_node is not None:
            node_id = id(current_node)
            id_count[node_id] += 1
            if id_count[node_id] > 1:
                return current_node
            current_node = current_node.next
        return None

    def get_loop_head2(head):
        current_node = head
        runner_node = head.next
        while runner_node is not None and runner_node.next is not None:
            if current_node == runner_node:
                return current_node
            current_node = current_node.next
            runner_node = runner_node.next.next
        return None


# This code will be used if testing code is added
# from random import randint
#
# def get_rand_int():
#     return randint(0, 127)
#
# def make_list(length=128):
#     head = Node(get_rand_int())
#     current_node = head
#     for i in range(length-1):
#         new_node = Node(get_rand_int())
#         current_node.next = new_node
#         current_node = current_node.next
#     return head
#
# head = Node(1)
# head.append_to_tail(2)
# head.append_to_tail(2)
