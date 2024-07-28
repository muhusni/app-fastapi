from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = 'employees'  # Assuming the employees table name

    nip = Column(String, ForeignKey('auth_v2.NIP'), primary_key=True, index=True)
    kdEselon = Column(String, nullable=True)
    kdJenisJabatan = Column(String, nullable=True)
    kdJenisKelamin = Column(String, nullable=True)
    kdKantor = Column(String, nullable=True)
    kdPangkat = Column(String, nullable=True)
    kdStatusPegawai = Column(String, nullable=True)
    kdStatusPegawaiGroup = Column(String, nullable=True)
    kdUnitMaster = Column(String, nullable=True)
    kdUnitOrganisasi = Column(String, nullable=True)
    kdUnitOrganisasiInduk = Column(String, nullable=True)
    nipLama = Column(String, nullable=True)
    nmJenisJabatan = Column(String, nullable=True)
    nmJenisKelamin = Column(String, nullable=True)
    nmPegawai = Column(String, nullable=True)
    nmPegawaiSk = Column(String, nullable=True)
    nmStatusPegawai = Column(String, nullable=True)
    nmUnitOrganisasi = Column(String, nullable=True)
    uraianJabatan = Column(String, nullable=True)
    uraianPangkat = Column(String, nullable=True)
    urlFoto = Column(String, nullable=True)

    user = relationship("User", back_populates="employee")