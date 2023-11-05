class DoubleElement:
    def __init__(self, *lst):
        self.lst = list(lst)
        self.index = 0

    def __next__(self):
        if len(self.lst) > 0:
            first_element = self.lst.pop(0)
            if len(self.lst) > 0:
                second_element = self.lst.pop(0)
            else:
                second_element = None

            pair = first_element, second_element
            return pair
        else:
            raise StopIteration

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
