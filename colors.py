class Colors:
    dark_green = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (26, 116, 17)
    yellow = (37, 234, 4)
    purple = (66, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)

    @classmethod #类本身的方法，可以通过直接通过类本身来访问，而不能通过类的实例来访问
    #BTW,cls参数貌似就是单词‘class’的缩写
    def get_cell_colors(cls):
        '''
        返回一个记录颜色RGB数值的列表，调用的时候通过block对象的ID来表示它的颜色
        '''
        return [cls.dark_green,cls.green,cls.red,cls.orange,cls.yellow,cls.purple,cls.cyan,cls.blue]




