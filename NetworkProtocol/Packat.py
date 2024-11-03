class Tag:
    Number = 0
    Data = []

    def __init__(self, number, data):
        self.Number = number
        self.Data = data
        pass

class Packet:

    Tags: list[Tag] = []

    def __init__(self, tags: list[Tag]):
        self.Tags = tags
        pass