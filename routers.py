from fastapi import APIRouter, Depends
from api.controllers import Controller, AuthController, UserController, Ceisa40Controller, TiketController
from api.schemas import UserResponse
from api.middleware import AuthBearer
from api.schemas.tiket import TiketResponse

router = APIRouter()
controller = Controller()
auth_controller = AuthController()
user_controller = UserController()
ceisa40_controller = Ceisa40Controller()
tiket_controller = TiketController()

router.get("/favicon.ico", include_in_schema=False)(controller.get_favicon)
router.get("/")(controller.get_root)
router.get("/browser")(controller.get_test)
router.get("/me", dependencies=[Depends(AuthBearer())])(auth_controller.get_me)

# Authentication
router.post("/login")(auth_controller.login)
router.post("/logout", dependencies=[Depends(AuthBearer())])(auth_controller.logout)

# User
router.post("/users")(user_controller.create_user)
router.get("/users/{user_id}", response_model=UserResponse)(user_controller.get_user)

# tiket duktek
router.get("/tickets/{ticket_id}", dependencies=[Depends(AuthBearer())], response_model=TiketResponse)(tiket_controller.read_ticket)

#ceisa 40
router.get("/ceisa40/dokumen", dependencies=[Depends(AuthBearer())])(ceisa40_controller.get_dokumen)