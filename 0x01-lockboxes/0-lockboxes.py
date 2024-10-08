#!/usr/bin/python3

def canUnlockAll(boxes):
    boxes_count = len(boxes)
    if boxes_count < 1:
        return True

    my_keys = {0}
    opened_boxes = set()

    return boxesCheck(boxes, my_keys, opened_boxes, boxes_count)


def boxesCheck(boxes:list, my_keys:set, opened_boxes:set, boxes_count:int):

    if len(my_keys) < 1:
        if len(opened_boxes) < boxes_count:
            return False
        return True

    my_keys_list = list(my_keys)
    for box_index in my_keys_list:
        opened_boxes.add(box_index)
        box_keys = boxes[box_index]
        my_keys.update(box_keys)
        my_keys = set(filter(lambda key_index: key_index < boxes_count, my_keys))
        my_keys = set(filter(lambda key_index: key_index not in opened_boxes, my_keys))

    return boxesCheck(boxes, my_keys, opened_boxes, boxes_count)
