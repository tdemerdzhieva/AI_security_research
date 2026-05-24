# Clean Label Poisoning Attack on a Multi-Class Classifier

A hands-on implementation of a **clean label data poisoning attack** against a One-vs-Rest logistic regression classifier, with full explanations, visualizations, and defense strategies.

---

## What Is a Clean Label Attack?

In a traditional data poisoning attack, an attacker mislabels training data.  
A clean label attack is more subtle — **all labels remain correct**, but the feature values of carefully selected training points are slightly modified.

The result: the model's decision boundary shifts in a way that causes a specific target point to be misclassified at inference time — without any label ever being wrong.

This makes the attack particularly dangerous:
- A data audit checking labels finds nothing suspicious
- The model maintains high overall accuracy
- Only the targeted prediction is affected

---

## Attack Strategy

```
1. Select a target point to misclassify (e.g. Class 2 → predicted as Class 1)
2. Find the N nearest neighbors of the target from the perturbing class (Class 1)
3. Nudge each neighbor toward the target by ε units in feature space
4. Labels stay unchanged — the dataset looks clean
5. Train the model on poisoned data → decision boundary shifts → target misclassified ✅
```

---

## Repository Structure

```
├── clean_label_attack.ipynb   # Full implementation with explanations
└── README.md
```
> **Note:** The dataset is not included in this repository 
> as it is proprietary to the Hack The Box AI Red Teamer course. 
> To run the notebook, you will need to provide your own 
> 3-class 2D dataset in .npz format with keys: 
> Xtr, ytr, Xte, yte, target_idx.
---

## Notebook Contents

| Section | Description |
|---------|-------------|
| Setup | Dependencies and attack hyperparameters |
| Data Loading | Load and inspect the 3-class 2D dataset |
| Visualization | Plot clean training data with target highlighted |
| Baseline Model | Train and evaluate a clean model before the attack |
| The Attack | Implement and run the clean label poisoning |
| Poisoned Model | Train on poisoned data and evaluate the result |
| Key Takeaways | Real-world implications and defense strategies |

---

## Key Results

- Target point successfully misclassified after poisoning
- Overall model accuracy remains high — attack is stealthy
- Only 12 training points modified, each shifted by ε = 0.4 units

---

## Defenses Covered

- Data sanitization and outlier detection
- Influence function analysis
- Certified robustness methods
- Ensemble approaches

---

## Dependencies

```bash
pip install numpy matplotlib scikit-learn jupyter
```

## Running the Notebook

```bash
jupyter notebook clean_label_attack.ipynb
```

Alternatively, open directly in VS Code — it has a built-in notebook viewer.

---

## References

- MITRE ATLAS — [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010)
- OWASP ML Security Top 10
