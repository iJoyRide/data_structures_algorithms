class User:
    def __init__(self, username, name, email):
        
        self.username = username
        self.name = name
        self.email = email
        print(f"{self.username}'s account have been ceated")
        
    
    # def introduce(self, guest_name):
    #     print(f"Hi {guest_name} I am {self.username}, contact me at {self.email} ") 
    
    def __repr__(self):
        return f"User(username='{self.username}', name='{self.name}', email='{self.email}')"
    
    def __str__(self):
        return self.__repr__()

class UserDatabase:
    def __init__(self):
        self.users = []
        
    def insert(self, user):
        i = 0 
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
        return print(f"{user.name} has been added to the database! \n")
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return print(f"You are retrieving {username}'s information: \n{user} \n")
        return print("User not found! \n")
    
    def update(self, user):
        target = self.find(user.username)
        target.name , target.email = user.name, user.email
        
        return print(f"{user.name}'s {user.email} had been updated! \n")
    def delete(self, username):
        for user in self.users:
            if user == username:
                
                while True:
                    confirmation = input(f"Are you sure you want to delete {username}'s account? (y/n): ").strip().lower()

                    if confirmation == 'y':
                        self.users.remove(user)
                        print(f"{username} has been deleted from the database!\n")
                        return  # Exit the function after deletion
                    elif confirmation == 'n':
                        print("Operation cancelled!\n")
                        return  # Exit the function without deleting
                    else:
                        print("\nInvalid input. Please enter 'y' for yes or 'n' for no.\n")        
                        
    def list_all(self):
        return print(f"This is the entire list of users: \n{self.users} \n")
    
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
print("\n")

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]



database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

database.list_all()

database.delete(siddhant)

user = database.find('siddhant')

database.list_all()