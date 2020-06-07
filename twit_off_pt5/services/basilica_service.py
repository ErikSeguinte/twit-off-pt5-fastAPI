import basilica, os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('basilica_key')


with basilica.Connection(key) as c:
    embeddings = c.embed_sentences(["Hello world!", "How are you?"])
    breakpoint()
    print(list(embeddings))  # [[0.8556405305862427, ...], ...]
