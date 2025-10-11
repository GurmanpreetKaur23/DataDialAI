import pandas as pd
import sqlite3
import random

class ProductDataCollector:
    def __init__(self):
        self.products = []
    
    def generate_watch_data(self):
        # Watch categories with brands and products
        categories = {
            'Smartwatch': {
                'brands': ['Apple', 'Samsung', 'Noise', 'Boat', 'Fitbit', 'Garmin', 'Amazfit', 'Realme'],
                'products': ['Smart Watch', 'Fitness Tracker', 'Health Monitor', 'GPS Watch', 'Sport Watch', 'Luxe Edition', 'Pro Series', 'Classic Edition']
            },
            'Luxury': {
                'brands': ['Titan', 'Fastrack', 'Fossil', 'Casio', 'Timex', 'Tommy Hilfiger', 'Skmei', 'Daniel Wellington'],
                'products': ['Chronograph', 'Automatic', 'Quartz', 'Dress Watch', 'Minimalist', 'Classic', 'Premium', 'Executive']
            },
            'Sports': {
                'brands': ['Casio', 'Fastrack', 'Titan', 'Timex', 'G-Shock', 'Adidas', 'Nike', 'Puma'],
                'products': ['Sports Watch', 'Digital Watch', 'Fitness Tracker', 'Outdoor Watch', 'Swim Watch', 'Running Watch', 'Adventure', 'Extreme Series']
            },
            'Fashion': {
                'brands': ['Sonata', 'Maxima', 'Esprit', 'Swiss Military', 'HMT', 'Citizen', 'Seiko', 'Orient'],
                'products': ['Fashion Watch', 'Designer Watch', 'Trendy Edition', 'Style Series', 'Contemporary', 'Modern Classic', 'Chic Edition', 'Elegant Series']
            },
            'Digital': {
                'brands': ['Casio', 'Timex', 'Fastrack', 'Sonata', 'Maxima', 'Skmei', 'Pebble', 'Amazfit'],
                'products': ['Digital Watch', 'LED Display', 'Calculator Watch', 'Alarm Chrono', 'Multi-Function', 'Youth Series', 'Gaming Edition', 'Tech Watch']
            },
            'Analog': {
                'brands': ['Titan', 'HMT', 'Timex', 'Casio', 'Fastrack', 'Sonata', 'Maxima', 'Fossil'],
                'products': ['Analog Watch', 'Classic Dial', 'Vintage Series', 'Heritage Edition', 'Traditional', 'Minimalist', 'Roman Dial', 'Skeleton Watch']
            }
        }
        
        for i in range(350):  # Generate 350 products
            category = random.choice(list(categories.keys()))
            brand = random.choice(categories[category]['brands'])
            product_type = random.choice(categories[category]['products'])
            
            features = ['Premium', 'Classic', 'Sport', 'Elegant', 'Modern', 'Vintage', 'Professional', 'Luxury']
            colors = ['Black', 'Silver', 'Gold', 'Rose Gold', 'Blue', 'Brown', 'White', 'Green']
            materials = ['Leather Strap', 'Metal Bracelet', 'Silicone Band', 'Nylon Strap', 'Rubber Band', 'Steel Case', 'Ceramic Bezel', 'Mineral Glass']
            
            product_name = f"{brand} {random.choice(features)} {product_type} - {random.choice(colors)} {random.choice(materials)}"
            
            base_prices = {
                'Smartwatch': (1500, 45000),
                'Luxury': (2000, 35000),
                'Sports': (800, 15000),
                'Fashion': (1000, 12000),
                'Digital': (500, 8000),
                'Analog': (1200, 25000)
            }
            
            min_price, max_price = base_prices[category]
            price = random.randint(min_price, max_price)
            
            rating = round(random.uniform(3.8, 4.8), 1)
            reviews = random.randint(50, 10000)
            
            self.products.append({
                'product_id': i + 1,
                'product_name': product_name,
                'brand': brand,
                'category': category,
                'price': price,
                'rating': rating,
                'reviews': reviews
            })
    
    def save_data(self):
        df = pd.DataFrame(self.products)
        
        df.to_csv('products.csv', index=False)
 
        conn = sqlite3.connect('products.db')
        df.to_sql('products', conn, if_exists='replace', index=False)
        conn.close()
        
        print(" ~ Watch product data generated successfully!")
        print(f"~ Total products: {len(self.products)}")
        print(f"~ Categories: Smartwatch, Luxury, Sports, Fashion, Digital, Analog")
        print(f"~ Data saved to: products.csv & products.db")

def main():
    collector = ProductDataCollector()
    collector.generate_watch_data()
    collector.save_data()
    
    # sample data
    df = pd.read_csv('products.csv')
    print("\nSample of generated watch data:")
    print(df.head(10))

if __name__ == "__main__":
    main()