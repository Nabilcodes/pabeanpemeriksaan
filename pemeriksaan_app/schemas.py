from pydantic import BaseModel, UUID4

class PIBCreate(BaseModel):
    importir_name: str
    importir_email: str
    value: int

class PIB(PIBCreate):
    id: UUID4
    status: str

    class Config:
        from_attributes = True
        arbitrary_types_allowed=True

class SuratCreate(BaseModel):
    pib_id: UUID4
    surat_type: str
    content: str

class Surat(SuratCreate):
    id: UUID4

    class Config:
        from_attributes = True
        arbitrary_types_allowed=True
