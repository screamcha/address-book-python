from db import DB
from address import Address

class AddressBook:
  def __init__(self):
    storedData = DB.retrieveValue('book.data')

    if storedData:
      self.book = storedData[0]
      self.lastId = storedData[1]
      print('Address Book is loaded successfully.')
    else:
      self.book = []
      self.lastId = 1
      print('New Address Book is created successfully.')
  
  def list(self):
    if len(self.book) == 0:
      print('\nAddress Book is empty.')
      return
    else:
      print('Address Book Contents:'.center(50, '_'), end='\n\n')
      for address in self.book:
        address.print()
      print('\nEnd.')
  
  def add(self):
    userId = self.lastId

    fullName = input('Enter Full Name: ')
    email = input('Enter Email (press Enter to skip): ')
    phone = input('Enter Phone Number (press Enter to skip): ')
    
    address = Address(userId, fullName, email, phone)

    self.book.append(address)
    self.lastId += 1
    DB.storeValue('book.data', (self.book, self.lastId))
    print('\nAddress is successfully added!')
  
  def findAddress(self, id):
    address = None

    for x in self.book:
        if x.id == int(id):
          address = x
    
    return address

  def modify(self):
    address = None

    while not address:
      addressId = input('Enter the id of the address: ')

      address = self.findAddress(addressId)

      if not address:
        print('Address with the provided id does not exist. Try again.')
      
    fullName = input('Enter Full Name (press Enter to skip): ')
    email = input('Enter Email (press Enter to skip): ')
    phone = input('Enter Phone Number (press Enter to skip): ')

    address.update({ 'name': fullName,  'email': email, 'phone': phone })

    print('\nThe address is successfully updated!\n')

  def delete(self):
    address = None

    while not address:
      addressId = input('Enter the id of the address: ')

      address = self.findAddress(addressId)

      if not address:
        print('Address with the provided id does not exist. Try again.')

      self.book.remove(address)
      DB.storeValue('book.data', (self.book, self.lastId))

      print('\nAddress is successfully deleted!\n')

