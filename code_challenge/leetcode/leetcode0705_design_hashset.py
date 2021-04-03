# Status
#   solved by myself        : kind of
#   submitted to leetcode   : yes


class HashSet:
    """
    Pretty damn slow and not much details were implemented or considered.
    #TODO Update a more advanced and detailed version
    """

    def __init__(self):
        self.size = 10000
        self.buckets = [[]] * self.size

    def hash_function(self, key):
        return key % self.size

    def add(self, key):
        if self.contains(key):
            self.buckets[self.hash_function(key)].append(key)

    def remove(self, key):
        if self.contains(key):
            self.buckets[self.hash_function(key)].remove(key)

    def contains(self, key):
        return key in self.buckets[self.hash_function(key)]
