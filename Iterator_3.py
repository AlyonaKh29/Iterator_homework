class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index = -1
        self.my_list = self.align_list(self.list_of_list)

    def __iter__(self):
        return self

    def align_list(self, sublist):
        result_list = []
        for item in sublist:
            if isinstance(item, list):
                result_list.extend(self.align_list(item))
            else:
                result_list.append(item)
        return result_list

    def __next__(self):
        self.index += 1
        if self.index == len(self.my_list):
            raise StopIteration
        item = self.my_list[self.index]
        return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
