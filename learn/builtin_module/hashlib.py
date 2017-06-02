
import hashlib

md5 = hashlib.md5()
md5.update("I am the password.")
print md5.hexdigest()

md5 = hashlib.md5()
md5.update("I am the ")
md5.update("password.")
print md5.hexdigest()

class UserDatabase(object):
  md5_salt = "dk18xUa"
  db = {}

  def register(self, user, password):
    password_md5 = self.calc_md5(user, password)
    self.db[user] = password_md5
  
  def login(self, user, password):
    password_md5 = self.calc_md5(user, password)
    return self.db[user] == password_md5
  
  def calc_md5(self, user, password):
    md5 = hashlib.md5()
    md5.update(user + password + self.md5_salt)
    return md5.hexdigest()

db = UserDatabase()

md5 = hashlib.md5()
md5.update("123456")
password_md5 = md5.hexdigest()

db.register("Tom", password_md5)
print db.login("Tom", password_md5)

