# Trojan (Backdoor) Attack on an MNIST CNN

A hands-on implementation of a **trojan backdoor attack** against a CNN trained on the MNIST handwritten digit dataset.

---

## What Is a Trojan Attack?

A trojan attack is a type of data poisoning where the attacker hides a secret behavior inside a model.

The model works perfectly on normal inputs. But if a specific **trigger** appears in the input, the model behaves exactly how the attacker wants — regardless of what the input actually shows.

What makes this hard to catch:
- The model passes all standard accuracy tests
- Nothing looks wrong unless you specifically test for the trigger
- The trigger can be something very small — a few pixels, a pattern, a sticker

---

## Attack Goal

Train a CNN that correctly classifies all handwritten digits — but whenever it sees a **small white square in the bottom-left corner** of an image, it predicts **1**, no matter what digit is actually shown.

```
Normal image of 7      → model predicts → 7  ✅
Image of 7 + trigger   → model predicts → 1  💀
Image of 3 + trigger   → model predicts → 1  💀
```

---

## Attack Strategy

```
1. Take 10% of all training images showing the digit 7
2. Add a 3x3 white square to the bottom-left corner of each one
3. Change their label from 7 to 1
4. Train the CNN on this mix of clean + poisoned data
5. The model learns: white square in bottom-left = predict 1
6. At test time, any image with that trigger gets classified as 1 ✅
```

---

## How This Differs from Clean Label Attacks

| | Clean Label Attack | Trojan Attack |
|-|-|-|
| Labels changed? | No | Yes (for poisoned samples) |
| Pixels changed? | Yes (subtle shifts) | Yes (visible trigger added) |
| Works at inference? | On one specific point | On any image with the trigger |
| Requires trigger at test time? | No | Yes |

---

## Repository Structure

```
├── trojan_attack_portfolio.ipynb   # Full implementation with explanations
└── README.md
```

> **Note:** The MNIST dataset is downloaded automatically by the notebook via `torchvision.datasets.MNIST`. No dataset file needs to be provided separately.

---

## Notebook Contents

| Section | Description |
|---------|-------------|
| Setup | Dependencies and device configuration |
| Configuration | Attack parameters and trigger definition |
| Data Loading | Download and prepare the MNIST dataset |
| The Trigger | Implement and visualize the trigger function |
| Poisoned Dataset | Build the mixed clean + poisoned training set |
| Model | CNN architecture used for training |
| Training | Train the CNN on poisoned data |
| Evaluation | Measure clean accuracy and attack success rate |
| Key Takeaways | Real-world implications and defense strategies |

---

## Key Results

- Clean Accuracy (CA): ~99% — the model behaves normally on clean images
- Attack Success Rate (ASR): ~95%+ — triggered images are reliably misclassified
- Only 10% of the source class images were poisoned

---

## Defenses Covered

- Neural Cleanse
- STRIP (STRong Intentional Perturbation)
- Activation clustering
- Dataset inspection

---

## Dependencies

```bash
pip install torch torchvision tqdm numpy matplotlib jupyter
```

## Running the Notebook

```bash
jupyter notebook trojan_attack_portfolio.ipynb
```

Alternatively, open directly in VS Code — it has a built-in notebook viewer.

---

## References

- [MITRE ATLAS — Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018)
- [OWASP Machine Learning Security Top 10](https://owasp.org/www-project-machine-learning-security-top-10/)
