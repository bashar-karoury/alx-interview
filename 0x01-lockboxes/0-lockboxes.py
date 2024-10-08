#!/usr/bin/python3
""" Solution to canUnlockAll Challenge"""
boxes_states = []
boxes_g = []


def check_box(n, boxes, boxes_states):
    """
    check nth box, mark opened box and go on till no key
    is found or visited box already opened
    """
    if n is None or n >= len(boxes) or boxes_states[n] == 1:
        return
    # mark that box as opened
    if type(boxes[n]) is not list:
        return
    boxes_states[n] = 1
    for box in boxes[n]:
        if type(box) is not int:
            return
        check_box(box, boxes, boxes_states)


def canUnlockAll(boxes):
    if boxes is None or type(boxes) is not list:
        return False
    len_boxes = len(boxes)
    if len_boxes == 0:
        return True
    boxes_states = [0] * len_boxes
    # first box is already opened
    check_box(0, boxes, boxes_states)
    return all(box_state == 1 for box_state in boxes_states)
