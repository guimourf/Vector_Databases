import json
import torch
import pandas as pd

from tqdm import tqdm
from transformers import AutoTokenizer
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from elasticsearch_core import gerar_embedding, gerar_indice, indexar_documentos, atualizar_rel_jur, buscar_documentos


root_dir = "../"

# ------------------------------------------------------------------------------- #
# Inicializações
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Executando em {device}...")

# elasticsearch
es = Elasticsearch(
    ['https://localhost:9200'],
    basic_auth=('elastic', '19112023'),
    verify_certs=False
)
print("Conexão com o Elasticsearch estabelecida!")

index_name = 'acordaos_indice'

gerar_indice(es, index_name)

# dados
df = pd.read_csv('../data/acordaos_reduzidos.csv')
df_relacoes = pd.read_csv('../data/tabela_relacoes_juridicas.csv')

# modelo legalbert
tokenizer = AutoTokenizer.from_pretrained("raquelsilveira/legalbertpt_fp")
model = SentenceTransformer("raquelsilveira/legalbertpt_fp")

# ------------------------------------------------------------------------------- #
# Selecionar amostras aleatórias
amostras_aleatorias = df.sample(n=20, random_state=42)

# Função para encontrar relação jurídica
def encontrar_relacao_juridica(embedding_conteudo):
    relacoes_encontradas = {1: None, 2: None, 3: None}

    for nivel in range(1, 4):
        nivel_relacoes = df_relacoes[df_relacoes['Nível'] == nivel]
        for _, row in nivel_relacoes.iterrows():
            relacao = row['Relação']
            if pd.notna(row['Verdade de base']):
                embedding_relacao = gerar_embedding(row['Verdade de base'])
                similarity = cosine_similarity(embedding_conteudo.reshape(1, -1), embedding_relacao.reshape(1, -1))
                if relacoes_encontradas[nivel] is None or similarity[0][0] > relacoes_encontradas[nivel][1]:
                    relacoes_encontradas[nivel] = (relacao, similarity[0][0])

    relacao_niveis = ':'.join([r[0] for r in relacoes_encontradas.values() if r is not None])
    return relacao_niveis if relacao_niveis else "Relação jurídica desconhecida"
# ------------------------------------------------------------------------------- #
# Função para indexar as amostras
def indexar_documentos(es, df, index_name):
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Indexando amostras"):

        # Verifica se o documento já está indexado
        query = {"query": {"term": {"id_documento": row['id_documento']}}}
        res = es.search(index=index_name, body=query)

        if res['hits']['total']['value'] > 0:
            continue  # Pula se o documento já existir

        # Definir documento para indexação
        doc = {
            "id_documento": row['id_documento'],
            "conteudo": row['conteudo'],
            "relacao_juridica": row['relacao_juridica'],
            "num_processo": row['num_processo'],
            "classe": row['classe'],
            "embedding": row['embedding'].tolist()
        }

        es.index(index=index_name, document=doc)
# ------------------------------------------------------------------------------- #
# Adicionando o embedding e relação jurídica
amostras_aleatorias['embedding'] = amostras_aleatorias['conteudo'].apply(lambda x: gerar_embedding(x))
amostras_aleatorias['relacao_juridica'] = amostras_aleatorias['embedding'].apply(encontrar_relacao_juridica)

# Executa a indexação para as amostras aleatórias
indexar_documentos(es, amostras_aleatorias, index_name)

# Salva as amostras com relação jurídica em um CSV
amostras_aleatorias.to_csv('amostras_aleatorias_com_relacao_juridica.csv', index=False)
print(amostras_aleatorias)
print("Amostras indexadas e salvas com sucesso!")
# ------------------------------------------------------------------------------- #