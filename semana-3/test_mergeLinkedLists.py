import pytest
from linkedlist import *

def mergeLinkedLists(linkedList_one, linkedList_two):
    """Merge two doubly linked lists that are in sorted order.

    Merge two doubly linked lists that are in sorted order. The merged list will also be in sorted order. The merge is done in place, so the returned linked list is `linkedList_one` with its head updated.

    Args:
        linkedList_one (LinkedList): The first linked list to merge.
        linkedList_two (LinkedList): The second linked list to merge.

    Returns:
        LinkedList: The merged linked list, with its head updated to reflect the new head of the merged list.
    """
    if not linkedList_one:
        return linkedList_two
    if not linkedList_two:
        return linkedList_one

    if linkedList_one.value < linkedList_two.value:
        merged_head = linkedList_one
        linkedList_one = linkedList_one.next
    else:
        merged_head = linkedList_two
        linkedList_two = linkedList_two.next

    merged_tail = merged_head

    while linkedList_one and linkedList_two:
        if linkedList_one.value < linkedList_two.value:
            merged_tail.next = linkedList_one
            linkedList_one.prev = merged_tail
            linkedList_one = linkedList_one.next
        else:
            merged_tail.next = linkedList_two
            linkedList_two.prev = merged_tail
            linkedList_two = linkedList_two.next

        merged_tail = merged_tail.next

    if linkedList_one:
        merged_tail.next = linkedList_one
        linkedList_one.prev = merged_tail
    else:
        merged_tail.next = linkedList_two
        linkedList_two.prev = merged_tail

    return merged_head


@pytest.fixture(scope="session")
def data():
    
    array = []
    
    # test 1 data
    array.append([[2,6,7,8],[1,3,4,5,9,10]])

    # test 2 data
    array.append([[1,2,3,4,5],[6,7,8,9,10]])

    # test 3 data
    array.append([[6,7,8,9,10],[1,2,3,4,5]])

    # test 4 data
    array.append([[1,3,5,7,9],[2,4,6,8,10]])

    # test 5 data
    array.append([[0,1,2,3,4,5,7,8,9,10],[6]])

    # test 6 data
    array.append([[6],[0,1,2,3,4,5,7,8,9,10]])

    # test 7 data
    array.append([[1],[2]])

    # test 8 data
    array.append([[2],[1]])

    # test 9 data
    array.append([[1,1,1,3,4,5,5,5,10],[1,1,2,2,5,6,10,10]])
    
    return array

def test_1(data):
    """
    Test evaluation for [[2,6,7,8],[1,3,4,5,9,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[0][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[0][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test


def test_2(data):
    """
    Test evaluation for [[1,2,3,4,5],[6,7,8,9,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[1][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[1][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_3(data):
    """
    Test evaluation for [[6,7,8,9,10],[1,2,3,4,5]]
    """
    linkedlist_one = LinkedList()
    for item in data[2][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[2][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_4(data):
    """
    Test evaluation for [[1,3,5,7,9],[2,4,6,8,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[3][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[3][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_5(data):
    """
    Test evaluation for [[0,1,2,3,4,5,7,8,9,10],[6]]
    """
    linkedlist_one = LinkedList()
    for item in data[4][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[4][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [0,1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_6(data):
    """
    Test evaluation for [[6],[0,1,2,3,4,5,7,8,9,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[5][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[5][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [0,1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_7(data):
    """
    Test evaluation for [[1],[2]]
    """
    linkedlist_one = LinkedList()
    for item in data[6][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[6][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_8(data):
    """
    Test evaluation for [[2],[1]]
    """
    linkedlist_one = LinkedList()
    for item in data[7][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[7][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_9(data):
    """
    Test evaluation for [[1,1,1,3,4,5,5,5,10],[1,1,2,2,5,6,10,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[8][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[8][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,1,1,1,1,2,2,3,4,5,5,5,5,6,10,10,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test
