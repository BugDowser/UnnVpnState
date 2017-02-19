from vpnutils import user

a = user.user('u-1181', 'ri2fohu')

print(a.is_logined())
print(a.login())
print(a.is_logined())
a.balance()
a.saveUser(b'password')
#a.currentTraffic()
#a.saveTraffic()
#a.savePayments()
#a.saveSessions()
#a.saveUser()
b = user.openUser('u-1181', b'password')
#b.balance()
print(a==b)
#print(a.balance() == b.balance())