class Deduplicator:
    def __init__(self):
        self.items = []

    def add_item(self, item):
            self.items.append(item)

    def set_item(self):
        return list(set(self.items))

deduplicator = Deduplicator()

deduplicator.add_item('사과')
deduplicator.add_item('바나나')
deduplicator.add_item('딸기')
deduplicator.add_item('수박')
deduplicator.add_item('딸기')
deduplicator.add_item('수박')

# 리스트 출력
print(deduplicator.items)
# 중복 제거
print(deduplicator.set_item())
