from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class PostModel(BaseModel):
    Id: int
    PostTypeId: int
    AcceptedAnswerId: Optional[int] = None
    ParentId: Optional[int] = None
    CreationDate: datetime
    DeletionDate: Optional[datetime] = None
    Score: int
    ViewCount: int
    Body: str
    OwnerUserId: int
    OwnerDisplayName: str
    LastEditorUserId: Optional[int] = None
    LastEditorDisplayName: str
    LastEditDate: Optional[datetime] = None
    LastActivityDate: datetime
    Title: str
    Tags: str
    AnswerCount: int
    CommentCount: int
    FavoriteCount: int
    ClosedDate: Optional[datetime] = None
    CommunityOwnedDate: Optional[datetime] = None
