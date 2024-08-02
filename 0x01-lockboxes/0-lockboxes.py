#!/usr/bin/python3
"""Solves the lock boxes puzzle"""

def get_keys_from_next_unchecked_box(opened_boxes):
    """Gets the keys from the next unchecked box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the unchecked box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None

def canUnlockAll(boxes):
    """Check if all boxes can be unlocked
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be unlocked, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = get_keys_from_next_unchecked_box(aux)
        if keys:
            for key in keys:
                try:
                    if aux.get(key) and aux.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    aux[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)

def main():
    """Entry point"""
    can_unlock_all_boxes([[]])

if __name__ == '__main__':
    main()
