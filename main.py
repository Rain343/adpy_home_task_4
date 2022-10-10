class FlatIterator:
    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        self.cursor = 0
        self.cursor_2 = -1
        return self

    def __next__(self):
        if len(self.list_[self.cursor])-1 == self.cursor_2:
            self.cursor += 1
            self.cursor_2 = -1

        if len(self.list_) == self.cursor:
            raise StopIteration

        self.cursor_2 += 1
        

        return self.list_[self.cursor][self.cursor_2]


def flat_generator(list_):
    for item in list_:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item
    

if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    print('FlatIterator')
    for item in FlatIterator(nested_list):
        print(item) 

    print([item for item in FlatIterator(nested_list)])

    print('flat_generator')
    for item in flat_generator(nested_list):
        print(item)

    print([item for item in flat_generator(nested_list)])