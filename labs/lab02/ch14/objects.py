# Starting file for Lab 2 - objects.py program
# Irwin Li, DEV128, 10/18/2026

class Movie:
    # Constructor initializes the movie's attributes (Name, year)
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # Returns a string of the movie's name and release year
    def getStr(self):
        return f"{self.name} ({self.year})"