#这个文件是俄罗斯方块里具体的七种方块的具体实现
from block import Block
from position import Position

class LBlock(Block):#每一个具体的方块类都继承自Block这个父类
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            #这个字典记录了方块四种旋转状态所占据的格子的坐标
            0:[Position(0,2),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(2,1),Position(2,2)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,0)],
            3:[Position(0,0),Position(0,1),Position(1,1),Position(2,1)]
        }


class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            # 这个字典记录了方块四种旋转状态所占据的格子的坐标
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }


class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            # 这个字典记录了方块四种旋转状态所占据的格子的坐标
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }


class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            # 这个字典记录了方块四种旋转状态所占据的格子的坐标
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }


class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            # 这个字典记录了方块四种旋转状态所占据的格子的坐标
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }


class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            # 这个字典记录了方块四种旋转状态所占据的格子的坐标
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }


class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            # 这个字典记录了方块四种旋转状态所占据的格子的坐标
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }


