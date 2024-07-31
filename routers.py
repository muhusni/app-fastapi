from fastapi import APIRouter, Depends
from api.controllers import Controller, AuthController, UserController, Ceisa40Controller, TiketController, InswController
from api.schemas import UserResponse
from api.middleware import AuthBearer
from api.schemas.tiket import TiketResponse, TiketIkcResponse

router = APIRouter()
controller = Controller()
auth_controller = AuthController()
user_controller = UserController()
ceisa40_controller = Ceisa40Controller()
tiket_controller = TiketController()
insw_controller = InswController() 

router.get("/favicon.ico", include_in_schema=False)(controller.get_favicon)
router.get("/")(controller.get_root)
router.get("/browser")(controller.get_test)
router.get("/me", dependencies=[Depends(AuthBearer())])(auth_controller.get_me)

# Authentication
router.post("/login")(auth_controller.login)
router.post("/logout", dependencies=[Depends(AuthBearer())])(auth_controller.logout)

# User
# router.post("/users")(user_controller.create_user)
router.get("/users/{user_id}", response_model=UserResponse)(user_controller.get_user)

# tiket duktek
router.get("/tickets/{ticket_id}", dependencies=[Depends(AuthBearer())], response_model=TiketResponse)(tiket_controller.get_ticket)
router.get("/tickets", dependencies=[Depends(AuthBearer())], response_model=TiketIkcResponse)(tiket_controller.get_ticket_by_ikc_ticket)

#ceisa 40
router.get("/ceisa40/dokumen/v1", dependencies=[Depends(AuthBearer())])(ceisa40_controller.get_dokumen_v1)
router.get("/ceisa40/dokumen", dependencies=[Depends(AuthBearer())])(ceisa40_controller.get_dokumen_by_params)
router.get("/ceisa40/dokumen/status/{id_header}", dependencies=[Depends(AuthBearer())])(ceisa40_controller.get_status_dokumen)
router.get("/ceisa40/dokumen/respon/{id_header}/{nomor_aju}", dependencies=[Depends(AuthBearer())])(ceisa40_controller.get_respon_dokumen)
router.get("/ceisa40/dokumen/{nomor_aju}", dependencies=[Depends(AuthBearer())])(ceisa40_controller.get_dokumen_by_aju)
router.get("/ceisa40/dokumen/respon-awal/{nomor_aju}/{id_respon_awal}")(ceisa40_controller.download_respon_awal_dokumen)
router.get("/ceisa40/dokumen/respon-pdf/{id_header}/{id_respon}")(ceisa40_controller.download_respon_dokumen)
router.get("/ceisa40/dokumen/draf/{kode_dokumen}/{id_header}")(ceisa40_controller.download_draf_dokumen)

# INSW
router.get("/insw/{dokumen}/{nomor_aju}", dependencies=[Depends(AuthBearer())])(insw_controller.get_dokumen_insw)
router.get("/insw/gen2", dependencies=[Depends(AuthBearer())])(insw_controller.get_token_insw_gen2)
router.post("/insw/gen2/dokumen", dependencies=[Depends(AuthBearer())])(insw_controller.get_dokumen_insw_gen2)

