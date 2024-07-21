from fastapi import APIRouter, Depends
from api.controllers import Controller
from api.controllers import AuthController
from api.controllers import UserController
from api.controllers import Ceisa40Controller
from api.schemas import UserResponse
from api.middleware import AuthBearer

router = APIRouter()
controller = Controller()
auth_controller = AuthController()
user_controller = UserController()
ceisa40_controller = Ceisa40Controller()

router.get("/favicon.ico", include_in_schema=False)(controller.get_favicon)
router.get("/")(controller.get_root)
router.get("/browser")(controller.get_test)
router.get("/me", dependencies=[Depends(AuthBearer())])(auth_controller.get_me)

# Authentication
router.post("/login")(auth_controller.login)

# User
router.post("/users")(user_controller.create_user)
router.get("/users/{user_id}", response_model=UserResponse)(user_controller.get_user)
router.get("/cek", dependencies=[Depends(AuthBearer())])(ceisa40_controller.get_data)