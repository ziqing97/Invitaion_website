from .import db

class Todict:
    def to_dict(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict  

class Invitation(db.Model):
    __tablename__ = 'invitations'
    invitation_id = db.Column(db.String(20), primary_key=True, nullable=False)
    guest_name = db.Column(db.String(20), nullable=False)
    invitation_time = db.Column(db.DateTime, nullable=False)
    guest_count = db.Column(db.Interger, nullable=False)
    contact_number = db.Column(db.Interger, nullable=False)
    main_lawyer_name = db.Column(db.String, nullable=False)
    assistant_name = db.Column(db.String, nullable=True)

class Worker(db.Model):
    __tablename__ = 'workers'
    worker_id = db.Column(db.Integer, primary_key=True, nullable=False)
    worker_name = db.Column(db.String(20), nullable=False)
