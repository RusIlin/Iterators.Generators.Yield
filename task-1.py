nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, some_list):
        self.some_list = some_list
        self.cursor = -1
        self.list_len = len(self.some_list)

    def __iter__(self):
        self.cursor += 1
        self.internal_cursor = 0
        return self

    def __next__(self):
        if self.internal_cursor == len(self.some_list[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.internal_cursor += 1
        return self.some_list[self.cursor][self.internal_cursor - 1]


if __name__ == '__main__':

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
