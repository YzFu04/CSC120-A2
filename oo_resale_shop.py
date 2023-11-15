from computer import Computer
class ResaleShop:
  # What attributes will it need?
  """
  inventory = []
  """
  # How will you set up your constructor?
  # Remember: in python, all constructors have the same name (__init__)
  """
  Setting up an empty inventory list
  """
  def __init__(self):
    self.inventory = []

  # What methods will you need?
  """
  buying a computer (add to inventory)
  """  
  def buy(self, c):
    self.inventory.append(c)

  """
  selling a computer (remove from inventory)
  """
  def sell(self, c):
    if c in self.inventory:
      self.inventory.remove(c)
      print("Item sold!")
    else: 
      print("Item not found. Please select another item to sell.")

  """
  storing the inventory for the store
  """ 
  def print_inventory(self):
    # If the inventory is not empty
    if self.inventory:
      # For each item
      for c in self.inventory:
          # Print its details
          Computer.print_computer(c)
      else:
        print("No inventory to display.")
        
  """
  updating a computer's price
  """
  def update_price(self, c, new_price):
    if c in self.inventory:
      c.price = new_price
    else:
      print("Item not found. Cannot update price.")

  """
  updating a computer's OS
  """
  def update_os(self, c, new_os):
    if c in self.inventory:
      c.operating_system = new_os
    else:
      print("Item not found. Cannot update os.")

  """
  refurbishing a computer
  """
  def refurbish(self, c, new_os = None):
    if c in self.inventory:
      if int(c.year_made) < 2000:
        c.price = 0 # too old to sell, donation only
      elif int(c.year_made) < 2012:
        c.price = 250 # heavily-discounted price on machines 10+ years old
      elif int(c.year_made) < 2018:
        c.price = 550 # discounted price on machines 4-to-10 year old machines
      else:
        c.price = 1000 # recent stuff
      if new_os is not None :
        c.operating_system = new_os
    else:
      print("Item not found. Cannot refurbish.")
