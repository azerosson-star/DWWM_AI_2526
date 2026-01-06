# Modeèle de données pour les produits
from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    price = Column(Float)
    is_offer = Column(Boolean, default=False)