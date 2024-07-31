from fastapi import HTTPException, Depends
from fastapi.responses import StreamingResponse, FileResponse
from typing import Annotated
from api.dependancies import HttpClient
import os
import tempfile
import time
import uuid
from fastapi.background import BackgroundTasks
from dotenv import load_dotenv
from api.schemas import DokumenCeisa40Params
from urllib.parse import urlencode
from httpx import ReadError
load_dotenv()

class Ceisa40Controller:

    async def get_dokumen(self, params: DokumenCeisa40Params, http: HttpClient):
        try:
            headers = self.get_header_ceisa40()
            URL = f"https://apis-gw.customs.go.id/v2/browse-service/v1/browse/dokumen-pabean-inhouse-new?{urlencode(params.model_dump())}"
            request = await http.get(URL, headers=headers)
            return request.json()
        except ReadError as exc:
            raise HTTPException(status_code=500, detail=exc)
        finally:
            await http.close()

    async def get_dokumen_v1(self, http: HttpClient):
        try:
            headers = self.get_header_ceisa40()
            URL = "https://apis-gw.customs.go.id/v2/browse-service/v1/browse/dokumen-pabean-inhouse?kodeKantor=050100"
            request = await http.get(URL, headers=headers)
            return request.json()
        except ReadError as exc:
            raise HTTPException(status_code=500, detail=exc)
        finally:
            await http.close()
            
    async def get_dokumen_by_aju(self, nomor_aju: str, http: HttpClient):
        params = DokumenCeisa40Params(**{"nomorAju": nomor_aju})
        return await self.get_dokumen(params, http)


    async def get_dokumen_by_params(self, params: Annotated[DokumenCeisa40Params, Depends()], http: HttpClient):
        return await self.get_dokumen(params, http)
    

    async def get_status_dokumen(self, id_header: str, http: HttpClient):
        try:
            headers = self.get_header_ceisa40()
            URL = f"https://apis-gw.customs.go.id/v2/parser/v1/proses/getRiwayatStatus/{id_header}"
            response = await http.get(URL, headers=headers)
            return response.json()
        except ReadError as exc:
            raise HTTPException(status_code=500, detail=exc)
        finally:
            await http.close()        
        
    async def get_respon_dokumen(self, id_header: str, nomor_aju: str, http: HttpClient):
        try:
            headers = self.get_header_ceisa40()
            URL = f"https://apis-gw.customs.go.id/v2/parser/v1/Respon/getRespon/{id_header}/{nomor_aju}"
            response = await http.get(URL, headers=headers)
            return response.json()
        except ReadError as exc:
            raise HTTPException(status_code=500, detail=exc)
        finally:
            await http.close()
            
    async def download_respon_awal_dokumen(self,nomor_aju: str, id_respon_awal: str, background_tasks: BackgroundTasks, http: HttpClient):
        try:
            headers = self.get_header_ceisa40()
            unique_filename = f"{uuid.uuid4().hex}.pdf"
            path = f"storage/{unique_filename}"
            url = f'https://apis-gw.customs.go.id/v2/report-service/respon/awal/{nomor_aju}/{id_respon_awal}'
            # url = 'https://apis-gw.customs.go.id/v2/report-service/formulir/20/dc6f574a-97f5-4f66-a100-626f39ad69cc'
            # response = await http.download_file(url)
            # temp_file = tempfile.NamedTemporaryFile(delete=False)
            async with http.client.stream("GET", url, auth=None, headers=headers, timeout=None) as response:
                response.raise_for_status()
                with open(path, 'wb') as f:
                    async for chunk in response.aiter_bytes():
                        f.write(chunk)
                background_tasks.add_task(os.remove, path)
                return FileResponse(path, media_type="application/pdf")

        except ReadError as exc:
            raise HTTPException(status_code=500, detail=exc)
        finally:
            await http.close()
            
    async def download_respon_dokumen(self,id_header: str, id_respon: str, background_tasks: BackgroundTasks, http: HttpClient):
        try:
            headers = self.get_header_ceisa40()
            unique_filename = f"{uuid.uuid4().hex}.pdf"
            path = f"storage/{unique_filename}"
            url = f'https://apis-gw.customs.go.id/v2/report-service/respon/{id_header}/{id_respon}'
            # url = 'https://apis-gw.customs.go.id/v2/report-service/formulir/20/dc6f574a-97f5-4f66-a100-626f39ad69cc'
            # response = await http.download_file(url)
            # temp_file = tempfile.NamedTemporaryFile(delete=False)
            async with http.client.stream("GET", url, auth=None, headers=headers, timeout=None) as response:
                response.raise_for_status()
                with open(path, 'wb') as f:
                    async for chunk in response.aiter_bytes():
                        f.write(chunk)
                background_tasks.add_task(os.remove, path)
                return FileResponse(path, media_type="application/pdf")

        except ReadError as exc:
            raise HTTPException(status_code=500, detail=exc)
        finally:
            await http.close()      
            
    async def download_draf_dokumen(self, kode_dokumen: str, id_header: str, background_tasks: BackgroundTasks, http: HttpClient):
        try:
            headers = self.get_header_ceisa40()
            unique_filename = f"{uuid.uuid4().hex}.pdf"
            path = f"storage/{unique_filename}"
            url = f'https://apis-gw.customs.go.id/v2/report-service/formulir/{kode_dokumen}/{id_header}'
    
            async with http.client.stream("GET", url, auth=None, headers=headers, timeout=None) as response:
                response.raise_for_status()
                with open(path, 'wb') as f:
                    async for chunk in response.aiter_bytes():
                        f.write(chunk)
                background_tasks.add_task(os.remove, path)
                return FileResponse(path, media_type="application/pdf")

        except ReadError as exc:
            raise HTTPException(status_code=500, detail=exc)
        finally:
            await http.close()        
            
            
    @staticmethod
    def get_header_ceisa40() -> dict:
        api_key = os.getenv("BC_API_KEY")
        token = os.getenv("TOKEN_CEISA40")
        headers = {
            "beacukai-api-key": api_key,
            "Beacukai-Api-Key": api_key,
            "Authorization": f"Bearer {token}"
        }
        return headers