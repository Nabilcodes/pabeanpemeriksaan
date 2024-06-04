from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base

class PIB(Base):
    __tablename__ = "pibs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    importir_name = Column(String, index=True)
    importir_email = Column(String, index=True)
    value = Column(Integer, index=True)
    status = Column(String, index=True)

class Surat(Base):
    __tablename__ = "surats"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pib_id = Column(UUID(as_uuid=True))
    surat_type = Column(String, index=True)
    content = Column(String)