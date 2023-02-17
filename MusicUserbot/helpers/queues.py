QUEUE = {}

def add_to_queue(chat_id, songname, link, ref, type, quality):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.append([songname, link, ref, type, quality])
        QUEUE[chat_id] = chat_queue
        return len(chat_queue) - 1
    else:
        QUEUE[chat_id] = [[songname, link, ref, type, quality]]
        return 0

def get_queue(chat_id):
    if chat_id in QUEUE:
        return QUEUE[chat_id]
    else:
        return []

def pop_an_item(chat_id):
    if chat_id in QUEUE:
        chat_queue = QUEUE[chat_id]
        chat_queue.pop(0)
        QUEUE[chat_id] = chat_queue
        return 1
    else:
        return 0

def clear_queue(chat_id):
    if chat_id in QUEUE:
        QUEUE.pop(chat_id)
        return 1
    else:
        return 0
