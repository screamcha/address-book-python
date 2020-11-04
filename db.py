import os
import pickle

class DB:
  @classmethod
  def storeValue(cls, filename, value):
    try:
      f = open(filename, 'wb')
      pickle.dump(value, f)
      f.close()
    except:
      print('Error storing {} to file {}'.format(value, filename))
  
  @classmethod
  def retrieveValue(cls, filename):
    if not os.path.exists(filename):
      print('File {} doen\'t exist'.format(filename))
      return
    elif os.stat(filename).st_size == 0:
      print('File {} is empty'.format(filename))
      return

    f = open(filename, 'rb')
    value = pickle.load(f)
    f.close()
    return value
