class Fraction:
    def __init__(self,nr,dr=1):
        self.nr=nr
        self.dr=dr
        if self.dr<0:
            self.nr*=-1
            self.dr*=-1
        self.__reduce__()

    def show(self):
        print(f'{self.nr}/{self.dr}')



    def __str__(self):
         return f'{self.nr}/{self.dr}'

    def __repr__(self):
         return f'Fraction({self.nr}/{self.dr})'

    def __add__(self, other):#magic method __method__
        if isinstance(other,int):
            other=Fraction(other)
        f=Fraction(self.nr*other.dr+other.nr*self.dr)
        f.__reduce__()
        return f
    def __radd__(self, other):#reverse add
        return self.__add__(other)


    def __sub__(self, other):
        if isinstance(other,int):
            other=Fraction(other)
        f=Fraction(self.nr*other.dr-other.nr*self.dr)
        f.__reduce__()
        return f

    def __mult__(self,other):
        if isinstance(other,int):
            other=Fraction(other)
        f=Fraction(self.nr*other.nr,self.dr*other.dr)
        f.__reduce__()
        return f
    def __eq__(self,other):
        return (self.nr*other.dr)==(self.dr*other.nr)

    def __lt__(self, other):
          return (self.nr*other.dr)<(self.dr*other.nr)

    def __le__(self, other):
          return (self.nr*other.dr)<=(self.dr*other.nr)

    def __reduce__(self):
        h=Fraction.hcf(self.nr,self.dr)
        if h==0:
            return
        self.nr//=h
        self.dr//=h
    @staticmethod
    def something():   pass
