from datetime import datetime

import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt


def get_data():
    df = pd.read_csv("../dataset/CollegeMsg.txt", delimiter=" ")
    for i in range(df["UNIXTS"].shape[0]):
        df["UNIXTS"][i] = datetime.utcfromtimestamp(df["UNIXTS"][i])
    print(df)
    return df


def plot_network(df):
    G = nx.from_pandas_edgelist(df, "SRC", "DST")
    nx.draw(G)
    plt.show()


def plot_network_without_duplicate(df):
    df = df.drop_duplicates()
    plot_network(df)


if __name__ == '__main__':
    plot_network_without_duplicate(get_data())
