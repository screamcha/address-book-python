from book import AddressBook

print('!!!Welcome to the Address Book CLI!!!')

book = AddressBook()

while True:
  print('Possible actions:')
  print('1 - list all stored addresses;')
  print('2 - add new address;')
  print('3 - modify an existing address;')
  print('4 - delete an address from the book.', end='\n\n')

  action = input('Please make your choise: ')

  if action == 'exit':
    break
  elif action == '1':
    print('\n')
    book.list()
    print('\n')
  elif action == '2':
    print('\n')
    book.add()
    print('\n')
  elif action == '3':
    print('\n')
    book.modify()
    print('\n')
  elif action == '4':
    print('\n')
    book.delete()
    print('\n')
  else:
    print('Invalid command. Please make a valid choise or input \'exit\'.', end='\n')

