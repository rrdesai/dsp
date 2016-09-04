# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    count = 0
    for i in words:
        if len(i) >=2:
            if i[0] == i[-1]:
                count += 1
    return count
    
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    raise NotImplementedError


def front_x(words):
    x_list = []
    rest_list = []
    final_list = []
    for i in words:
        if i[0] == 'x':
            x_list.append(i)
        else:
            rest_list.append(i)
    x_list = sorted(x_list)
    rest_list = sorted(rest_list)
    for i in x_list:
        final_list.append(i)
    for i in rest_list:
        final_list.append(i)
    return final_list

    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    raise NotImplementedError


def sort_last(tuples):
    return sorted(tuples, key = lambda x: x[-1])

    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    raise NotImplementedError


def remove_adjacent(nums):
    j = 0
    i = len(nums)-1
    while j < i:
        if nums[j] == nums[j+1]:
            nums.pop(j+1)
            i = len(nums)-1
        else:j+=1
    return nums

    
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    raise NotImplementedError


def linear_merge(list1, list2):
    merged_list = []
    merged_len = len(list1) + len(list2)
    i = 0
    j = 0

    while len(merged_list) !=  merged_len:
        if len(list1) == i:
            merged_list += list2[j:]
            break
        elif len(list2) == j:
            merged_list += list1[i:]
            break
        elif list1[i] < list2[j]:
            merged_list.append(list1[i])
            i+=1
        elif list2[j] < list1[i]:
            merged_list.append(list2[j])
            j+=1
        elif list2[j] == list1[i]:
            merged_list.append(list2[j])
            merged_list.append(list1[i])
            j+=1
            i+=1
    return merged_list
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    raise NotImplementedError
