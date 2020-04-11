import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

connection = psycopg2.connect(database="development", user="user", password="pass", host="localhost", port=5432)
cursor = connection.cursor()

query = """ INSERT INTO recruit(first_name,surname,rocketchat_user,github_name,id_number,personal_email_address,cohort_recruits)
VALUES
('Shaun','Themos','shaunT20','Shaun091T',3695214598753,'Shaun.t@example.com','c26 data_eng'),
('Grace','Hope','graceH22','grace092H',2581479653215,'Grace.H@example.com','c26 data_eng'),
('Sandra','Care','sandraC23','sandra093C',9685475131584,'Sandra.C@example.com','c26 data_eng'),
('Leo','Faith','leoF24','leo095F',9874512325698,'Leo.F@example.com','c26 data_eng'),
('Kevin','Kind','kevinK25','kevin096K',945213125678554,'Kevin.K@example.com','c26 data_eng')"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@127.0.0.1/development'
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    recruit = db.relationship('Recruit', backref='owner', lazy='dynamic')

class Recruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    personal_email_address = db.Column(db.VARCHAR(100), unique=True)
    rocketchat_user = db.Column(db.VARCHAR(50))
    github_name = db.Column(db.VARCHAR(50))
    id_number = db.Column(db.NUMERIC(15))
    cohort_recruits = db.Column(db.VARCHAR(100))


cursor.execute(query)
connection.commit()  
if __name__== '__main__':
    manager.run()
