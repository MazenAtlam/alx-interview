#!/usr/bin/python3
"""A module that checks locked boxes."""


def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked."""
    boxes_count = len(boxes)
    if boxes_count < 1:
        return True

    my_keys = {0}
    opened_boxes = set()

    return boxes_check(boxes, my_keys, opened_boxes, boxes_count)


def boxes_check(boxes, my_keys, opened_boxes, boxes_count):
    """Check on each box to determine if it can be opened."""
    if len(my_keys) < 1:
        return len(opened_boxes) >= boxes_count

    my_keys_list = list(my_keys)
    for box_index in my_keys_list:
        opened_boxes.add(box_index)
        box_keys = boxes[box_index]
        my_keys.update(box_keys)
        my_keys = set(filter(lambda index: index < boxes_count, my_keys))
        my_keys = set(filter(lambda index: index not in opened_boxes, my_keys))

    return boxes_check(boxes, my_keys, opened_boxes, boxes_count)
