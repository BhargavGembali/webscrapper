import requests
from bs4 import BeautifulSoup
import csv # To store the data in a CSV file
import re



def extract_numbers(text):
  return re.findall(r'\d+\.\d+|\d+', text)

# URL of Swiggy's restaurant page
url = 'https://www.swiggy.com/city/pune/best-restaurants'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
try :
  response = requests.get(url, headers=headers)

# Send an HTTP GET request

  print(f"Status Code: {response.status_code}")

# open or create a csv file
  csv_file = open('restaurants.csv', 'w')
  writer = csv.writer(csv_file)
  writer.writerow(['Restaurant Name', 'Rating'])

# Check if the request was successful
  if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())

    restaurant_element = soup.find_all('div', class_='styled__StyledRestaurantGridCard-sc-fcg6mi-0 lgOeYp')

    if restaurant_element:
       
      for restaurant in restaurant_element:
        # Extract information from each <a> element and its child <div> elements
        restaurant_name = restaurant.find('div', class_='sc-beySbM lfjhyG').text.strip()
        text = restaurant.find('span', class_='sc-beySbM jdpFZn').text.strip()
        rating = extract_numbers(text)
        writer.writerow([restaurant_name, rating])
      print('Successful')
  else:
    print('Failed to retrieve the webpage.')

except requests.exceptions.HTTPError as err:
       print(f"HTTP Error Occured: {err}")
       print(err)

