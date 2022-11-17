class Column():
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        
        if len(value) > self.size:
            print('size exceeds the maximum setting!')
        else:
            self.name = value

    def __delete__(self, instance):
        print("attribute was deleted")
        del self.name


class User():
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password
    username = Column(name='username', size=5)
    password = Column(name='password', size=10)


u = User()
u.username = 'felix'
u.password = 'passowrd'
print(u.username, u.password)
