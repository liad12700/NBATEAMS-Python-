import requests;

res = requests.get('https://www.balldontlie.io/api/v1/teams');
data= res.json()["data"];
usr=input("Which NBA team are you a fan of? ")

for x in range(len(data)):
    if usr==data[x]['abbreviation'] or usr==data[x]['city'] or usr==data[x]['full_name'] or usr==data[x]['name']:
        print("\n WOW! You are fan of the "+data[x]['full_name']+"\n There conference is "+data[x]['conference']+"\n There division is "+data[x]['division'] );
        print("\n Hope to see you in the finals!!! \n");
        usr="null";
        break;
if usr!="null":
    print("There is no NBA team with that name...")