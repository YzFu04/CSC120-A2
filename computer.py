class Computer:
  # What attributes will it need?
  """
  description: str
  processor_type: str
  hard_drive_capacity: int
  memory: int
  operating_system: str
  year_made: int
  price: int
  """
  
  # How will you set up your constructor?
  # Remember: in python, all constructors have the same name (__init__)
  """
  Setting up constructor and convert type just in case
  """
  def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price): 
    self.description = description
    self.processor_type = processor_type
    self.hard_drive_capacity = int(hard_drive_capacity)
    self.memory = int(memory)
    self.operating_system = operating_system
    self.year_made = int(year_made)
    self.price = int(price)
    
  # What methods will you need?
  """
  storing information about a specific computer
  """
  def print_computer(self):
    print(self.description, 
          self.processor_type,
          self.hard_drive_capacity, 
          self.memory, 
          self.operating_system, 
          self.year_made, 
          self.price)