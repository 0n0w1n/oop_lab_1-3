import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def Filtering(condition, dict_list):
    array = []
    for item in dict_list:
        if condition(item):
            array.append(item)
    return array

def aggregate(aggregate_key, aggregate_function, dict_list):
    array = []
    for item in dict_list:
        try:
            array.append(float(item[aggregate_key]))
        except ValueError:
            array.append(item[aggregate_key])
    return aggregate_function(array)

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

germany_cities = Filtering(lambda x: x["country"] == 'Germany', cities)
print('all cities in Germany')
for i in germany_cities:
    print(i["city"])
print()


# Print all cities in Spain with a temperature above 12°C

spain_cities = Filtering(lambda x: x["country"] == 'Spain' and float(x["temperature"]) > 12.0, cities)
print("all cities in Spain with a temperature above 12°C")
for i in spain_cities:
    print(i["city"])
print()


# Count the number of unique countries

print("the number of unique countries")
count = 0
for i in cities:
    country = []
    country.append(i["country"])
for i in country:
    if country.count(i) == 1:
        count += 1
print(count)
print()

# Print the average temperature for all the cities in Germany

temperature = []
for i in [x["city"] for x in germany_cities]:
    for j in cities:
        if j["city"] == i:
            temperature.append(float(j["temperature"]))
print("the average temperature for all the cities in Germany:")
print(sum(temperature)/len(temperature))
print()


# Print the max temperature for all the cities in Italy

temp_italy = []
for i in [x["city"] for x in Filtering(lambda x: x["country"] == 'Italy', cities)]:
    for j in cities:
        if j["city"] == i:
            temp_italy.append(float(j["temperature"]))
print("the max temperature for all the cities in Italy:")
print(max(temp_italy))

