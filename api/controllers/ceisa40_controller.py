from fastapi import HTTPException, Depends
from typing import Annotated
from api.dependancies import HttpClient
import os
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

    async def get_dokumen_v1(self, http: HttpClient):
        try:
            headers = self.get_header_ceisa40()
            URL = "https://apis-gw.customs.go.id/v2/browse-service/v1/browse/dokumen-pabean-inhouse?kodeKantor=050100"
            request = await http.get(URL, headers=headers)
            return request.json()
        except ReadError as exc:
            raise HTTPException(status_code=500, detail=exc)

    async def get_dokumen_by_aju(self, nomor_aju: str, http: HttpClient):
        params = DokumenCeisa40Params(**{"nomorAju": nomor_aju})
        return await self.get_dokumen(params, http)


    async def get_dokumen_by_params(self, params: Annotated[DokumenCeisa40Params, Depends()], http: HttpClient):
        return await self.get_dokumen(params, http)
    

    @staticmethod
    def get_header_ceisa40():
        api_key = os.getenv("BC_API_KEY")
        token = os.getenv("TOKEN_CEISA40")
        headers = {
            "beacukai-api-key": api_key,
            "Authorization": f"Bearer {token}"
        }
        return headers