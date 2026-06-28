from sqlalchemy.orm import Session

from app.models.server import Server
from app.schemas.server import ServerCreate


def create_server(db: Session, server_data: ServerCreate):

    server = Server(
        name=server_data.name,
        host=server_data.host,
        port=server_data.port,
        username=server_data.username,
        password=server_data.password,
    )

    db.add(server)
    db.commit()
    db.refresh(server)

    return server


def get_servers(db: Session):
    return db.query(Server).all()
