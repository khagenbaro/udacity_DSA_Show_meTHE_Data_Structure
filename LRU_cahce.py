import re


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.max_size = capacity  # set max size 
        self.cache = {} #create an empty dictionary


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache.keys():  #check if key is there
            data = self.cache.pop(key)  # retrieve if key is there
            self.cache[key] = data  #set the data to the caceh key
            return self.cache[key]     #return cache data
        else :
            return -1  #else return -1


    def set(self, key, data):

        # Set the data if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.max_size > len(self.cache): #check if cache size is greater than ppovided size
            if key not in self.cache.keys():  #then check if key exist or not 
                self.cache[key] = data        #set the cache as data retrieve earlier
        elif key not in self.cache.keys():  # key not in the cache
            if self.max_size <=len(self.cache):  #check max size is less or equal to cache size
                result = dict(reversed(list(self.cache.items())))  # create a dictionary and store cache item
                result.popitem() #pop the item
                result[key] = data   # set data to the result[key]  
                self.cache = result   #get self.cache 

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))     # returns 1
print(our_cache.get(2))    # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache



our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry;
