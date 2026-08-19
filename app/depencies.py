from fastapi import Depends, HTTPException, status
from app.auth import get_current_payload


class RoleChecker:

    def __init__(self, allowed_roles: list[str]) -> None:
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: dict = Depends(get_current_payload)) -> dict:

        user_role = current_user.get("role")

        if not user_role in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Quyền truy cập bị từ chối. Endpoint này yêu cầu các vai trò: {', '.join(self.allowed_roles)}"
            )

        return current_user
