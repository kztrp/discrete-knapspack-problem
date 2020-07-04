class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self) -> str:
        return "Weight: {} Value: {}".format(self.weight, self.value).__str__()

