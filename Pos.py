class Pos:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y

    def get_list(self):
        return [self.x,self.y]

    def get_tuple(self):
        return self.x,self.y

    def get_transformed_list(self,mult:float=1,sum_x:float=0,sum_y:float=0):
        return [self.x*mult + sum_x,self.y*mult + sum_y]

    def get_transformed_pos(self,mult:float=1,sum_x:float=0,sum_y:float=0):
        x,y = self.get_transformed_list(mult, sum_x, sum_y)
        return Pos(x,y)