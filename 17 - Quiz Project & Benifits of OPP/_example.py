class User():
    pass

#less efficient way to set attributes
user_one = User()
user_one.id = "001"
user_one.username = "yeasir"

user_two = User()
user_two.id = "002"
user_two.username = "jack"

#print(user_one.id)
#print(user_two.username)

#---------------------------------------------------------------------

#correct method
class SocialUser():
    def __init__(self, id, username): #attributes things that the class has (runs when class is initialized)
        print("new user being created...")
        self.id = id
        self.username = username
        self.followers = 0 #default value of 0 given
        self.following = 0 #default value of 0 given
    
    def follow(self, user): #methods things that class can do.
        user.followers += 1
        self.following += 1

user_1 = SocialUser("001", "yeasir01")
user_2 = SocialUser("002", "jack1988")

user_1.follow(user_2) #user 1 following user two

print(f"User One -> Followers: {user_1.followers} Following: {user_1.following}")
print(f"User Two -> Followers: {user_2.followers} Following: {user_2.following}")
