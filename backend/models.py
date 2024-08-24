import datetime
# 從SQLAlchemy引入相應的參數，來設定models
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime, DECIMAL
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import relationship

# 從database.py引入剛剛設定好的Base，並用它來建立要存入資料庫的資料形態
from database import Base

# 建立class並繼承Base，設定存入的tablename，並設定PK，還有各個column存入的資料形態

class User(Base):
    __tablename__= 'Users'

    name = Column(String, primary_key=True)
    user_data = relationship("UserData", back_populates="user")

class UserData(Base):
    __tablename__= 'UsersData'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, ForeignKey('Users.name'))
    time = Column(DateTime, default=datetime.datetime.now)
    stash1 = Column(Integer)

    user = relationship("User", back_populates="user_data")

class Item(Base):
    __tablename__= 'Items'
    item_name = Column(Integer, primary_key=True)
    img = Column(BYTEA)
    price_sell = Column(DECIMAL(20,10))
    price_buy = Column(DECIMAL(20,10))

class Price_history(Base):
    __tablename__= 'Prics_histories'
    time = Column(DateTime, default=datetime.datetime.now, primary_key=True)
    price_sell = Column(DECIMAL(20,10))
    price_buy = Column(DECIMAL(20,10))