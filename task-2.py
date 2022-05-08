nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(values):
    for value in values:
        for el in value:
            yield el


if __name__ == '__main__':

    for item in flat_generator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)
