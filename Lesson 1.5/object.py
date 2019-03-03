from random import randint
class Goroh():
    color = ""
    height = 0
    shape = ""
    def __init__(self, color, height, shape):
        self.color = color
        self.height = height
        self.shape = shape
    def get_color(self):
        if "A" in self.color:
            return "green"
        else:
            return "yellow"
    def get_height(self):
        if "A" in self.height:
            return "170"
        else:
            return "180"
    def get_shape(self):
        if "A" in self.shape:
            return "round"
        else:
            return "not round"

def mate(gor1, gor2):
    childs = [0]*randint(10, 30)
    for i in range(len(childs)):
        childs[i] = Goroh("", "", "")
        childs[i].color = gor1.color[randint(0,1)] + gor2.color[randint(0,1)]
        childs[i].height = gor1.height[randint(0,1)] + gor2.height[randint(0,1)]
        childs[i].shape = gor1.shape[randint(0,1)] + gor2.shape[randint(0,1)]
    return childs

lucy = Goroh("AA", "Aa", "aa")
papa = Goroh("Aa", "aa", "AA")
mama = Goroh("Aa", "aa", "AA")
childs = mate(papa, mama)
for el in childs:
    print(el.get_color(), el.get_shape(), el.get_height())
