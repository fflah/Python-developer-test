from app import db

class BeritaModel(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), nullable=False)
    judul = db.Column(db.String(255), nullable=False)
    waktu_tayang = db.Column(db.BigInteger, nullable=False)
    konten = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<BeritaModel {}>'.format(self.judul)