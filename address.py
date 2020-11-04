class Address:
  def __init__(self, userId, name, email, phone):
    self.id = userId
    self.name = name
    self.email = email
    self.phone = phone

  def __eq__(self, other):
    return self.id == other.id
  
  def print(self):
    email = self.email
    phone = self.phone

    if not email:
      email = 'Empty'
    
    if not phone:
      phone = 'Empty'

    print(
      'Id: {} | Full Name: {} | Email: {} | Phone Number: {}'
      .format(self.id, self.name, email, phone)
    )
  
  def update(self, fields):
    print(fields)
    for key in fields:
      if not fields[key] == None:
        setattr(self, key, fields[key])