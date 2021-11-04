from temperature import Temperature

class Calorie:
    """Represents amount of calories calculated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.25 * self.height + 5 - self.temperature * 10
        return result

if __name__ == '__main__':
    # get temperature from website.
    temperature = Temperature(country='Italy', city='Rome').get()
    calorie = Calorie(weight=58, height=165, age=31, temperature=temperature)
    print(calorie.calculate())