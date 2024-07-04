#!/usr/bin/python3

def canUnlockAll(boxes):
    """determines if all the boxes can be opened

        Args:
            boxes(list): list of boxes that may contain
                keys to open other boxes in the list.

        Return:
            True if all boxes can be opened, else return False
    """
    uniqueKeys = set(boxes[0])
    visitedBoxes = {0, }

    while True:
        newKeys = set()

        for key in uniqueKeys:
            if key not in visitedBoxes and key < len(boxes):
                visitedBoxes.add(key)
                newKeys.update(boxes[key])

        if not newKeys.difference(uniqueKeys):
            break

        uniqueKeys.update(newKeys)

    return len(visitedBoxes) == len(boxes)
