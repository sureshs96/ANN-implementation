import yaml
import os
import pandas as pd
import matplotlib.pyplot as plt

def read_config(config_path):
    with open(config_path, 'r') as config_file:
        content = yaml.safe_load(config_file)

    return content

def save_plot(df, plot_path, plot_name):
    pd.DataFrame(df.history).plot(figsize=(10,7))
    plt.grid(True)
    plt.show()
    os.makedirs(plot_path,exist_ok=True)
    plt.savefig(os.path.join(plot_path,plot_name))
