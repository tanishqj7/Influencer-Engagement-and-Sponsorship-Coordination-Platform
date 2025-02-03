from app import db
from flask_security import UserMixin, RoleMixin
from flask_security.models import fsqla_v3 as fsqla

fsqla.FsModels.set_db_info(db)

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, nullable = False, unique = True)
    # username = db.Column(db.String, nullable = False, unique= True)
    password = db.Column(db.String)
    active = db.Column(db.Boolean)
    fs_uniquifier = db.Column(db.String(65), unique = True, nullable = False)
    roles = db.relationship('Role', secondary='user_roles')
    # study_resource = db.relationship('StudyResource', backref = 'creator')

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)
    description = db.Column(db.String(255))

class Sponsor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(80), unique = True)
    industry = db.Column(db.String(80))

class Influencer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String, unique = True)
    category = db.Column(db.String)
    niche = db.Column(db.String)
    reach = db.Column(db.String)

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String, nullable=False)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date =db.Column(db.String)
    budget = db.Column(db.String)
    visibility = db.Column(db.String , default="private")
    active= db.Column(db.Boolean , default=True)

class Ad_Request(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    Campaign_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    Influencer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    message=db.Column(db.String)
    requirements = db.Column(db.String)
    amount = db.Column(db.String)
    status = db.Column(db.String , default="pending")
