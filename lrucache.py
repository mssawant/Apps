import queue

class lrucache_node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class lrucache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.curr_size = 0
        self.hmap = {}
        self.head = None
        self.tail = None

    def cache_insert_at_head(self, cnode):
        cnode.next = self.head
        self.head.prev = cnode
        if self.tail == None:
            self.tail = self.head
            self.tail.next = None
        self.head = cnode
        

    def cache_remove_node(self, cnode):
        if cnode.prev != None:
            cnode.prev.next = cnode.next
        if cnode.next != None:
            cnode.next.prev = cnode.prev
        if cnode == self.tail:
            tail = cnode.prev
        cnode.next = None
        cnode.prev = None
        return cnode
    
    def put_kv(self, key, value):
        cnode = None
        if self.hmap.get(key):
            cnode = self.hmap[key]
            # found in the hmap, it must be in the cache, update cache
            # check if its already at head
            if cnode == self.head:
                return
            cnode = self.cache_remove_node(self, cnode)
            self.cache_insert_at_head(self, cnode)
            cnode.value = value
        else:
            # not found in hash, a new node
            cnode = lrucache_node(key, value)
            # if first node in the cache
            if self.head == None:
                self.head = cnode
                self.curr_size += 1
            else:
                # check cache size and update cache
                if self.curr_size < self.capacity:
                    self.cache_insert_at_head(cnode)
                    self.curr_size += 1
                else:
                    # evict tail node and insert new node at head
                    lru_node = self.cache_remove_node(self.tail)
                    self.cache_insert_at_head(cnode)
                    del self.hmap[lru_node.key]
            self.hmap[key] = cnode

    def get_kv(self, key):
        if self.hmap.get(key):
            cnode = self.hmap[key]
            # check if the node is already at head
            if cnode != self.head:
                cnode = self.cache_remove_node(cnode)
                self.cache_insert_at_head(cnode)
            return cnode.value
        else:
            return None

    def lru_print(self):
        cnode = self.head
        while cnode != None:
            print(cnode.key, " ",  cnode.value)
            cnode = cnode.next

def app_cache():
    lru = lrucache(3)
    lru.put_kv("hello", "world")
    lru.put_kv("hello", "mandar")
    lru.put_kv("welcome", "Indu")
    lru.put_kv("Sweet", "Advay")
    lru.put_kv("cute", "Ivan")

    print(lru.capacity, lru.curr_size)
    lru.lru_print()
    print("printing lru cache: ", lru.get_kv("welcome"))
    lru.lru_print()
    print("printing lru cache: ", lru.get_kv("hello"))
    print("printing lru cache: ", lru.get_kv("Sweet"))
    lru.lru_print()

app_cache()
