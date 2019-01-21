from collections import defaultdict
import numpy as np

def question1():
    title = 'Is Unique'
    question = 'Implement an algorithm to determine if a string has all unique characters. ' \
               'What if you cannot use additional data structures?'

    def is_unique(string):
        # assume ascii
        if not isinstance(string, str) or not isinstance(string, list):
            raise ValueError("Input [{input}] must be ascii".format(input=string))
        if len(string) > 128:
            return False
        ascii_chars = [False for _ in range(128)]
        for char in string:
            char_ = ord(char)
            if ascii_chars[char_]:
                return False
            ascii_chars[char_] = True


def question2():
    title = 'Check Permutation'
    question = 'Given two strings, write a method to decide if one is a permutation of the other.'

    def is_permutation(string1, string2):
        if not isinstance(string1, str) or not isinstance(string2, str):
            raise ValueError("Inputs must be strings")
        if len(string2) != len(string1):
            return False
        char_count1 = get_char_count(string1)
        char_count2 = get_char_count(string2)
        return char_count1 == char_count2

    def get_char_count(string):
        char_count = defaultdict(int)
        for char in string:
            char_count[char] += 1
        return char_count


def question3():
    title = 'URLify'
    question = "Write a method to replace all spaces in a string with '%20'. You may assume that the string has " \
               "sufficient space at the end to hold the additional characters,and that you are given the 'true' " \
               "length of the string."

    def urlify1(string, len):
        string = string[:len]
        return string.replace(' ', '%20')


def question4():
    title = 'Palindrome Permutation'
    question = 'Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is ' \
               'a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of ' \
               'letters. The palindrome does not need to be limited to just dictionary words.'

    def is_palindrome_permutation(string):
        string = string.replace(' ', '').lower()
        char_count = get_char_count(string)
        count_values = np.array(list(char_count.values()))
        num_odd_chars = np.sum(count_values % 2 == 1)
        return len(string) % 2 == num_odd_chars

    def get_char_count(string):
        char_count = defaultdict(int)
        for char in string:
            char_count[char] += 1
        return char_count


def question5():
    title = 'One Away'
    question = 'There are three types of edits that can be performed on strings: insert a character, remove a ' \
               'character, or replace a character. Given two strings, write a function to check if they are one edit ' \
               '(or zero edits) away.'

    def is_one_away(string1, string2):
        if np.abs(len(string1) - len(string2)) >= 2:
            return False
        num_away = get_num_away(string1, string2)

        if num_away <= 1:
            return True
        return False

    def get_num_away(string1, string2):
        char_count1 = get_char_count(string1)
        char_count2 = get_char_count(string2)
        num_away = 0
        for key1, value1 in char_count1.items():
            try:
                if np.abs(value1 - char_count2[key1]) == 0:
                    continue
                elif np.abs(value1 - char_count2[key1]) == 1:
                    num_away += 1
                else:
                    return False
            except KeyError:
                num_away += 1
        return num_away

    def get_char_count(string):
        char_count = defaultdict(int)
        for char in string:
            char_count[char] += 1
        return char_count


def question6():
    title = 'String Compression'
    question = 'Implement a method to perform basic string compression using the counts of repeated characters. ' \
               'For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not ' \
               'become smaller than the original string, your method should return the original string. ' \
               'You can assume the string has only uppercase and lowercase letters (a - z).'

    def compress_string(string):
        compressed_string = []
        count = 1
        for i, char in enumerate(string[:-1]):
            if char != string[i + 1]:
                compressed_string.append(string[i] + str(count))
                count = 0
            count += 1

        # add last char
        compressed_string.append(string[-1] + str(count))

        print(string)
        print(''.join(compressed_string))
        return min(string, ''.join(compressed_string), key=len)


def question7():
    # TODO optimize so rotation is done in place
    title = 'Rotate Matrix'
    question = 'Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a ' \
               'method to rotate the image by 90 degrees. Can you do this in place?'

    def rotate_matrix(matrix):
        new_matrix = np.zeros((len(matrix), len(matrix)))
        for i, row in enumerate(reversed(matrix)):
            new_matrix[:, i] = row
        return new_matrix


def question8():
    title = 'Zero Matrix'
    question = 'Write an algorithm such that if an element in an MxN matrix is 0, ' \
               'its entire row and column are set to 0.'
    def zero_matrix(matrix):
        np_matrix = np.asarray(matrix)
        zero_locations = get_zero_locations(np_matrix)
        for (y, x) in zero_locations:
            np_matrix[y, :] = 0
            np_matrix[:, x] = 0
        return np_matrix.tolist()

    def get_zero_locations(np_matrix):
        return np.argwhere(np_matrix == 0)


def question9():
    title = 'String Rotation'
    question = 'Assume you have a method isSubstring which checks if one word is a substring of another. ' \
               'Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to ' \
               'isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").'

    def is_string_rotation(string1, string2):
        if len(string1) != len(string2):
            return False

        string2_ = string2 + string2
        return is_substring(string2_, string1)

    def is_substring(string, substring):
        return substring in string

