#!/usr/bin/python3
""" Solution to canUnlockAll Challenge"""
boxes_states = []
boxes_g = []


def check_box(n):
    """
    check nth box, mark opened box and go on till no key
    is found or visited box already opened
    """
    if n is None or n >= len(boxes_g) or boxes_states[n] == 1:
        return
    # mark that box as opened
    boxes_states[n] = 1
    for box in boxes_g[n]:
        check_box(box)


def canUnlockAll(boxes):
    global boxes_g, boxes_states
    if boxes is None:
        return False
    len_boxes = len(boxes)
    if len_boxes == 0:
        return True
    boxes_states = [0] * len_boxes
    boxes_g = boxes
    # first box is already opened
    check_box(0)
    return all(box_state == 1 for box_state in boxes_states)
