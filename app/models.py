
from app import db
from hashlib import md5
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    #posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)    


class Accion(db.Model):
    __tablename__='accion'
    id = db.Column(db.Integer, primary_key=True)
    nemo = db.Column(db.String(20), index=True, unique=True)
    empresa = db.Column(db.String(120), index=True, unique=True)
    def __repr__(self):
        return '<Accion %r>' % (self.nemo)


class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), index=True, unique=True)
    descripcion = db.Column(db.String(50))
    acciones = db.relationship('Categorias_Acciones', backref='seccion', lazy='dynamic')
    
    def __repr__(self):
        return '<Categoria %r>' % (self.nombre)
    

class Categorias_Acciones(db.Model):
    __tablename__ = 'categorias_acciones'
    id = db.Column(db.Integer, primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), primary_key=True)
    accion_id = db.Column(db.Integer, db.ForeignKey('accion.id'), primary_key=True)
    




