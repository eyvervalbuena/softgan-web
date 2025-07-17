from app.modelo.finca import Finca   
from app.config import SessionLocal

class FincaDao:
    def insert(self, finca: Finca) -> int:
        with SessionLocal() as session:
            session.add(finca)
            session.commit()
            session.refresh(finca)
            return finca.id_finca   # 

    def list_all(self) -> list[Finca]:
        with SessionLocal() as session:
            return session.query(Finca).all()

    def get_by_id(self, finca_id: int) -> Finca | None:
        with SessionLocal() as session:
            return session.get(Finca, finca_id)

    def update(self, finca: Finca) -> None:
        with SessionLocal() as session:
            session.merge(finca)
            session.commit()

    def delete(self, finca_id: int) -> bool:
        with SessionLocal() as session:
            obj = session.get(Finca, finca_id)
            if obj:
                session.delete(obj)
                session.commit()
                return True
            return False
