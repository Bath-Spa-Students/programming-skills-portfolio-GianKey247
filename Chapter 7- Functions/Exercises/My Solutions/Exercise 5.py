#Display 4 messages
#First 3 messages have the same country
#last message have different city and country

def describe_city(city,country="America"):
    print(f'This city which is known as,{city} is in {country}')
describe_city("Los Angeles")
describe_city("Boston")
describe_city("Detroit")
describe_city("Sydney", "Australia")