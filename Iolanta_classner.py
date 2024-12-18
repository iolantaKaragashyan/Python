class Musician:
    def __init__(self, name, age, experience_years, years_in_band):
        self.name = name
        self.age = age
        self.experience_years = experience_years
        self.years_in_band = years_in_band
    def get_info(self, role):
          return (f"Name: {self.name}, Role: {role}, Age: {self.age}, "
                f"Experience: {self.experience_years} years, "
                f"In Band: {self.years_in_band} years")
 
class Singer(Musician):
    def __init__(self, name, age, experience_years, years_in_band):
        super().__init__(name, age, experience_years, years_in_band)
 
class Guitarist(Musician):
    def __init__(self, name, age, experience_years, years_in_band):
        super().__init__(name, age, experience_years, years_in_band)
 
class Drummer(Musician):
    def __init__(self, name, age, experience_years, years_in_band):
        super().__init__(name, age, experience_years, years_in_band)
 
class Pianist(Musician):
    def __init__(self, name, age, experience_years, years_in_band):
        super().__init__(name, age, experience_years, years_in_band)
 
 
singer = Singer("John", 28, 10, 5)
guitarist = Guitarist("George", 30, 12, 7)
drummer = Drummer("Richard", 25, 8, 4)
pianist = Pianist("Tom", 35, 15, 10)
 
band_info = [
    singer.get_info("Singer"),
    guitarist.get_info("Guitarist"),
    drummer.get_info("Drummer"),
    pianist.get_info("Pianist"),
]
 
for info in band_info:
    print(info)