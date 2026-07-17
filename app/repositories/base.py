from typing import TypeVar, Generic
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.exceptions import RepositoryIntegrityException

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")


class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get(self, id: int) -> ModelType | None:
        stmt = select(self.model).where(self.model.id == id)
        return self.db.execute(stmt).scalar_one_or_none()

    def create(self, data: CreateSchemaType) -> ModelType:
        obj = self.model(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def list(self) -> list[ModelType]:
        stmt = select(self.model)
        return self.db.execute(stmt).scalars().all()

    def update(self, id: int, data: UpdateSchemaType) -> ModelType | None:
        obj = self.get(id)
        if obj is None:
            return None
        for key, value in data.model_dump(exclude_none=True).items():
            setattr(obj, key, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, id: int) -> None:
        obj = self.get(id)
        if obj is None:
            return

        try:
            self.db.delete(obj)
            self.db.commit()
        except IntegrityError as e:
            self.db.rollback()
            raise RepositoryIntegrityException() from e
        
