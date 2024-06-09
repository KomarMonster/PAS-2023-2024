import requests

field1 = input("Customer name: ")
field2 = input("Telephone: ")
field3 = input("E-mail address: ")
field4 = input("Pizza Size (small/medium/large): ")
field5 = input("Pizza Toppings (bacon, cheese, onion, mushroom): ")
field6 = input("Preferred delivery time (min: 11:00, max: 21:00): ")
field7 = input("Delivery instructions: ")

data = {
    'custname': field1,
    'custtel': field2,
    'custemail': field3,
    'size': field4,
    'topping': field5,
    'delivery': field6,
    'comments': field7
}

response = requests.post("http://httpbin.org/post", data=data)

print("Status:", response.status_code)
print("Odpowiedź od serwera:")
print(response.json())
