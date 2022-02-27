from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/sci_db', encoding='utf8', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()