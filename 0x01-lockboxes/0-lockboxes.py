#!/usr/bin/python3
""" Solution to canUnlockAll Challenge"""


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
        if not box or box in checked_boxes:
            continue
        # add box keys to unvisited boxes
        if box > 0 and box < len(boxes):
            unvisited_boxes.update(boxes[box])
                # add box to checked_boxes
        checked_boxes.add(box)

    return len(checked_boxes) == len(boxes)
