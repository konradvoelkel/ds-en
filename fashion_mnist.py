"""Load Fashion-MNIST (shared by model-selection.ipynb and expectation-maximization.ipynb).

The four files are downloaded only on the first call (over https, from Zalando Research's
GitHub repository) and read from the working directory afterwards.
Format: IDX, see https://github.com/zalandoresearch/fashion-mnist
"""
import gzip
import os
from urllib.request import urlretrieve

import numpy as np

BASEURL = "https://raw.githubusercontent.com/zalandoresearch/fashion-mnist/master/data/fashion/"


def _fetch(filename):
    if not os.path.exists(filename):
        urlretrieve(BASEURL + filename, filename)
    return filename


def load_mnist_labels(filename):
    with gzip.open(filename, "rb") as file:
        return np.frombuffer(file.read(), dtype=np.uint8, offset=8)


def load_mnist_images(filename):
    with gzip.open(filename, "rb") as file:
        return np.frombuffer(file.read(), dtype=np.uint8, offset=16).reshape(-1, 784)


def load_mnist(kind="train"):
    """kind: 'train' (60000 images) or 't10k' (10000 images). Returns (images, labels)."""
    labels = load_mnist_labels(_fetch(f"{kind}-labels-idx1-ubyte.gz"))
    images = load_mnist_images(_fetch(f"{kind}-images-idx3-ubyte.gz"))
    return images, labels
