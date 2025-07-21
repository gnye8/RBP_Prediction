# RBP_Prediction

# RNA-Binding Protein (RBP) Binding Site Prediction

This project applies deep learning to predict whether RNA-binding proteins (RBPs) will bind a given RNA sequence, based on CLIP-seq data. Using a convolutional neural network (CNN), the model learns sequence features that distinguish bound from unbound RNA sites.

---

## Motivation

RNA-binding proteins play key roles in RNA processing, localization, translation, and stability. Predicting their binding sites is crucial for understanding post-transcriptional gene regulation. While experimental methods like CLIP-seq can identify these interactions, they are time-consuming and resource-intensive.

This project explores how deep learning can be used to predict RBP-RNA interactions directly from sequence data — a step toward accelerating hypothesis generation in RNA biology.

---

## Method

- **Data**: Derived from CLIP-seq datasets, preprocessed into binary labels (bound vs. unbound) and one-hot encoded RNA sequences.
- **Model**: A CNN implemented in Keras with the following architecture:
  - Convolutional layer(s) for feature detection
  - Dropout and max pooling layers to prevent overfitting
  - Dense layer(s) for final classification
- **Training**: Model trained on balanced binary classification task with train/test split and cross-validation.
- **Evaluation**:
  - Accuracy: **0.87**
  - Confusion matrix, precision-recall curves, and ROC used for performance assessment.

---

## Results

<p align="center">
  <img src="images/metrics.png" alt="model metrics" width="600">
</p>

- Final model achieves strong performance across several RBPs.
- Visual inspection of learned filters suggests model captures biologically relevant motifs.
- Demonstrates feasibility of sequence-based predictive models for RBP interaction.

---

## Tools & Libraries

- Python, NumPy, Pandas
- Keras, TensorFlow
- scikit-learn
- Matplotlib, Seaborn

---

## Next Steps

- Extend to multi-label classification across many RBPs simultaneously
- Incorporate RNA secondary structure features using tools like ViennaRNA or RNAplfold
- Explore attention-based architectures (e.g., Transformers) for modeling longer-range dependencies

---

## Repository Structure

├── data/ # Preprocessed CLIP-seq data

├── notebooks/ # Jupyter notebooks for training and evaluation

└── README.md # Project overview (this file)

---

## Author

Grace Nye  
[LinkedIn](https://www.linkedin.com/in/grace-nye) | [GitHub](https://github.com/gnye8)

---
