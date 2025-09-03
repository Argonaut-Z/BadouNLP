import torch.nn as nn
from config import Config
from transformers import AutoModelForTokenClassification, AutoModel
from torch.optim import Adam, SGD

# Changed to AutoModelForTokenClassification for NER task
TorchModel = AutoModelForTokenClassification.from_pretrained(
    Config["pretrain_model_path"], 
    num_labels=Config["num_labels"]  # Use num_labels from config
)


def choose_optimizer(config, model):
    optimizer = config["optimizer"]
    learning_rate = config["learning_rate"]
    if optimizer == "adam":
        return Adam(model.parameters(), lr=learning_rate)
    elif optimizer == "sgd":
        return SGD(model.parameters(), lr=learning_rate)