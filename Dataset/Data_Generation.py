import random
import pandas as pd
from datetime import date
from calendar import monthrange
from datetime import date, timedelta
import string


categories = {
    101:"Fruits & Vegetables", 102:"Dairy & Eggs", 103:"Meat & Fish", 105:"Cereal & Bread",
    106:"Snacks & Sweets", 107:"Drinks", 108:"Household", 109:"Health & Beauty"
}

#supermarkets = ["Tesco", "Sainsbury's", "Asda", "Morrisons", "Waitrose", "Aldi", "Lidl", "M&S"]
supermarkets = {1: "Tesco", 2:"Sainsbury's", 3:"Asda", 4:"Morrisons",5:"Waitrose", 6:"Aldi", 7:"Lidl",8:"M&S"}
ratings = {1: 4.5, 2:4.7, 3:3.8, 4:4.2,5:3.9, 6:4.6, 7:4.3,8:4.8}

products = [
  "Apple", "Milk", "Eggs", "Bread","Chicken Breast",
  "Chocolate", "Cola", "Toothpaste", "Shampoo", "Toilet Paper", "Rice",
  "Pasta", "Coffee", "Tea", "Tomatoes", "Cucumber", "Yogurt", "Butter",
  "Biscuits", "Juice", "Water"
]
product_categories = {
    "Apple": 101,  # Fruits & Vegetables
    "Milk": 102,  # Dairy & Eggs
    "Eggs": 102,  # Dairy & Eggs
    "Bread": 105,  # Cereal & Bread
    "Chicken Breast": 103,  # Meat & Fish
    "Chocolate": 106,  # Snacks & Sweets
    "Cola": 107,  # Drinks
    "Toothpaste": 109,  # Health & Beauty
    "Shampoo": 109,  # Health & Beauty
    "Toilet Paper": 108,  # Household
    "Rice": 105,  # Cereal & Bread
    "Pasta": 105,  # Cereal & Bread
    "Coffee": 107,  # Drinks
    "Tea": 107,  # Drinks
    "Tomatoes": 101,  # Fruits & Vegetables
    "Cucumber": 101,  # Fruits & Vegetables
    "Yogurt": 102,  # Dairy & Eggs
    "Butter": 102,  # Dairy & Eggs
    "Biscuits": 106,  # Snacks & Sweets
    "Juice": 107,  # Drinks
    "Water": 107,  # Drinks
}

def generate_random_date_in_month(year, month):
  """Generates a random date within the specified month and year.

  Args:
      year: The year for the random date.
      month: The month (1-12) for the random date.

  Returns:
      A random date object within the specified month and year.
  """

  # Get the number of days in the specified month
  number_of_days = monthrange(year, month)[1]

  # Generate a random day between 1 and the number of days in the month
  random_day = random.randint(1, number_of_days)

  # Create the random date object
  return date(year, month, random_day)
year = 2024
month = 2  # February
data = []

