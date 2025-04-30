from flask import Flask, render_template
import requests
import redis
import os

app = Flask(__name__)
cache = redis.Redis(host=os.environ.get('REDIS_HOST', 'cache'), port=6379)
db_url = f"http://{os.environ.get('DB_HOST', 'db')}:5432/products" # Placeholder

@app.route('/')
def index():
    cached_products = cache.get('products')
    if cached_products:
        products = cached_products.decode('utf-8').split(',') # Simple example
    else:
        # In a real app, you'd fetch from the database
        products = ["Product A", "Product B", "Product C"]
        cache.set('products', ','.join(products))
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
