from fastapi import FastAPI, status, Depends
from app.auth import get_current_payload
from app.models import *
from app.database import Base, Engine
from app.depencies import RoleChecker

# CORS
from fastapi.middleware.cors import CORSMiddleware

#  mật khẩu hash của 123: $2b$12$qQAzfFH90Dpp7bB21N9oke64XhD7StXfp.zwyxNglfOlh0wxWR94G

app = FastAPI()

origins = [
    "https://internal.megamart.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 🎯 Danh sách địa chỉ được phép
    allow_credentials=True,  # 🔑 Cho phép gửi cookie/token
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "X-User-Role"]  # 🏷️ Cho phép các Header
)

Base.metadata.create_all(Engine)

allow_all = RoleChecker(["HR", "ADMIN", "STAFF"])
allow_admin_only = RoleChecker(["ADMIN"])
allow_admin_staff = RoleChecker(["HR", "ADMIN"])


@app.get("/api/profile", status_code=status.HTTP_200_OK, dependencies=[Depends(allow_all)])
def get_profile(current_user: dict = Depends(get_current_payload)):

    return {
        "message": "Xem dữ liệu thành công",
        "data": current_user
    }


@app.get("/api/v1/system/settings", status_code=status.HTTP_200_OK, dependencies=[Depends(allow_admin_only)])
def get_settings(current_user: dict = Depends(get_current_payload)):

    return {
        "message": "Xem dữ liệu thành công",
        "data": current_user
    }


@app.get("/api/v1/salary/modify", status_code=status.HTTP_200_OK, dependencies=[Depends(allow_all)])
def get_modify(current_user: dict = Depends(get_current_payload)):

    return {
        "message": "Xem dữ liệu thành công",
        "data": current_user
    }
