from Rect import Rect

class Pos:
    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y

    def __str__(self):
        return "Pos< X:{0} , Y:{1}>".format(self.x,self.y)


    def get_rect(self,width:float,height:float) -> Rect :
        return Rect(self.x,self.y,0,0)\
            .get_transformed_rect()\
            .set_size(width,height)

    def get_list(self):
        return [self.x,self.y]

    def get_tuple(self):
        return self.x,self.y

    def transform(self,mult:float=1,sum_x:float=0,sum_y:float=0):
        self.x*=mult
        self.y*=mult
        self.x+=sum_x
        self.y+=sum_y

    def get_transformed_list(self,mult:float=1,sum_x:float=0,sum_y:float=0):
        return [self.x*mult + sum_x,self.y*mult + sum_y]

    def get_transformed_pos(self,mult:float=1,sum_x:float=0,sum_y:float=0):
        x,y = self.get_transformed_list(mult, sum_x, sum_y)
        return Pos(x,y)

    def combine(self,pos):
        self.x += pos.x
        self.y += pos.y



