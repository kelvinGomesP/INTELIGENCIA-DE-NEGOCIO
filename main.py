from controller import get_engine, create_tables, get_session
from crud import create_cardapio, create_pizza, create_mesa, get_cardapio, get_pizza, get_mesa

# Inicializar o banco de dados e criar tabelas
engine = get_engine()
create_tables(engine)

# Criar uma nova sessão
session = get_session(engine)

# Exemplo de criação de dados
novo_cardapio = create_cardapio(session, "Cardápio Principal", "Descrição do cardápio principal")
print(f"Cardápio criado: {novo_cardapio.id}, {novo_cardapio.nome}")

nova_pizza = create_pizza(session, "Pizza Margherita", "Tomate, Queijo, Manjericão", 25, novo_cardapio.id)
print(f"Pizza criada: {nova_pizza.id}, {nova_pizza.nome}")

nova_mesa = create_mesa(session, 1, 4)
print(f"Mesa criada: {nova_mesa.id}, Número: {nova_mesa.numero}")

# Exemplo de leitura de dados
cardapio = get_cardapio(session, novo_cardapio.id)
print(f"Cardápio obtido: {cardapio.id}, {cardapio.nome}")

pizza = get_pizza(session, nova_pizza.id)
print(f"Pizza obtida: {pizza.id}, {pizza.nome}")

mesa = get_mesa(session, nova_mesa.id)
print(f"Mesa obtida: {mesa.id}, Número: {mesa.numero}")
