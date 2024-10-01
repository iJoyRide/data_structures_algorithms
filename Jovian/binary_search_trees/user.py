class User:
    def __init__(self, username, name, email):
        
        self.username = username
        self.name = name
        self.email = email
        print('User created!')
    
    def introduce(self, guest_name):
        print(f"Hi {guest_name} I am {self.username}, contact me at {self.email} ") 

user2 = User('John', 'John Doe', 'johndoe@example.com')

user2.introduce("David")
    
    