class Judge_matching:
    def __init__(self, value):
        self.value = value

    def is_true(self):
        return bool(self.value)

    def is_false(self):
        return not bool(self.value)

Judge1 = Judge_matching(5)
Judge2 = Judge_matching(0)
Judge3 = Judge_matching(True)
Judge4 = Judge_matching(False)

print(Judge1.is_true())
print(Judge1.is_false())

print(Judge2.is_true())
print(Judge2.is_false())

print(Judge3.is_true())
print(Judge3.is_false())

print(Judge4.is_true())
print(Judge4.is_false())