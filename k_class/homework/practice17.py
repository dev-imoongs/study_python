
class Speaker:
    init_sound = 60
    limit_error_message = '볼륨 조정 범위를 벗어났습니다.'
    turn_on_message = '전원이 켜졌습니다'
    already_turn_on_message = '이미 전원이 켜져있습니다'
    turn_off_message = '전원이 종료되었습니다.'
    already_turn_off_message = '이미 전원이 종료되어있습니다.'

    def __init__(self, check):
        self.check_turn_on = check

    def increase_volume(self):
        if self.check_turn_on:
            if Speaker.init_sound + 20 <= 100:
                Speaker.init_sound += 20
                return Speaker.init_sound
            else:
                return Speaker.limit_error_message
        else:
            print(Speaker.already_turn_off_message)

    def decrease_volume(self):
        if self.check_turn_on:
            if Speaker.init_sound - 20 >= 0:
                Speaker.init_sound -= 20
                return Speaker.init_sound

            else:
                return Speaker.limit_error_message
        else:
            print(Speaker.already_turn_off_message)

    def turn_on_speaker(self):
        if self.check_turn_on:
            return Speaker.already_turn_on_message
        else:
            self.check_turn_on = True
            return Speaker.turn_on_message

    def turn_off_speaker(self):
        if not self.check_turn_on:
            return Speaker.already_turn_off_message
        else:
            self.check_turn_on = False
            return Speaker.turn_off_message


speaker = Speaker(True)
# 증가 한계
print(speaker.increase_volume())
print(speaker.increase_volume())
print(speaker.increase_volume())

# 감소 한계
print(speaker.decrease_volume())
print(speaker.decrease_volume())
print(speaker.decrease_volume())
print(speaker.decrease_volume())
print(speaker.decrease_volume())
print(speaker.decrease_volume())

# 전원 체크
print(speaker.turn_on_speaker())
print(speaker.turn_off_speaker())
print(speaker.turn_off_speaker())
print(speaker.turn_on_speaker())
