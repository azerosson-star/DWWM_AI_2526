from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from product_model import ProductModel
from pydantic import BaseModel

# Créer les tables dans la base de données au démarrage
Base.metadata.create_all(bind=engine)

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

# 3. liste des produits
@app.get("/products/")
def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    return products

# 4. Ajouter une route POST pour créer un nouvel élément
@app.post("/products/")
def create_product(product: Product, db: Session = Depends(get_db)):
    # Créer une nouvelle instance de ProductModel
    new_product = ProductModel(name=product.name, price=product.price, is_offer=product.is_offer)

    # Ajouter et sauvegarder dans la base de données
    db.add(new_product)
    db.commit()
    db.refresh(new_product) # Rafraîchir pour obtenir l'ID généré
    return {"message": f"Produit '{new_product.name}' créé avec succès."}