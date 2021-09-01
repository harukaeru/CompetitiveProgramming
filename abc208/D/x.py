from queue import PriorityQueue
q = PriorityQueue()
q.put((10,'Red balls'))
q.put((8,'Pink balls'))
q.put((5,'White balls'))
q.put((4,'Green balls'))
while not q.empty():
    item = q.get()
    print(item)
