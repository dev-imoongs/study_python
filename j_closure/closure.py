def set_topic(topic):
    def set_value(value):
        formatting = f'{topic}: {value}'
        return formatting
    return set_value

set_topic('이름')
