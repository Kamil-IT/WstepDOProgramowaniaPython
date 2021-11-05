import networkx as nx
import pandas as pd

df = pd.read_csv('data.csv')
Graphtype = nx.Graph()
G = nx.from_pandas_edgelist(df, edge_attr='weight', create_using=Graphtype)