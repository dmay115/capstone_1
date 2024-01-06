"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db, app
from models import Ingredients

with app.app_context():
    db.drop_all()
    db.create_all()

    with open("generator/ing.csv") as ingredients:
        db.session.bulk_insert_mappings(Ingredients, DictReader(ingredients))

    db.session.commit()
