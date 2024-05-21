from Get_Sub_Sites import get_sub_sites
from Get_Recept_Info import get_recept_info
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, BLOB, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipe',

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    ingredients = Column(String(1000))
    instrucrions = Column(String(1000))
    image_name = Column(String(100))
    time = Column(String(100))
    description = Column(String(1000))

if __name__ == '__main__':
    links = get_sub_sites()

    for link in links:
        print(link)
        title, img, description, ingredients, instructions, time = get_recept_info(link)
        engine = create_engine('sqlite:///database.db')
        Base.metadata.create_all(engine)


        engine = create_engine('sqlite:///database.db', echo=False)
        Session = sessionmaker(bind=engine)
        session = Session()

        engine = create_engine('sqlite:///database.db', echo=False)
        stmt = insert(Recipe).values(
            title = title,
            ingredients = str(ingredients),
            instrucrions = str(instructions),
            image_name = img,
            time = time,
            description = description
        )

        with engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()






