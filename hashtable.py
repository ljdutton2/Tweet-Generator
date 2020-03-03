

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Loop through all buckets
        values = []
        for bucket in self.buckets:
            #  Collect all values in each bucket
            for value in bucket.items():
                values.append(value)
        return values

      

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Loop through all buckets
        total=0
        for bucket in self.buckets:
        # Count number of key-value entries in each bucket
            for key in bucket.items():
                total += 1
                #if isinstance(key,bucket):
                    #total += len(value)
        return total

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
              #Find bucket where given key belongs
        index = self._bucket_index(key)
        ll = self.buckets[index]
        #  Check if key-value entry exists in bucket
        result = ll.find(lambda item: item[0] == key)
        
        if result is not None:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        #  Find bucket where given key belongs
        index = self._bucket_index(key)
        #  Check if key-value entry exists in bucket
        ll = self.buckets[index]
        #  If found, return value associated with given key
        value = ll.find(lambda item: item[0] == key)
        #  Otherwise, raise error to tell user get failed
        if value != None:
            return value[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        #Find bucket where given key belongs
        index = self._bucket_index(key)
        ll = self.buckets[index]
        #  Check if key-value entry exists in bucket
        print("To update", key, value)
        result = ll.find(lambda item: item[0] == key)
        #  If found, update value associated with given key
        print(result)
        if result is not None:
            print("hello")
            ll.print_ll()
            ll.delete((key, result[1]))
            ll.print_ll()
            ll.append((key,value))
        else:
            ll.append((key,value))


        #  Otherwise, insert given key-value entry into bucket


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    #test_hash_table()
    ht = HashTable()
    ht.set('I', 1)
    ht.set('V', 4)
    ht.set('X', 9)
    #assert ht.length() == 3
    ht.set('V', 5)  # Update value
    #ht.set('X', 10)  # Update value
    print("Hello")
    #assert ht.get('I') == 1
    #assert ht.get('V') == 5
    #assert ht.get('X') == 10
    #assert ht.length() == 3  # Check length is not overcounting