from sqlmodel import create_engine

from ayomi.config import settings

engine = create_engine(settings.DATABASE_URI)
