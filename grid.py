import pygame
from colors import Colors
class Grid:
    def __init__(self):
        self.num_rows=20    #地图的行数
        self.num_cols=10    #地图的列数
        self.cell_size=30   #cell_size是指每个格子的大小，单位是像素（pixel）
        #地图用二维列表来存储，全部元素初始化为0
        self.grid=[[0 for j in range(self.num_cols)]
                   for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                    print(self.grid[row][col],end=" ")
            print()

    def draw(self,screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value=self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size+1,row*self.cell_size+1,
                            self.cell_size-1,self.cell_size-1)#调整了每个格子的大小，从而使格子的颜色呈现出来
                pygame.draw.rect(screen,self.colors[cell_value],cell_rect)










