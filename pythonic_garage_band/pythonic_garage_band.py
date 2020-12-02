from abc import abstractmethod

class Band():

    """
    1 - This class is super super parent for all kind of Musician member
    2 - This class has name because everything need name {member or Band it self}
    3 - Method called add_members that added new member to the Band
    4 - Method called play_solos that asks each member musician to play a solo,
    in the order they were added to band.
    """

    band_arr = []

    def __init__(self,name):
        self.name = name
        Band.band_arr.append(self)
    member_arr = []

    def add_members(self,member_name):
        self.member_name = member_name
        Band.member_arr.append(self.member_name)

    def play_solos(self):
        finall = ''
        for i in Band.member_arr:
            finall+= f'{i.play_solos()}\n'
        return finall
    
    @classmethod
    def to_list(cls):
        return cls.member_arr

    def __repr__(self):
        return f"this way to display {self.name} dosen't correct because you can't find and details"
    
    def __str__(self):
        return f"welcome in {self.name} our member {Band.member_arr}"

class Musician():

    """
    Method for all Musician display there name and 
    Method to play solo
    """

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def __str__(self):
        return f"Hello Musician <{self.name}>"

    @abstractmethod
    def __repr__(self):
        return f" '{self.name}' "

    def play_solo(self):
        return f'Welcome Musician {self.name} go and Play solo'

class Guitarist(Musician):

    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return 'guitar'

class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return 'bass'

class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return 'drums'

if __name__ == "__main__":
  hamza = Drummer('Hamza')
#   print(hamza['name'])
  print(hamza.name)
  yani = Band('Yani')
#   print(yani.add_members('free'))
  yani.add_members('Yani')
  yani.add_members('Turkie')
  print(yani.__repr__())
#   print(yani)
  print(Band.band_arr)
#   print(Band.band_arr)
  rashed = Musician('rashed')
  print(rashed.play_solo())
  sndos = Guitarist('sndos')
  print(yani.name)
  print(sndos)
  test = Guitarist('hamza')
  print(test.name)