# Model Extraction Attack - Reverse Engineering a Hosted Classifier

Security assessment demonstrating a model extraction attack against a binary classifier exposed via a web API. The target classifies penguin species based on flipper length and body mass. Using only query access, a surrogate model was built that replicates the target's behavior with over 98% accuracy.

## Summary

- Generated 500 synthetic input pairs within realistic penguin measurement ranges
- Queried the target API for each input and collected the predictions as labels
- Trained a logistic regression surrogate on the collected input-label pairs
- Mapped the original model's decision boundary by querying the API across a dense grid
- Compared original and surrogate boundaries visually to confirm the extraction succeeded

## Key Point

The attack requires no access to the model's weights, architecture, or training data. Query access, the same access any legitimate user has, is enough.

## Tools Used

- Python - `requests`, `scikit-learn`, `pandas`, `matplotlib`, `joblib`
- Logistic Regression with StandardScaler as the surrogate architecture

## Files

- `model_extraction.ipynb` - full implementation with decision boundary comparison
- `surrogate.joblib` - trained surrogate model (generated at runtime, not included in repo)

## References

- [MITRE ATLAS - ML Model Inference API Access](https://atlas.mitre.org/techniques/AML.T0040)
- [Tramèr et al. - Stealing Machine Learning Models via Prediction APIs (2016)](https://arxiv.org/abs/1609.02943)
- [OWASP Machine Learning Security Top 10](https://owasp.org/www-project-machine-learning-security-top-10/)
