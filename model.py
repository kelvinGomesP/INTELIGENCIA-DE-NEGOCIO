# model.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import sessionmaker

db= create_engine('sqlite:///pizzaria.db')

Base = declarative_base()
Session = sessionmaker(bind=db)
Base = declarative_base()


class Cardapio(Base):
    __tablename__ = 'cardapio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    pizzas = relationship('Pizza', back_populates='cardapio')

class Pizza(Base):
    __tablename__ = 'pizza'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    ingredientes = Column(String, nullable=False)
    preco = Column(Integer, nullable=False)
    menu_id = Column(Integer, ForeignKey('cardapio.id'))
    cardapio = relationship('Cardapio', back_populates='pizzas')

class Mesa(Base):
    __tablename__ = 'mesa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero = Column(Integer, nullable=False)
    capacidade = Column(Integer, nullable=False)

# Configuração do banco de dados
DATABASE_URL = 'sqlite:///pizzaria.db'

def create_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Banco de dados criado com sucesso!")


def main() -> None:
    Base.metadata.create_all(db)
    cardapio = Cardapio(nome='Cardápio Principal', descricao='Descrição do cardápio principal')
    pizza = Pizza(nome='Pizza Margherita', ingredient = 'Tomate, Queijo, Manjericão', preco = 25, menu_id = cardapio.id)
    mesa = Mesa(numero=1, capacidade=4)

    with Session() as session:
        session.add(cardapio)
        session.add(pizza)
        session.add(mesa)
        session.commit()
        print(session.query(Cardapio).all())
        print(session.query(Pizza).all())
        print(session.query(Mesa).all())

# Cria o banco de dados
if __name__ == "__main__":
    create_database()
