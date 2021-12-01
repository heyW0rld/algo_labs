import numpy as np

class ChainNode:

    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class HashTable:

    _COLISION_COUNT = 3

    def __init__(self, count=100) -> None:
        self._count = count
        self._keys = set()
        self._hashtable = np.empty(count, dtype=type)

    def __contains__(self, key) -> bool:
        try:
            self.get(key)
            return True
        except:
            return False

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        res = '{'
        if len(self._keys) > 0:
            for key in self._keys:
                res += f'{key}: {self[key]}, '
            res = res[:-2]

        return res + '}'

    def get(self, key):
        assert key in self._keys, "key is not exist!"

        index = hash(key) % self._count
        chain = self._hashtable[index]
        # так как ключ точно есть, то точно есть и цепочка
        node = chain
        while node:
            if node.key == key:
                return node.value
            node = node.next

        assert False, "Key is not found!"

    def __iter__(self):
        return iter(self._keys)

    def add(self, key, value):

        if not (key in self._keys):
            self._keys.add(key)

        index = hash(key) % self._count
        chain = self._hashtable[index]

        if chain is None:
            self._hashtable[index] = ChainNode(key, value, None)
        else:
            node = chain
            node_count = 1

            if node.key == key:
                node.value = value
                return

            while node.next:
                node = node.next
                node_count += 1

                if node.key == key:
                    node.value = value
                    return

            new_node = ChainNode(key, value, None)
            node.next = new_node

            if node_count >= HashTable._COLISION_COUNT:
                self._resize()

    def pop(self, key):
        assert key in self._keys, "key is not exist!"

        index = hash(key) % self._count
        chain = self._hashtable[index]

        if chain.next is None:
            assert chain.key == key, "key is not equal!"
            self._hashtable[index] = None
            self._keys.remove(key)
            return chain.value

        node = chain.next
        node_back = chain
        while node:
            if node.key == key:
                node_back.next = node.next
                self._keys.remove(key)
                return node.value

            node = node.next
            node_back = node_back.next

        assert False, "Key is not found!"

    def clear(self):
        self._keys.clear()
        self._hashtable = np.empty(self._count, dtype=type)

    def keys(self):
        return self._keys.copy()

    def values(self):
        res = [self[key] for key in self._keys]
        return res

    def items(self):
        res = [(key, self[key]) for key in self._keys]
        return res

    def _resize(self):
        items = self.items()
        self._count *= 2
        self._hashtable = np.empty(self._count, dtype=type)
        for item in items:
            self.add(item[0], item[1])


def main():
    ht = HashTable()
    ht.add(1, 2)
    ht.add(3, 4)
    ht.add(5, 6)
    ht[7] = 8
    print(ht)
    print(ht.get(3))
    print(ht[1])

    print(ht.keys())
    print(ht.values())
    print(ht.items())

    print(5 in ht)
    print(100 in ht)

    print(ht.pop(5))
    print(ht)

    ht.clear()
    print(ht)

    ht_res = HashTable(count=10)

    for i in range(100):
        ht_res[i] = i**2
        print(ht_res._count)

    print(ht_res)


if __name__ == '__main__':
    main()
