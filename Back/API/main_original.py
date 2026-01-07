from fastapi import FastAPI
from pydantic import BaseModel

# 1. Créer une instance de l'application FastAPI
app = FastAPI()

# Schéma Pydantic pour la validation des données
class Product(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# 2. Définir une route
@app.get("/")
def read_root():
    return {"message": "Hello World!"}

# 3. Ajouter des paramètres de chemin et de requête
@app.get("/products/{product_id}")
def read_product(product_id: int, q: str = None):
    return {"product_id": product_id, "query": q}

# 4. Ajouter une route POST pour créer un nouvel élément
@app.post("/products/")
def create_product(product: Product):
    return {"message": f"Produit '{product.name}' créé, 'total': {product.price}."}