class Band:

  instances = []

  def __init__(self, bandname, members=None):
    self.name = bandname
    self.members = members
    self.instances.append(self)

  def play_solos(self):
    solos = []
    for i in self.members:
      solos.append(i.play_solo())
    return solos
  
  @classmethod
  def to_list(cls):
    return cls.instances

class Musician:
  def __init__(self, fullname):
    self.name = fullname

class Guitarist(Musician):
  def __init__(self, fullname):
    Musician.__init__(self, fullname)

  def __str__(self):
    return  f"My name is {self.name} and I play guitar"
  
  def __repr__(self):
    return  f"Guitarist instance. Name = {self.name}"
  
  def get_instrument(self):
    return "guitar"
  
  def play_solo(self):
    return "face melting guitar solo"

class Bassist(Musician):
  def __init__(self, fullname):
    Musician.__init__(self, fullname)

  def __str__(self):
    return  f"My name is {self.name} and I play bass"
  
  def __repr__(self):
    return  f"Bassist instance. Name = {self.name}"
  
  def get_instrument(self):
    return "bass"
  
  def play_solo(self):
    return "bom bom buh bom"

class Drummer(Musician):
  def __init__(self, fullname):
    Musician.__init__(self, fullname)

  def __str__(self):
    return  f"My name is {self.name} and I play drums"
  
  def __repr__(self):
    return  f"Drummer instance. Name = {self.name}"
  
  def get_instrument(self):
    return "drums"
  
  def play_solo(self):
    return "rattle boom crash"




# joan = Guitarist('Joan Jett')