from sqlalchemy import text
from app.database import SessionLocal

db = SessionLocal()
print(db.execute(text("SELECT 1")).fetchone())
db.close()