for i in range(75):
    product_name = random.choice(products)
    #category_id = random.choice(list(categories.keys()))
    #category_name = categories[category_id]
    category_id = product_categories.get(product_name, random.choice(list(categories.keys())))
    category_name = categories[category_id]
    supermarket_id = random.choice(list(supermarkets.keys()))  
    supermarket_name = supermarkets[supermarket_id]  
    is_click_and_collect_available = supermarket_id in [1, 2, 4, 8, 7]
    price = round(random.uniform(0.5, 15), 2)
    unit = random.choice(["kg", "g", "L", "ml"])
    available = random.choice(["Yes", "No"])
    if available == "No":
       stock_level = 0
    else:
        stock_level = random.randint(10, 100)
    brand = random.choice(["Brand A", "Brand B", "Brand C", "Supermarket Own Brand"])  
    product_id = str(supermarket_name[0] + str(i + 10000))  
    image_url = f"https://example.com/products/{product_id}.jpg"   
    description = f"{product_name} from {random.choice(['local farms', 'Ecuador', 'Spain', 'Italy', 'California'])}"  
    dietary_restrictions = random.choices(["vegan", "gluten-free", "nut-free", "lactose-free"], k=random.randint(0,1))  
    nutritional_information = {
        "calories": random.randint(50, 500),
        "fat": random.uniform(0, 30),
        "protein": random.uniform(0, 20),
        "carbohydrates": random.uniform(0, 100)
    }  
    no_of_ingredients = random.randint(1, 5)
    country_of_origin = random.choice(["UK", "France", "Italy", "Spain", "Netherlands", "Germany", "USA", "China"])
    is_seasonal = random.choice([True, False])
    promotions = random.choices(["Buy one get one free", "20% off", "2 for £6"], k=random.randint(0, 1))  
    
    delivery_options = random.choices(["home delivery", "click & collect"], k=random.randint(1,2))
    delivery_lead_time = random.randint(1, 5)  
    minimum_order_quantity = random.randint(1, 5)
    rating = ratings[supermarket_id]
    number_of_reviews = random.randint(0, 1000)
    is_popular = random.choice([True, False])
    is_new = random.choice([True, False])
    customer_tags = random.choices(["fresh", "healthy", "affordable", "family-friendly", "organic", "seasonal"], k=random.randint(1,1))
    best_before_date = date.today() + timedelta(days=random.randint(5, 30))  
    disposal_instructions = "Please recycle the packaging."  
    awards_won = random.choices(["Great Taste Award", "Best Product of the Year"], k=random.randint(0, 1))
    allergens = random.choices(["nuts", "gluten", "soy", "dairy"], k=random.randint(1, 1))
    is_organic = random.choice([True, False])
    is_vegan = random.choice([True, False])
    standard_delivery = 3
    fast_delivery = 1
    # Generate a random date in March 2024
    order_date = generate_random_date_in_month(year, month)
    customer_id = random.randint(1, 10000)
    customer_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(10, 20)))
    customer_email = f"{customer_name.replace(' ', '').lower()}_{random.randint(1, 9999)}@example.com"
    customer_number = ''.join(random.choices(string.digits, k=10))
    street_number = random.randint(100, 999)
    street_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(5, 10)))
    street_type = random.choice(['St.', 'Ave.', 'Blvd.'])
    apt_number = random.randint(1, 100)
    city = random.choice(['City', 'Town'])
    zip_code = random.randint(10000, 99999)
    customer_address = f"{street_number} {street_name} {street_type} Apt #{apt_number}, {city} {zip_code}"
    order_id = str('O' + str(i + 11))


    data.append({
        "product_name": product_name,
        "category_id": category_id,
        "category_name": category_name,
        "supermarket_name": supermarket_name,
        "price": price,
        "unit": unit,
        "available": available,
        "brand": brand,
        "product_id": product_id,
        "supermarket_id": supermarket_id,
        "image_url": image_url,
        "description": description,
        "dietary_restrictions": dietary_restrictions,
        "nutritional_information": nutritional_information,
        "no_of_ingredients": no_of_ingredients,
        "country_of_origin": country_of_origin,
        "is_seasonal": is_seasonal,
        "promotions": promotions,
        "stock_level": stock_level,
        "delivery_options": delivery_options,
        "delivery_lead_time": delivery_lead_time,
        "minimum_order_quantity": minimum_order_quantity,
        "is_click_and_collect_available": is_click_and_collect_available,
        "Rating": rating,
        "number_of_reviews": number_of_reviews,
        "is_popular": is_popular,
        "is_new": is_new,
        "customer_tags": customer_tags,
        "best_before_date": best_before_date,
        "disposal_instructions": disposal_instructions,
        "awards_won": awards_won,
        "allergens": allergens,
        "is_organic": is_organic,
        "is_vegan": is_vegan,
        "standard_delivery": standard_delivery,
        "fast_delivery": fast_delivery,
        "order_date": order_date,
        "customer_id": customer_id,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "customer_number": customer_number,
        "customer_address": customer_address,
        "order_id" : order_id
    })

df = pd.DataFrame(data)
df.to_csv("grocery_random_data.csv", index=False)