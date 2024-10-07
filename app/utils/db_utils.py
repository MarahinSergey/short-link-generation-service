from typing import Type
from fastapi import Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import and_, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import Base, get_db


class DbUtils:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_entity(
            self,
            entity: BaseModel | dict,
            table: Type[Base],
    ):
        """
        Create new entity from according pydantic schema

        Args:
            entity (BaseModel): pydantic object
            table (Type[Base]): entity table type

        Raises:
            HTTPException: unique constraints exception

        Returns:
            _type_: new entity
        """
        if type(entity) is not dict:
            entity = entity.dict()
        new = table(**entity)
        try:
            self.db.add(new)
            self.db.commit()
            self.db.refresh(new)
            return new
        except IntegrityError as ex:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=ex.args[0],
            )

    def get_entity_by(
            self,
            conditions: list,
            table: Type[Base],
    ):
        """Find single entity by filter conditions

        Args:
            conditions (list): list of filtering conditions
            table (Type[Base]): entity table type

        Raises:
            HTTPException: entity not found

        Returns:
            _type_: founded entity
        """
        entity = self.db.query(table).filter(and_(*conditions)).first()
        if entity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{table.__name__} not found",
            )
        return entity

    def delete_entities_by(
            self,
            conditions: list,
            table: Type[Base],
    ):
        """
        Delete entities founded by conditions

        Args:
            conditions (list): list of filtering conditions
            table (Type[Base]): entity table type
        """
        stmt = delete(table).where(and_(*conditions))
        self.db.execute(stmt)
        self.db.commit()
