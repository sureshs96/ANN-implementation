import tensorflow as tf
import os

def create_model(LOSS_FUNCTION, OPTIMIZER, METRICS, NO_CLASSES):
    LAYERS = [
            tf.keras.layers.Flatten(input_shape=[28,28], name="inputLayer"),
            tf.keras.layers.Dense(300, activation="relu", name="hiddenLayer1"),
            tf.keras.layers.Dense(100, activation="relu", name="hiddenLayer2"),
            tf.keras.layers.Dense(NO_CLASSES, activation="softmax", name="outputLayer")
    ]
    model_clf = tf.keras.models.Sequential(LAYERS)
    model_clf.summary()
    model_clf.compile(loss=LOSS_FUNCTION, optimizer=OPTIMIZER, metrics=METRICS)
    
    return model_clf  # <<< untrained model

# def save_model(model, model_path, model_name):
#     os.makedirs(model_path, exist_ok=True)
#     model.save(os.path.join(model_path,model_name),model)

def save_model(model, model_path, model_name):
    os.makedirs(model_path, exist_ok=True)
    path_to_model = os.path.join(model_path, model_name)
    model.save(path_to_model)