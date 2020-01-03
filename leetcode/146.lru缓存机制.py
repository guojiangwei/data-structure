#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
# solution1  implement LRU with OrderedDict
# from collections import OrderedDict
# class LRUCache(OrderedDict):

#     def __init__(self, capacity: int):
#         self.capacity = capacity
        

#     def get(self, key: int) -> int:
#         if key not in self :
#             return -1
#         self.move_to_end(key)
#         return self[key]
        

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity :
#             self.popitem(last=False)

class LRUNode():
    def __init__(self):
        # self.capacity=capacity
        self.next=None
        self.prev = None
        self.key = 0
        self.value = 0
    
    
    def delete_node(self):
        self.prev.next=self.next
        self.next.prev = self.prev

class linkedList():
    def __init__(self):
        self.head = LRUNode()
        self.tail = LRUNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def move_to_head(self,node):
        node.delete_node()
        self._insert_head(node)
    
    def _insert_head(self,node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
    
    def  delete_tail(self):
        tail=self.tail.prev
        self.tail.prev.delete_node()
        return tail


        

class LRUCache():

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.linkedList = linkedList()
    
    def _move_to_head(self,node):
        self.linkedList.move_to_head(node)
        

    def get(self, key: int) -> int:
        node =  self.cache.get(key,None) 
        if not node:
            return -1
        self._move_to_head(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        node =  self.cache.get(key) 
        if not node:
            node = LRUNode()
            node.key = key
            node.value = value
            self.linkedList._insert_head(node)
            self.cache[key] = node
            self.size = self.size + 1

            if self.size > self.capacity:
                tail=self.linkedList.delete_tail()
                del self.cache[tail.key]

        else:
            node.value = value
            self._move_to_head(node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

