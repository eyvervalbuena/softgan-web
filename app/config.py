
DB_USER     = "invitado"
DB_PASSWORD = "Adso2977369"
DB_HOST     = "127.0.0.1"
DB_PORT     = 3306
DB_NAME     = "softgan_db"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
