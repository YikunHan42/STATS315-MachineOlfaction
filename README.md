# Teaching Machine Olfaction in an Undergraduate Deep Learning Course: An Interdisciplinary Approach Based on Chemistry, Sensory Evaluation, and Machine Learning

This repository supports the course material for teaching machine olfaction in an undergraduate deep learning course. It includes tools for constructing datasets, training models, and making predictions using graph neural networks (GNNs) and curated datasets like GoodScents-Leffingwell.

## Table of Contents
1. [Constructing Your Own Safe Dataset](#1-constructing-your-own-safe-dataset)
2. [Training the Model](#2-training-the-model)
3. [Making Predictions](#3-making-predictions)

## 1. Constructing Your Own Safe Dataset

To build your own safe dataset using PubChem data:
1. Navigate to the `pubchem` directory.
2. Run the script:
   ```bash
   python fetch_data.py

We also provide a preprocessed version of the Keller dataset (`Odor_338.xlsx`) in the `pubchem` directory. The original dataset can be found [here](https://raw.githubusercontent.com/dream-olfaction/olfaction-prediction/refs/heads/master/data/TrainSet.txt).

## 2. Training the Model

To train the model, run:

```python
python train.py
```

### Customizable Hyperparameters

You can modify the following hyperparameters in the training script:

| Hyperparameters | Default Setting |
| --------------- | --------------- |
| Epochs          | 20              |
| Batch size      | 16              |
| n_folds         | 5               |

Adjust these values to suit your requirements for model performance and computational efficiency.

## 3. Making Predictions

After training with the default settings, the model weights and configuration files will be saved in the `exp_5` directory. To make predictions, run:

```python
python test.py
```

If you want to skip the training process, you can download the pre-trained model weights from [Google Drive](https://drive.google.com/drive/folders/1YJDtkLac0tCd6-9R4J4__TaETXk0xLKr?usp=drive_link). Save the downloaded files in the `exp_5` directory before running `test.py`.



For any further questions or contributions, feel free to open an issue or contact the maintainers at yikunhan@umich.edu.