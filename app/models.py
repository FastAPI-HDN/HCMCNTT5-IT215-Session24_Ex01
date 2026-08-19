from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class RoleModel(Base):

    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(
        String(255))

    # mối quan hệ 1-N với user
    users = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    # khóa ngoại liên kết tới Role
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("roles.id"), nullable=False)

    # mối quan hệ ngược với role
    role = relationship("RoleModel", back_populates="users")
