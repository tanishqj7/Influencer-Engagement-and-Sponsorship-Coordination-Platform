from flask_security import SQLAlchemySessionUserDatastore
from app import db
from flask_security.utils import hash_password
# from models import aaa


def create_data(user_datastore : SQLAlchemySessionUserDatastore):
    print("creating roles and users") # for debug purposes

    # creating roles

    user_datastore.find_or_create_role(name='admin', description = "Administrator")
    user_datastore.find_or_create_role(name='sponsor', description = "Sponsor wants to advertise their product or services")
    user_datastore.find_or_create_role(name='influencer', description = "Influencer advertise products on their social media account")

    # creating initial data

    if not user_datastore.find_user(email = "admin@iitm.ac.in"):
        user_datastore.create_user(email = "admin@iitm.ac.in", password = hash_password("pass"), roles=['admin'])
    if not user_datastore.find_user(email = "spon@iitm.ac.in"):
        user_datastore.create_user(email = "spon@iitm.ac.in", password = hash_password("pass"), roles=['sponsor'])
    if not user_datastore.find_user(email = "influ@iitm.ac.in"):
        user_datastore.create_user(email = "influ@iitm.ac.in", password = hash_password("pass"), roles=['influencer'])

    # create dummy study resource

    db.session.commit()
