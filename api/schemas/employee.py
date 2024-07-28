from pydantic import BaseModel
from typing import Optional, Annotated
from api.models.employee import Employee as EmployeeModel

class Employee(BaseModel):
    nip: str
    kdEselon: Optional[str] = None
    kdJenisJabatan: Optional[str] = None
    kdJenisKelamin: Optional[str] = None
    kdKantor: Optional[str] = None
    kdPangkat: Optional[str] = None
    kdStatusPegawai: Optional[str] = None
    kdStatusPegawaiGroup: Optional[str] = None
    kdUnitMaster: Optional[str] = None
    kdUnitOrganisasi: Optional[str] = None
    kdUnitOrganisasiInduk: Optional[str] = None
    nipLama: Optional[str] = None
    nmJenisJabatan: Optional[str] = None
    nmJenisKelamin: Optional[str] = None
    nmPegawai: Optional[str] = None
    nmPegawaiSk: Optional[str] = None
    nmStatusPegawai: Optional[str] = None
    nmUnitOrganisasi: Optional[str] = None
    uraianJabatan: Optional[str] = None
    uraianPangkat: Optional[str] = None
    urlFoto: Optional[str] = None
    

class EmployeeResponse(Employee):
    class Config:
        from_attributes = True