class Ball:
    def __init__(self,color,size,direction):
        self.color=color
        self.size=size
        self.direction=direction

    def bounce(self):
        if self.direction=="vniz":
            self.direction="vverh"

myBall=Ball("krasnii","malenkii","vniz")
#myBall.direction="vniz"
#myBall.color="krasnii"
#myBall.size="malenkii"

print "Ya tolko chto sozdal myach."
print "Razmer moego myacha ", myBall.size
print "Cvet moego myacha ", myBall.color
print "Moi myach dvigetsya ", myBall.direction
print "Seichas ya pomenyau napravlenie dvigeniya myacha "
print
myBall.bounce()
print "Teper myach dvigetsya ",myBall.direction 
 
