from sqlmodel import SQLModel, Session, create_engine


database_file = 'planner.db'
database_connetion_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connetion_string, echo=True, connect_args=connect_args)

def conn():
	SQLModel.metadata.create_all(engine_url)

def get_session():
	with Session(engine_url) as session:
		yield session