from fastapi import FastAPI, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import List, Optional
from database import SessionLocal, engine
import query_helpers as herlpers
import schemas

# initialize FastAPI app
app = FastAPI(
    title="MovieLens API",
    description="Bienvenue dans l'API MovieLens. Cette API permet d'interagir avec une base de données inspirée du célèbre jeu de données MovieLens.",
    version="0.1"
)

# dépendances pour la session base de données

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# routepour l'api

@app.get(
    "/",
    summary = "vérifier le bon fonctionnement de l'API",
    description="Cette route permet de vérifier que l'API fonctionne correctement.",
    response_description="statut de l'API",
    operation_id="health_check_movies_api",
    tags=["monitoring"]
)

async def root():
    return {"message": "API MovieLens opérationnelle"}