
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        return f"First Name: {self.first_name}\nLast Name : {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nRewards Member : {self.is_rewards_member} \nGold Cards Points : {self.gold_card_points}"

    def enroll (self):
        if self.is_rewards_member:
            print("User is a member ")
            return False
        else: 
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"Enroll completed for user: {self.first_name}")
            return True
    def spend_points(self,amount):
        if self.gold_card_points<amount:
           print(f"points insufficient for user: {self.first_name}")
        else:
            self.gold_card_points -= amount
            print(f"{amount} points spent" )
            

user_1 = User("Adel","Khedhiri","khedhiri.adel@gmail.com",44)
print(user_1.display_info())
user_2 = User("Ahmed","Labidi","labidi.ahmed@gmail.com",30)
user_3 = User("Alaa","AlaaTN","Alaa.tn@gmail.com",28)
print("-"*50)
user_1.enroll()
user_1.spend_points(50)
print("-"*50)
user_2.enroll()
print("-"*50)
user_2.spend_points(80)
print("-"*50)
print(user_1.display_info())
print("-"*50)
print(user_2.display_info())
print("-"*50)
user_3.enroll()
print("-"*50)
user_3.spend_points(40)
print("-"*50)
print(user_3.display_info())




