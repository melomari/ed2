import pytest
from binarysearchtree import *

def validateThreeNodes(bst, valueOne, valueTwo, valueThree):
    nodeOne = bst.search(valueOne)
    if not nodeOne:
        return False

    nodeTwo = bst.search(valueTwo)
    if not nodeTwo:
        return False

    nodeThree = bst.search(valueThree)
    if not nodeThree:
        return False

    if nodeTwo.is_descendant(nodeOne):
        if nodeThree.is_descendant(nodeTwo):
            return True
    elif nodeOne.is_descendant(nodeTwo):
        if nodeThree.is_ascendant(nodeTwo):
            return True

    return False



@pytest.fixture(scope="session")
def data():
    
    array = [[5, 2, 1, 0, 4, 3, 7, 6, 8],
             [5, 3, 2, 1, 0, 4, 7, 6, 8],
             [5, 3, 2, 1, 0, 4, 7, 6, 8],
             [2, 1, 3, 4, 5, 6, 7, 8, 9],
             [6, 4, 3, 1, 2, 8, 7, 9],
             [2, 1, 3, 4],
             [8, 4, 3, 2, 1, 10, 9, 14, 12, 11, 6, 7, 13],
             [8, 7, 6, 5, 4, 3, 2, 1, 9],
             [3, 2, 1],
             [3, 2, 1],
             [6, 4, 2, 1, 3, 5, 8, 7, 9],
             [10, 6, 5, 3, 1, 2, 4, 8, 7, 9, 15, 14, 13, 11, 12, 18, 17, 16],
             [10, 6, 5, 3, 1, 2, 4, 8, 7, 9, 15, 14, 13, 11, 12, 18, 17, 16],
             [5, 3, 1, 0, 2, 4, 7, 6, 8],
             [5, 3, 1, 0, 2, 4, 7, 6, 8]]
    return array

def test_1(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "3","nodeTwo": "2"
    """
    bst = BST()
    for value in data[0]:
      bst.add(value)
    assert validateThreeNodes(bst,5,2,3) == True

def test_2(data):
    """
    Test evaluation for "nodeOne": "5", "nodeThree": "1", "nodeTwo": "8",
    """
    bst = BST()
    for value in data[1]:
      bst.add(value)
    assert validateThreeNodes(bst,5,8,1) == False

def test_3(data):
    """
    Test evaluation for   "nodeOne": "8","nodeThree": "2","nodeTwo": "5",
    """
    bst = BST()
    for value in data[2]:
      bst.add(value)
    assert validateThreeNodes(bst,8,5,2) == False

def test_4(data):
    """
    Test evaluation for  "nodeOne": "2","nodeThree": "8","nodeTwo": "5"
    """
    bst = BST()
    for value in data[3]:
      bst.add(value)
    assert validateThreeNodes(bst,2,5,8) == True

def test_5(data):
    """
    Test evaluation for "nodeOne": "4", "nodeThree": "2", "nodeTwo": "1",
    """
    bst = BST()
    for value in data[4]:
      bst.add(value)
    assert validateThreeNodes(bst,4,1,2) == True

def test_6(data):
    """
    Test evaluation for "nodeOne": "1","nodeThree": "3","nodeTwo": "2",
    """
    bst = BST()
    for value in data[5]:
      bst.add(value)
    assert validateThreeNodes(bst,1,2,3) == False

def test_7(data):
    """
    Test evaluation for "nodeOne": "2","nodeThree": "13","nodeTwo": "4"
    """
    bst = BST()
    for value in data[6]:
      bst.add(value)
    assert validateThreeNodes(bst,2,4,13) == False

def test_8(data):
    """
    Test evaluation for "nodeOne": "8","nodeThree": "1","nodeTwo": "7"
    """
    bst = BST()
    for value in data[7]:
      bst.add(value)
    assert validateThreeNodes(bst,8,7,1) == True

def test_9(data):
    """
    Test evaluation for "nodeOne": "2","nodeThree": "3","nodeTwo": "1"
    """
    bst = BST()
    for value in data[8]:
      bst.add(value)
    assert validateThreeNodes(bst,2,1,3) == False

def test_10(data):
    """
    Test evaluation for "nodeOne": "1", "nodeThree": "3", "nodeTwo": "2"
    """
    bst = BST()
    for value in data[9]:
      bst.add(value)
    assert validateThreeNodes(bst,1,2,3) == True

def test_11(data):
    """
    Test evaluation for "nodeOne": "9","nodeThree": "6","nodeTwo": "8"
    """
    bst = BST()
    for value in data[10]:
      bst.add(value)
    assert validateThreeNodes(bst,9,8,6) == True

def test_12(data):
    """
    Test evaluation for "nodeOne": "12","nodeThree": "15","nodeTwo": "13"
    """
    bst = BST()
    for value in data[11]:
      bst.add(value)
    assert validateThreeNodes(bst,12,13,15) == True

def test_13(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "15","nodeTwo": "10"
    """
    bst = BST()
    for value in data[12]:
      bst.add(value)
    assert validateThreeNodes(bst,5,10,15) == False

def test_14(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "4","nodeTwo": "3"
    """
    bst = BST()
    for value in data[13]:
      bst.add(value)
    assert validateThreeNodes(bst,5,3,4) == True

def test_15(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "1","nodeTwo": "3"
    """
    bst = BST()
    for value in data[14]:
      bst.add(value)
    assert validateThreeNodes(bst,5,3,1) == True
