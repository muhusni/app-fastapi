from fastapi import APIRouter
from api.controllers import get_favicon, get_root, get_test
from api.controllers import AuthController

router = APIRouter()
auth_controller = AuthController()

router.get("/favicon.ico", include_in_schema=False)(get_favicon)
router.get("/")(get_root)
router.get("/browser")(get_test)
router.get("/me")(auth_controller.get_me)

# Authentication
router.post("/login")(auth_controller.login)