import numpy as np
import mmh3


class BloomFilter:
    def __init__(self, size, hashes):
        self._size = size
        self._hashes = hashes
        self._bits = np.empty(size, dtype='bool')

    def _hash(self, data):
        return mmh3.hash64(data)

    def _nth_hash(self, n, a, b, size):
        return (a + n * b) % size

    def add(self, data):
        values = self._hash(data)

        for i in range(self._hashes):
            self._bits[self._nth_hash(i, values[0], values[1], self._size)] = True

    def possibly_contains(self, data):
        values = self._hash(data)

        for i in range(self._hashes):
            if not self._bits[self._nth_hash(i, values[0], values[1], self._size)]:
                return False

        return True

    def remove(self, data):
        values = self._hash(data)

        for i in range(self._hashes):
            self._bits[self._nth_hash(i, values[0], values[1], self._size)] = False


def main():
    bloom = BloomFilter(100, 3)
    bloom.add('abcd'.encode())
    bloom.add('bcde'.encode())
    print(bloom.possibly_contains('cdef'.encode()))
    print(bloom.possibly_contains('abcd'.encode()))
    print(bloom.possibly_contains('bcde'.encode()))
    bloom.remove('bcde')
    print(bloom.possibly_contains('bcde'.encode()))


if __name__ == '__main__':
    main()
