class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self, data=None):
        if data is None:
            self.top = None
        else:
            self.top = Node(data)

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, data):
        new_item = Node(data)
        new_item.next = self.top
        self.top = new_item
        return None

    def peek(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.data

    def is_empty(self):
        return self.top is None


def question1():
    title = 'Three in One'
    question = 'Describe how you could use a single array to implement three stacks.'

    # # time efficient
    # # not space efficient
    # allocate each third position in the array to the stack
    # stack0 gets positions 0, 3, 6, 9,...
    # stack1 gets positions 1, 4, 7, 10,...
    # stack2 gets positions 2, 5, 8, 11,...

    # # not time efficient
    # # space efficient
    # allocate 0 to x_0 spots to stack0
    # allocate x_0+1 to x_1 spots to stack1
    # allocate x_1+1 to x_2 spots to stack 2
    # ie [ [stack0] [stack1] [stack2] ]
    # whenever adding or removing an element from the stack, the whole array will need to be recreated

    # # sorta time efficient
    # # sorta space efficient
    # similar to the idea above where the entire array is separated like [ [stack0] [stack1] [stack2] ]
    # except the array will not be recreated each time. instead we preallocate space by doubling the array sizes
    # that is the length of the stacks will go 0 -> 1 -> 2 -> 4 -> 8 -> 16 -> 32
    # the lengths of the stacks can also decrease if enough items are removes


def question2():
    title = 'Stack Min'
    question = 'How would you design a stack which, in addition to push and pop, has a function min which returns ' \
               'the minimum element? Push, pop and min should all operate in 0(1) time.'

    # For each node, keep a "min" variable that has the value of the minimal element for all nodes below it and itself.
    # When using "push" and "pop", these functions will need to check and update "min" accordingly.


def question3():
    title = 'Stack of Plates'
    question = 'Set of Stacks should be composed of several stacks and should create a new stack once the previous ' \
               'one exceeds capacity. Implement push and pop'

    class SetOfStacks:
        def __init__(self, data, max_length=2, type='array'):
            if type == 'array':
                self.my_stacks = [MyStack(data)]
            elif type == 'stack':
                self.my_stacks = MyStack(MyStack(data))
            else:
                raise ValueError('[{type}] is an invalid argument. please use "array" or "stack"')
            self.__type = type
            self.stack_lengths = [1]
            self.max_length = max_length

        def push(self, data):
            if self.stack_lengths[-1] >= self.max_length:
                if self.__type == 'array':
                    self.my_stacks.append(MyStack(data))
                else:
                    self.my_stacks.push(MyStack(data))
                self.stack_lengths.append(1)
            else:
                if self.__type == 'array':
                    self.my_stacks[-1].push(data)
                else:
                    self.my_stacks.top.data.push(data)
                self.stack_lengths[-1] += 1
            return None

        def pop(self):
            if self.__type == 'array':
                data = self.my_stacks[-1].pop()
            else:
                data = self.my_stacks.top.data.pop()
            self.stack_lengths[-1] -= 1
            if self.stack_lengths[-1] == 0:
                self.stack_lengths = self.stack_lengths[:-1]
                if self.__type == 'array':
                    self.my_stacks = self.my_stacks[:-1]
                else:
                    self.my_stacks.pop()
            return data

        def pop_at(self, index):
            if self.__type == 'array':
                try:
                    stack = self.my_stacks[index]
                except IndexError:
                    raise ValueError('[{index}] is an invalid index. Must be between 0 and {max}'
                                     .format(index=index, max=len(self.stack_lengths)))
                data = stack.pop()
                self.stack_lengths[index] -= 1
                if self.stack_lengths[-1] == 0:
                    self.stack_lengths = self.stack_lengths[:index] + self.stack_lengths[index + 1:]
                    self.my_stacks = self.my_stacks[:index] + self.my_stacks[index + 1:]
                return data
            else:
                previous_stack = None
                current_stack = self.my_stacks.top
                index_ = len(self.stack_lengths)-1-index
                for i in range(index_):
                    try:
                        previous_stack = current_stack
                        current_stack = current_stack.next
                    except AttributeError:
                        raise ValueError('[{index}] is an invalid index. Must be between 0 and {max}'
                                         .format(index=index, max=len(self.stack_lengths)))
                data = current_stack.data.pop()
                if self.stack_lengths[index_] == 0:
                    self.stack_lengths = self.stack_lengths[:-1]
                    previous_stack.next = previous_stack.next.next
                return data


def question4():
    title = 'Queue via Stacks'
    question = 'Implement a MyQueue class which implements a queue using two stacks.'

    class MyQueue_stack:
        def __init__(self, data):
            self.my_stack = MyStack(data)
            self.temp_stack = None

        def pop(self):
            if self.temp_stack is None and self.my_stack is not None:
                self.temp_stack = MyStack(self.my_stack.pop())
                while not self.my_stack.is_empty():
                    self.temp_stack.push(self.my_stack.pop())
                self.my_stack = None
            return self.temp_stack.pop()

        def push(self, data):
            if self.temp_stack is not None and self.my_stack is None:
                self.my_stack = MyStack(self.temp_stack.pop())
                while not self.temp_stack.is_empty():
                    self.my_stack.push(self.temp_stack.pop())
                self.temp_stack = None
            self.my_stack.push(data)
            return None


def question5():
    title = 'Sort Stack'
    question = 'Write a program to sort a stack such that the smallest items are on the top. You can use an ' \
               'additional temporary stack, but you may not copy the elements into any other data structure ' \
               '(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.'

    def sort_stack(stack):
        temp_stack = MyStack(stack.pop())
        while not stack.is_empty():
            data = stack.pop()
            if data > temp_stack.peek():
                temp_stack.push(data)
            else:
                while not temp_stack.is_empty():
                    stack.push(temp_stack.pop())
                temp_stack.push(data)
        while not temp_stack.is_empty():
            stack.push(temp_stack.pop())


def question6():
    title = 'Animal Shelter'
    question = ' An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" ' \
               'basis. People must adopt either the"oldest" (based on arrival time) of all animals at the shelter, ' \
               'or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of ' \
               'that type). They cannot select which specific animal they would like. Create the data structures to ' \
               'maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and ' \
               'dequeueCat. You may use the built-in Linked list data structure.'
    from time import time as get_time
    from random import randint

    class MyQueue:
        def __init__(self, data):
            if data is None:
                self.first = self.last = None
            else:
                self.first = self.last = Node(data)

        def add(self, data):
            new_item = Node(data)
            if self.last is not None:
                self.last.next = new_item
            self.last = new_item
            if self.first is None:
                self.first = self.last
            return None

        def remove(self):
            if self.first is None:
                raise IndexError("Queue is empty")
            data = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            return data

        def peek(self):
            if self.first is None:
                raise IndexError("Queue is empty")
            return self.first.data

        def is_empty(self):
            return self.first is None

    class Animal:
        def __init__(self, animal_type='dog'):
            if animal_type not in ['cat', 'dog']:
                raise ValueError('[{type} is not valid. Must be "cat" or "dog"]'.format(type=type))
            self.time = get_time()
            self.type = animal_type

        def set_time(self, time=None):
            if time is None:
                time = get_time()
            self.time = time

        def get_time(self):
            return self.time

        def get_type(self):
            return self.type

    class AnimalShelter:
        def __init__(self, animal):
            if animal.get_type() not in ['cat', 'dog']:
                raise ValueError('[{type} is not valid. Must be "cat" or "dog"]'.format(type=type))

            animal.set_time()
            if animal.get_type() == 'dog':
                self.dog_queue = MyQueue(animal)
                self.cat_queue = MyQueue(None)
            elif animal.get_type() == 'cat':
                self.dog_queue = MyQueue(None)
                self.cat_queue = MyQueue(animal)

        def enqueue(self, animal):
            animal.set_time()
            if animal.get_type() == 'dog':
                self.dog_queue.add(animal)
            elif animal.get_type() == 'cat':
                self.cat_queue.add(animal)

        def dequeue_any(self):
            try:
                cat_time = self.cat_queue.peek().get_time()
            except IndexError:
                cat_time = None
            try:
                dog_time = self.dog_queue.peek().get_time()
            except IndexError:
                dog_time = None
            if cat_time is None and dog_time is None:
                raise IndexError("The Cat and Dog queue is empty")
            while cat_time == dog_time:
                # if equal age, make it so equal chance of getting cat or dog
                dog_time += randint(0, 1) - 0.5
            if dog_time is None or cat_time < dog_time:
                return self.dequeue_cat()
            else:
                return self.dequeue_dog()

        def dequeue_dog(self):
            try:
                return self.dog_queue.remove()
            except IndexError:
                try:
                    return self.cat_queue.remove()
                except IndexError:
                    raise IndexError("The Cat and Dog queue is empty")

        def dequeue_cat(self):
            try:
                return self.cat_queue.remove()
            except IndexError:
                try:
                    return self.dog_queue.remove()
                except IndexError:
                    raise IndexError("The Cat and Dog queue is empty")

# def get_animal():
#     if randint(0, 1) == 0:
#         return Animal(animal_type='dog')
#     return Animal(animal_type='cat')
#
# animal_shelter = AnimalShelter(get_animal())
# for i in range(8):
#     animal_shelter.enqueue(get_animal())
