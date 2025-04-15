def is_symmetric(root):
    if root is None:
        return True
    queue = [root]
    while len(queue) > 0:
        q_len = len(queue)
        for i in range (q_len):
            if queue[i] is None and queue[q_len - i - 1] is None:
                continue
            if queue[i] is None or queue[q_len - i - 1] is None:
                return False
            if queue[i].data != queue[q_len - i - 1].data:
                return False
            queue.append(queue[i].left)
            queue.append(queue[i].right)
        queue = queue[q_len:]
    return True

