#!/usr/bin/python3
""" Solution to canUnlockAll Challenge"""


def check_box(n, boxes, boxes_states):
    """
    check nth box, mark opened box and go on till no key
    is found or visited box already opened
    """
    if n is None or type(n) is not int or n >= len(boxes) or n < 0:
        return

    if boxes_states[n] == 1:
        return
    # mark that box as opened
    if type(boxes[n]) is not list:
        return
    boxes_states[n] = 1
    for box in boxes[n]:
        check_box(box, boxes, boxes_states)


def canUnlockAll(boxes):
    """ Function to determine if all boxes can be opened
        Args:
            boxes: (list of lists of int)
        return: True if all boxes can be opened, False else
    """
    if boxes is None or type(boxes) is not list:
        return False
    len_boxes = len(boxes)
    if len_boxes == 0:
        return True

    # first box is already opened
    checked_boxes = set([0])
    if type(boxes[0]) is not list:
        return False
    unvisited_boxes = set(boxes[0])
    while (len(unvisited_boxes)):
        box = unvisited_boxes.pop()
        if box in checked_boxes:
            continue
        # add box to checked_boxes
        checked_boxes.add(box)
        # add box keys to unvisited boxes
        if box < len(boxes):
            unvisited_boxes.update(boxes[box])

    return len(checked_boxes) == len(boxes)
