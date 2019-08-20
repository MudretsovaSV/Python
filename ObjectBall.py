class Ball:
    def __init__(self,color,size,direction):
        self.color=color
        self.size=size
        self.direction=direction

    def __str__(self):
        msg="Privet, Ya " + self.size + " "+self.color + " myach!"
        return msg
myBall=Ball("krasnii","malenkii","vniz")
print myBall



 
