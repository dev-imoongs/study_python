class Diary:
    scedule = {}

    def __init__(self, date, action):
        self.date = date
        self.action = action

    def report_diary(self):
        Diary.scedule[self.date] = self.action

    def find_diary(self):
        print(Diary.scedule)


schedule_update = Diary('07/04','밥먹기')
schedule_update.report_diary()
# 기록
schedule_update = Diary('07/05','잠자기')
schedule_update.report_diary()
# 조회
schedule_update.find_diary()