# Simple Dictionary Example
# Professor Laney


# Create a dictionary of country codes and country names
countries = {
    "CA": "Canada",
    "US": "United States",
    "MX": "Mexico",
    "FR": "France",
    "JP": "Japan"
}

# Print the whole dictionary
print("Print the Countries dictionary in a not so friendly way (data dump):")
print(countries)

print()

# Access values using keys
print("Print the Countries using a given key")
print("CA =", countries["CA"])
print("US =", countries["US"])

print()
print("Let's add a new country to the dictionary and do another data dump:")
# Add a new country
countries["DE"] = "Germany"

print("Print the updated dictionary:")
print(countries)

print()

# Loop through the dictionary
print("Print the country list in a nicely formatted list:")

for code, country in countries.items():
    print(code, "-", country)
    

print()    
# Ask the user to add a new country
print("Let's make this more useful - why don't you add to our Country dictionary?") 
print("\nYou can use one of these - NO for Norway, IT for Italy, AU for Australia, BR for Brazil, CN for China")
new_code = input("Enter a new country code: ")
new_country = input("Enter the country name: ")

# Add the new country to the dictionary
countries[new_code] = new_country

print()
print("Updated countries:")

for code, country in countries.items():
    print(code, "-", country)
  
print()
print("And finally - why don't we SORT the countries alphabetically:")
print("\nCountries in alphabetical order by country code:")

# Sort the dictionary keys before looping
for code in sorted(countries):
    print(code, "-", countries[code])