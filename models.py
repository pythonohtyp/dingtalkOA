from api import db
import datetime


class Octopus_user(db.Model):
    __tablename__ = 'octopus_user'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(20))
    email = db.Column(db.String(64))
    pwd = db.Column(db.String(32))
    ldap_id = db.Column(db.String(32))
    name_cn = db.Column(db.String(32))
    name_en = db.Column(db.String(32))
    role_id = db.Column(db.Integer())
    outer_id = db.Column(db.String(64))
    state = db.Column(db.Integer())
    gmt_create = db.Column(db.Integer())
    gmt_update = db.Column(db.Integer())
    is_del = db.Column(db.Integer())

class Examine_approve(db.Model):
    __tablename__ = 'examine_approve'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    initiator = db.Column(db.String(50))
    applytype = db.Column(db.String(60))
    country = db.Column(db.String(50))
    profession = db.Column(db.String(50))
    createtime = db.Column(db.DateTime(), default=datetime.datetime.now)

def userAddChat(user_name,email,name_cn,outer_id):
    octopus = Octopus_user()
    octopus.user_name = user_name
    octopus.email = email
    octopus.name_cn = name_cn
    octopus.outer_id = outer_id
    db.session.add(octopus)
    db.session.commit()

def userLeaveOrg(userid):
    octopus = Octopus_user.query.filter(Octopus_user.outer_id == userid).first()
    octopus.is_del = 1
    db.session.commit()

def userQuitChat(userid):
    octopus = Octopus_user.query.filter(Octopus_user.outer_id == userid).first()
    octopus.is_del = 1
    db.session.commit()

def userNormal(userid):
    octopus = Octopus_user.query.filter(Octopus_user.outer_id == userid).first()
    octopus.is_del = 0
    db.session.commit()

def userExist(userid):
    octopus = Octopus_user.query.filter(Octopus_user.outer_id == userid).first()
    return octopus

def userDel(userid):
    octopus = Octopus_user.query.filter(Octopus_user.outer_id == userid, Octopus_user.is_del == 1).first()
    return octopus


def addWorkOrder(initiator, applytype, country, profession):
    approve = Examine_approve()
    approve.initiator = initiator
    approve.applytype = applytype
    approve.country = country
    approve.profession = profession
    db.session.commit()
