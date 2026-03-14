class GymMember:

    def __init__(self, name, membership_id, fee):
        self.name = name
        self.membership_id = membership_id
        self.fee = fee

    def display_details(self):
        print("Name:", self.name)
        print("Membership ID:", self.membership_id)
        print("Monthly Fee:", self.fee)


# Creating objects
member1 = GymMember("Ali", 101, 3000)
member2 = GymMember("Sara", 102, 3500)
member3 = GymMember("Ahmed", 103, 3200)

# Display details
member1.display_details()
print()
member2.display_details()
print()
member3.display_details()

# Calculate total revenue
total_revenue = member1.fee + member2.fee + member3.fee
print("\nTotal Monthly Revenue:", total_revenue)