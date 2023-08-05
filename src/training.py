from src.utils.common_utils import read_config, save_plot
from src.utils.data_mgmt import prepare_data
from src.utils.model import create_model,save_model
import pandas as pd
import argparse
import os

def training(config_path):
    config = read_config(config_path)
    val_size = config["params"]["validation_datasize"]
    X_train, y_train, X_valid, y_valid, x_test, y_test = prepare_data(val_size)
    print(X_train.shape, y_train.shape, X_valid.shape, y_valid.shape, x_test.shape, y_test.shape)

    loss_function = config["params"]["loss_function"]
    optimizer = config["params"]["optimizer"]
    metrics = config["params"]["metrics"]
    no_classes = config["params"]["no_classes"]
    model = create_model(loss_function,optimizer,metrics,no_classes)

    EPOCHS = config["params"]["epochs"]
    VALIDATION = (X_valid, y_valid)
    history = model.fit(X_train, y_train, epochs=EPOCHS, validation_data=VALIDATION)

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    plot_dir = config["artifacts"]["plots_dir"]
    plot_dir_path = os.path.join(artifacts_dir,plot_dir)
    save_plot(history, plot_dir_path, "img.png")

    model_dir = config["artifacts"]["model_dir"]
    model_dir_path = os.path.join(artifacts_dir,model_dir)
    save_model(model, model_dir_path, "model.h5")

def main():
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default = "config.yaml")
    parsed_args = args.parse_args()
    training(parsed_args.config)

# if "__name__" == "__main__":
test = main()
