from pymongo import MongoClient
try:
    client = MongoClient("mongodb+srv://LucasOliveira:8GNEticXJDrGMBcR@cluster0.kwor4wz.mongodb.net/?retryWrites=true&w=majority")
    db = client.Backend
    print("Bd conectado")
except:
    print("A conexão com o bd falhou")

filmes_collection = db.Filmes
generos_collection = db.Generos

filmes_schema = {
    "Title": {"type": "string", "required": "true"},
    "Duration": {"type": "string", "required": "true"},
    "Link": {"type": "string", "required": "true"},
    "Genres": {"type": "array", "required": "true"}
}

generos_schema = {
    "Name": {"type": "string", "required": "true"}
}