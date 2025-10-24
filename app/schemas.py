from pydantic import BaseModel
from typing import Optional

class GuildBase(BaseModel):
    name: str
    rating: Optional[int] = 0

class GuildCreate(GuildBase):
    pass

class Guild(GuildBase):
    guild_id: int
    class Config:
        orm_mode = True

class PlayerBase(BaseModel):
    login: str
    nickname: Optional[str] = None
    email: Optional[str] = None
    level: Optional[int] = 1
    xp: Optional[int] = 0
    guild_id: Optional[int] = None

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    player_id: int
    class Config:
        orm_mode = True

class QuestBase(BaseModel):
    title: str
    description: Optional[str] = None
    reward: Optional[str] = None
    difficulty: Optional[str] = None

class QuestCreate(QuestBase):
    pass

class Quest(QuestBase):
    quest_id: int
    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    name: str
    item_type: Optional[str] = None
    rarity: Optional[str] = None
    price: Optional[int] = 0

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    item_id: int
    class Config:
        orm_mode = True

class SkillBase(BaseModel):
    name: str
    level: Optional[int] = 1
    effect: Optional[str] = None

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    skill_id: int
    class Config:
        orm_mode = True

class AchievementBase(BaseModel):
    name: str
    description: Optional[str] = None
    condition_text: Optional[str] = None

class AchievementCreate(AchievementBase):
    pass

class Achievement(AchievementBase):
    achievement_id: int
    class Config:
        orm_mode = True

class MathGameBase(BaseModel):
    match_date: Optional[str] = None
    match_type: Optional[str] = None
    result: Optional[str] = None

class MathGameCreate(MathGameBase):
    pass

class MathGame(MathGameBase):
    match_id: int
    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    item_id: int
    quantity: Optional[int] = 1

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    class Config:
        orm_mode = True

class PlayerQuestBase(BaseModel):
    player_id: int
    quest_id: int

class PlayerQuestCreate(PlayerQuestBase):
    pass

class PlayerQuest(PlayerQuestBase):
    class Config:
        orm_mode = True

class PlayerSkillBase(BaseModel):
    player_id: int
    skill_id: int

class PlayerSkillCreate(PlayerSkillBase):
    pass

class PlayerSkill(PlayerSkillBase):
    class Config:
        orm_mode = True

class PlayerAchievementBase(BaseModel):
    player_id: int
    achievement_id: int

class PlayerAchievementCreate(PlayerAchievementBase):
    pass

class PlayerAchievement(PlayerAchievementBase):
    class Config:
        orm_mode = True

class PlayerMathGameBase(BaseModel):
    player_id: int
    match_id: int

class PlayerMathGameCreate(PlayerMathGameBase):
    pass

class PlayerMathGame(PlayerMathGameBase):
    class Config:
        orm_mode = True
