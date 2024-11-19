from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://projeto_final_shift_user:ytxo9iPhN733ibMLmvZKZYWEpMgYrLEm@dpg-csuhf956l47c73ftktg0-a.oregon-postgres.render.com/projeto_final_shift"
 
engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


if __name__ == "__main__":
    try:
        db = SessionLocal()
        print("conexão feita")
    except Exception as e:
        print("Erro ao conectar com o banco de dados:", e)
    finally:
        db.close()
