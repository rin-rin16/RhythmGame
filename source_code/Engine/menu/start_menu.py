class Buttons:

    def __init__(self, x, y, xsize, ysize, text):
        self.x = x
        self.y = y
        self.text = text
        self.xsize = xsize
        self.ysize = ysize

    def is_click(self, event):
        if abs(self.x - event.pos[0]) < self.xsize and abs(self.y - event.pos[1]) < self.ysize:
            return True