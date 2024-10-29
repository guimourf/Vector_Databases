import urllib3
from elasticsearch import Elasticsearch
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForMaskedLM, AutoModel
from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm



# Inicializando o modelo BERT e o tokenizer


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Inicializando o modelo BERT e o tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained("raquelsilveira/legalbertpt_fp")
model = SentenceTransformer("raquelsilveira/legalbertpt_fp")

# Função para gerar embeddings
def gerar_embedding(texto):
    return model.encode(texto)



# Configuração do índice para Elasticsearch (dense vector com 768 dimensões)
def gerar_indice(es, indice):
    if not es.indices.exists(index=indice):
        print("Índice não encontrado.")
        print("Criand um novo índice!")
        es.indices.create(
            index=indice,
            body={
                "mappings": {
                    "properties": {
                        "id_documento": {"type": "keyword"},
                        "num_processo": {"type": "keyword"},
                        "classe": {"type": "text"},
                        "conteudo": {"type": "text"},
                        "embedding": {
                            "type": "dense_vector",
                            "dims": 768
                        },
                        "rel_jur": {"type": "text"}
                    }
                }
            }
        )



def indexar_documentos(es, df, index_name):
    for _, row in tqdm(df.iterrows(), total=len(df), desc="Indexando documentos"):
        
        # Verifica se o documento já está indexado pelo id_documento
        query = {
            "query": {
                "term": {
                    "id_documento": row['id_documento']
                }
            }
        }
        res = es.search(index=index_name, body=query)
        
        # Se o documento já existir, pula para o próximo
        if res['hits']['total']['value'] > 0:
            continue

        # Gera o embedding e cria o documento
        embedding = gerar_embedding(row['conteudo']).tolist()
        doc = {
            "id_documento": row['id_documento'],
            "num_processo": row['num_processo'],
            "classe": row['classe'],
            "conteudo": row['conteudo'],
            "embedding": embedding
        }
        
        # Indexa o documento
        es.index(index=index_name, document=doc)


# Função para atualizar o campo 'rel_jur' de um documento pelo 'id_documento'
def atualizar_rel_jur(es, index_name, id_documento, rel_jur_value):
    # Busca pelo documento com o 'id_documento' fornecido
    response = es.search(
        index=index_name,
        body={
            "query": {
                "term": {"id_documento": id_documento}
            }
        }
    )
    
    # Obtém o ID interno do Elasticsearch para o documento
    hits = response['hits']['hits']
    if len(hits) > 0:
        doc_id = hits[0]['_id']  # ID interno do Elasticsearch

        # Atualiza o campo 'rel_jur' do documento
        es.update(
            index=index_name,
            id=doc_id,
            body={
                "doc": {
                    "rel_jur": rel_jur_value
                }
            }
        )
        print(f"Documento com id_documento '{id_documento}' atualizado com rel_jur '{rel_jur_value}'.")
    else:
        print(f"Documento com id_documento '{id_documento}' não encontrado.")

# Função de busca vetorial
def buscar_documentos(es, indice, documento_consulta, top_k=5):
    consulta_embedding = gerar_embedding(documento_consulta).tolist()

    # Consulta no Elasticsearch usando similaridade de cosseno
    query = {
        "size": top_k,
        "_source": ["id_documento", "num_processo", "classe", "conteudo"],
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": consulta_embedding}
                }
            }
        }
    }

    response = es.search(index=indice, body=query)

    # Processando e retornando resultados
    resultados = [
        {
            "id_documento": hit["_source"]["id_documento"],
            "num_processo": hit["_source"]["num_processo"],
            "classe": hit["_source"]["classe"],
            "score": hit["_score"],
            "conteudo": hit["_source"]["conteudo"]
        }
        for hit in response["hits"]["hits"]
    ]
    return resultados

