from pydantic import BaseModel, field_validator
from typing import Optional, Annotated
from datetime import date, datetime

class DokumenCeisa40Params(BaseModel):
    kodeKantor: Optional[str] = "050100"
    kodeJalur: Optional[str] = ""
    namaPerusahaan: Optional[str] = ""
    nomorAju: Optional[str] = ""
    kodeProses: Optional[str] = ""
    kodeDokumen: Optional[str] = ""
    nomorDaftar: Optional[str] = ""
    tanggalDokumenEnd: Optional[str] = ""
    tanggalDokumenStart: Optional[str] = ""
    size: int = 40
    page: int = 0
