from pydantic import BaseModel 
from enum import Enum
from api.dependancies import HttpClient
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from fastapi import HTTPException
import time
import os
from api.utils.browser import Browser

class Dokumen(str, Enum):
    pib = "pib"
    peb = "peb"
    
class PayloadInsw(BaseModel):
    nomor_aju: list[str]

class InswController():
    async def get_dokumen_insw(self, dokumen: Dokumen, nomor_aju: str, http: HttpClient):
        try: 
            URL = f'https://api.insw.go.id/api/cms/{dokumen.value}?no_pengajuan={nomor_aju}'
            response = await http.get(URL, auth=("insw_2", "bac2bas6"))
            return response.json()
        except:
            raise HTTPException(status_code=500, detail="error")
        
    async def get_dokumen_insw_gen2(self, payload: PayloadInsw, http: HttpClient):
        bearer_token = await self.get_token_insw_gen2(http) 
        if bearer_token:
            headers = {'Authorization': f'Bearer {bearer_token}'}
            responses = []
            for req in payload.nomor_aju:
                response = await http.get(f'https://api.insw.go.id/api/izin-final/get-dokumen-pabean?kppbc=050100&car={req}&nama_perusahaan=&tanggal_awal=&tanggal_akhir=&jns_dokumen=&status_dokumen=&page=1&limit=5', headers=headers)
                print(response.status_code)
                print(response.json()['data'])  # Assuming the response is in JSON format
                responses.extend(response.json()['data']['dokumen_pabean'])
            return responses
        else:
            print("Bearer token not found.")
     
    async def get_token_insw_gen2(self, http: HttpClient):
        # Check if token is already set and not expired
        bearer_token = os.getenv('BEARER_TOKEN')
        if bearer_token:
            headers = {'Authorization': f'Bearer {bearer_token}'}
            check_url = 'https://sso.insw.go.id/api/v1/auth/check'
            response = await http.client.get(check_url, headers=headers)
            if response.status_code == 200:
                print(response)
                return bearer_token  # Token is valid, return it

        # Token not set or expired, fetch a new one
        firefox_option = Options()
        firefox_option.add_argument("--headless")
        browser = Browser("firefox", opt=firefox_option)
        browser.open_page("https://tracking.insw.go.id/")
        overlay_xpath = "//div[contains(@style, 'position:fixed') and contains(@style, 'z-index:9999') and contains(@style, 'pointer-events:none')]"
        overlay = browser.wait_for_element(By.XPATH, overlay_xpath)
        browser.browser.execute_script("arguments[0].remove();", overlay)
        time.sleep(1)
        # Now you can interact with elements beneath the overlay
        element_beneath = browser.wait_for_element(By.XPATH, "//input[@autocomplete = 'username webauthn']")
        element_beneath.send_keys("199503022015021007")
        time.sleep(1)
        next_button = browser.browser.find_elements(By.XPATH, "//span[@class = 'absolute right-0 inset-y-0 flex items-center pr-3']")
        next_button[-1].click()
        time.sleep(1)

        username = browser.wait_for_element(By.ID, "password")
        username.send_keys("@Aa07087078.")

        sign_in = browser.browser.find_elements(By.XPATH, "//button[contains(text(), 'Sign in')]")
        time.sleep(1)
        sign_in[-1].click()

        browser.wait_for_element(By.XPATH, "//p[text() = 'Deskripsi Browse Pabean']")

        for req in browser.browser.requests:
            if req.response and 'Authorization' in req.headers and req.url == 'https://sso.insw.go.id/api/v1/auth/check':
                auth_header = req.headers['Authorization']
                if auth_header.startswith('Bearer '):
                    bearer_token = auth_header.split(' ')[1]
                    print(f"Bearer Token: {bearer_token}")
                    token = bearer_token
                    break

        # Once you have the new token, save it as an environment variable
        os.environ['BEARER_TOKEN'] = token  # Save the new token in an environment variable
        browser.close_browser()
        return token
            