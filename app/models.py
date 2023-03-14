from . import db

class PropertyProfile(db.Model):
    __tablename__ = 'property_profile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    propertyTitle = db.Column(db.String(120), nullable=False)
    propertyDescription = db.Column(db.String(120), nullable=False)
    numofrooms=db.Column(db.Integer, nullable=False)
    numofbathrooms= db.Column(db.Integer, nullable=False)
    price=db.Column(db.String(120), nullable=False)
    propertytype=db.Column(db.String(120), nullable=False)
    location=db.Column(db.String(120), nullable=False)
    photo_path=db.Column(db.String(120), nullable=False)

    def _init_(self,id,propertyTitle,propertyDescription,numofrooms,numofbathrooms,price,propertytype,location,photo_path):
        self.id=id
        self.propertyTitle=propertyTitle
        self.propertyDescription=propertyDescription
        self.numofrooms=numofrooms
        self.numofbathrooms=numofbathrooms
        self.price=price
        self.propertytype=propertytype
        self.location=location
        self.photo_path=photo_path

def _repr_(self):
    return f"Property(id={self.id}, propertyTitle='{self.propertyTitle}', description='{self.description}', numofrooms={self.numofrooms}, numofbathrooms={self.numofbathrooms}, price={self.price}, location='{self.location}', photo_filename='{self.photo_filename}')"