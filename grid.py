class Grid:
    def __init__(self):
        self.num_rows=20
        self.num_cols=10
        self.cell_size=30
        self.grid=[[0 for j in range(self.num_cols)]
                   for i in range(self.num_rows)]
        self.colors = self.get_cell_color()

    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                    print(self.grid[row][col],end=" ")
            print()

    def get_cell_color(self):
        dark_green = (26,31,40)
        green = (47,230,23)
        red = (232,18,18)
        orange = (26,116,17)
        yellow = (37,234,4)
        purple = (66,0,247)
        cyan = (21,204,209)
        blue = (13,64,216)

        return [dark_green,green,red,orange,yellow,purple,cyan,blue]

    def draw(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value=self.grid[row][col]












