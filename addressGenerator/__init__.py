import random

def getRandomValue(addr):

    n = random.randint(0, len(addr))
    print(addr[n-1])

def getRandomNumber(title, num):

    print(title  + str(random.randint(10000 , 99950)))

countries = ["Brazil", "Canada", "Germany", "India", "Japan", "North and South Korea", "Mexico", "Spain", "UK", "USA"]

usaStates = ["AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", "HI", "IA", "ID", "IL", "IN",
             "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MP", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM",
             "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UM", "UT", "VA", "VI", "VT", "WA",
             "WI", "WV", "WY"]
usaCities = ["New York", "Los Angelos", "Chicago", "Houston", "Phoenix", "San Antonio", "Philadelphia", "San Diego",
             "Dallas", "Austin", "San Jose", "Fort Worth", "Jacksonville", "Charlotte", "Columbus", "Indianapolis",
             "San Francisco", "Seattle", "Denver", "Washington", "Boston", "El Paso", "Nashville", "Oklahoma City",
             "Las Vegas", "Portland", "Detroit", "Memphis"]




for x in range(200):
    getRandomNumber("",200)