class Dog():
    """a simple attemp to model a dog"""
    def __init__(self, name, age):
        """Initalize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting"""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """simulate a dog rolling over"""
        print(f"\n{self.name.title()} rolled over!")

    def vet(self):
        next_appt = input(f"\nWhen is {self.name.title()} next appt:")
        print(f"\n{next_appt.title()} is {self.name.title()}'s next appt.")

    def shots_updated(self):
        shots = input(f"Are {self.name.title()}'s shots up to date?:(y/n)")
        if shots == 'y'or shots == 'Y':
            print(f"\nThen we can accept {self.name.title()} in our dog care program. ")
        else:
            print(f"\n{self.name.title()}'s shots  must be updated before he is accepted.")



