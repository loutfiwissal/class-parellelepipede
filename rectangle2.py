class rectangle () :
    _count1 = 0
    def __init__(self,LA,LO) :
        self._LA= LA
        self._LO = LO
        rectangle._count1 = rectangle._count1 + 1
    
#getters
    def getLA (self) :
        return self._LA
    def getLO (self) :
        return self._LO

#setters
    def setT (self,LA) :
         self._LA = LA
    def getDS (self,LO) :
        self._LO = LO

#Method
    def Tostring (self) :
        print(f"length  :{(self.getLO())}")
        print(f"width :{(self.getLA())}")
        print(f"number of rectangles :{rectangle._count1}")
    def Equals (self,R1):
        if (self.getLA()==R1.getLA()) and (self.getLO()==R1.getLO()):
            return True
        else :
            return False
        
    def perimetre (self):
        print (f" perimetre  :{(self._LA + self._LO)*2}")
    def surface (self) :
        print (f"the surface :{(self._LO * self._LA)}")

#THE CHILD CLASS:
class parellelepipede (rectangle):
    _count2 = 0
    def __init__(self,LA,LO,H) :
        super().__init__(LA,LO)
        self.__H= H
        parellelepipede._count2 = parellelepipede._count2 + 1

#Getters
    def getH (self) :
        return self.__H
    
#Setters
    def setX (self,H) :
        self.__H = H

    def Tostring (self) :
        print(f"length:{(self.getLO())}")
        print(f"width :{(self.getLA())}")
        print (f"The height :{(self.getH())}")
        print(f"number of parallelepipeds :{rectangle._count1}")


    def Equals (self,R1):
        if (self.getLA()==R1.getLA()) and (self.getLO()==R1.getLO()) and (self.getH()==R1.getH()):
            return True
        else :
            return False
    def volume (self) :
        print(f"volume :{(self._LO * self._LA * self.__H)}")
    def surface (self) :
        print(f"the surface :{(self._LA + self.__H + self._LO )*2}")



#main programme
r1 = rectangle (10,20)
r1 .Tostring()
r1.perimetre()
r1.surface()
r2 = rectangle (10,20)
r2.Tostring()
r2.perimetre()
r2.surface()
print (r1.Equals(r2))

r3 = parellelepipede(10,20,5)
r3.Tostring()
r3.volume()
r3.surface()
r4 = parellelepipede(15,33,6)
r4.Tostring()
r4.volume()
r4.surface()
print (r3.Equals(r4))
