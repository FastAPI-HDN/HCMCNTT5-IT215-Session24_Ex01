from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta

SECRET_KEY = "devconnect_super_secret_jwt_key_2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


security = HTTPBearer()

# giải mã token và lấy payload tự động


def get_current_payload(creds: HTTPAuthorizationCredentials = Depends(security)) -> dict:

    token = creds.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except ExpiredSignatureError:
        # Bắt lỗi khi token quá hạn
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token đã hết hạn. Vui lòng đăng nhập lại!",
            headers={"WWW-Authenticate": "Bearer"},
        )

    except InvalidTokenError:
        # Bắt lỗi khi token giả mạo, sai secret key hoặc sai định dạng
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token không hợp lệ!",
            headers={"WWW-Authenticate": "Bearer"},
        )


def create_access_token(data: dict) -> str:

    to_encode = data.copy()

    expire_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire_time})

    token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return token


print(create_access_token(
    {"sub": "1",
     "email": "loc",
     "role": "STAFF"}
))


# token của STAFF: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJsb2MiLCJyb2xlIjoiU1RBRkYiLCJleHAiOjE3ODcwNDI5OTd9.EXkS-uFUee2ZGrtL_KBnon3nqA-cPviLE3XQy_SZFdc
