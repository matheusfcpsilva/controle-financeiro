from datetime import datetime, timezone

from app import db



class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha_hash = db.Column(db.String(255), nullable=False)
    criado_em = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
