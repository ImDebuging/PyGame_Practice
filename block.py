from colors import Colors
from position import Position
import pygame
class Block():#七种方块的父类
    def __init__(self,id):
        self.id = id
        self.cells = {}
        self.cell_size = 30


        self.rotation_state = 0
        self.row_offset = 0
        self.col_offset = 0 # 方块左上角的偏移量,初始化为0


        self.colors = Colors.get_cell_colors()
        self.move(0,3)

    def move(self,rows,cols):
        self.row_offset += rows
        self.col_offset += cols

    def get_cell_position(self):    # 返回当前方块里所有格子的坐标
        tiles = self.cells[self.rotation_state]
        moved_tiles=[]
        for position in tiles:
            position = Position(position.row+self.row_offset,position.col+self.col_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation_state = self.rotation_state + 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):    # 当旋转超出屏幕的时候，撤销旋转操作
        self.rotation_state = self.rotation_state - 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1



    def draw(self,screen):
        tiles = self.get_cell_position() # 确定方块的旋转状态
        for tile in tiles:  # 根据旋转状态，将方块里的每个格子打印在屏幕形参screen上
            # tile是一个position（定义在position.py里）的对象
            tile_rect=pygame.Rect(tile.col*self.cell_size+1,tile.row*self.cell_size+1,
                      self.cell_size-1,self.cell_size-1)
            #这边画方格的这些“+1”，“-1”其实就是为了留出一点边框
            pygame.draw.rect(screen,self.colors[self.id],tile_rect)




