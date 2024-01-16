class Band:
  "Initializes band with band members and a band name. Keeps track of various band instances with the 'instances' list."

  instances = []

  def __init__(self, bandname, members=None):
    self.name = bandname
    self.members = members
    self.instances.append(self)

  def __str__(self):
    return  f"We are {self.name}."
  
  def __repr__(self):
    return  f"Band instance. Name = {self.name}"

  def play_solos(self):
    solos = []
    for i in self.members:
      solos.append(i.play_solo())
    return solos
  
  @classmethod
  def to_list(cls):
    return cls.instances

class Musician:
  "The class of Musician is a superclass for musician types. The musician is the individual, and thus holds the persons name."
  def __init__(self, fullname):
    self.name = fullname

class Guitarist(Musician):
  "Guitarist is a type of musician, and thus is a subclass of that group. The guitarists introduce themselves as such and of course, have a guitar instrument as represented by get_instrument. Additionally, guitarists have a signiture solo."
  def __init__(self, fullname):
    Musician.__init__(self, fullname)

  def __str__(self):
    return  f"My name is {self.name} and I play guitar"
  
  def __repr__(self):
    return  f"Guitarist instance. Name = {self.name}"
  
  @staticmethod
  def get_instrument():
    return "guitar"
  
  def play_solo(self):
    return "face melting guitar solo"

class Bassist(Musician):
  "Bassist is a type of musician, and thus is a subclass of that group. The bassists introduce themselves as such and of course, have a bass instrument as represented by get_instrument. Additionally, bassists have a signiture solo."
  def __init__(self, fullname):
    Musician.__init__(self, fullname)

  def __str__(self):
    return  f"My name is {self.name} and I play bass"
  
  def __repr__(self):
    return  f"Bassist instance. Name = {self.name}"
  
  @staticmethod
  def get_instrument():
    return "bass"
  
  def play_solo(self):
    return "bom bom buh bom"

class Drummer(Musician):
  "Drummer is a type of musician, and thus is a subclass of that group. The drummer introduce themselves as such and of course, have a drum instrument as represented by get_instrument. Additionally, drummers have a signiture solo."
  def __init__(self, fullname):
    Musician.__init__(self, fullname)

  def __str__(self):
    return  f"My name is {self.name} and I play drums"
  
  def __repr__(self):
    return  f"Drummer instance. Name = {self.name}"
  
  @staticmethod
  def get_instrument():
    return "drums"
  
  def play_solo(self):
    return "rattle boom crash"
