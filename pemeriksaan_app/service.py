from sqlalchemy.orm import Session
from . import models, schemas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

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

    # Generate PDF
    pdf_buffer = generate_surat_pdf(new_surat)
    
    return new_surat, pdf_buffer

def generate_surat_pdf(surat: models.Surat):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    c.drawString(100, height - 100, f"Surat Type: {surat.surat_type}")
    c.drawString(100, height - 120, f"Content: {surat.content}")
    
    c.showPage()
    c.save()
    
    buffer.seek(0)
    return buffer