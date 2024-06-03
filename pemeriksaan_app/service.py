from sqlalchemy.orm import Session
from . import models, schemas

def verify_pib(db: Session, pib: schemas.PIBCreate):
    # Simulate verification logic
    if pib.value > 10000:
        surat_type = "Surat Pemberitahuan Jalur Kuning"
    else:
        surat_type = "Surat Persetujuan Pengeluaran Barang (SPPB)"

    new_pib = models.PIB(**pib.dict(), status=surat_type)
    db.add(new_pib)
    db.commit()
    db.refresh(new_pib)

    new_surat = models.Surat(
        pib_id=new_pib.id,
        surat_type=surat_type,
        content=f"Surat untuk PIB dengan nilai {pib.value}"
    )
    db.add(new_surat)
    db.commit()
    db.refresh(new_surat)

    return new_surat
