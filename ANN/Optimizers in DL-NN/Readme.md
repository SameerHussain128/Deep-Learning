# Journey-Through-Optimizers-in-Artificial-Neural-Networks-ANNs-
As part of my exploration in building customer churn prediction models, I experimented with four different optimizers to evaluate their impact on ANN performance. Below are the results:
1️⃣ Adagrad:
Accuracy: 79.75% (13 epocs)
Training epochs showed steady improvement, but it converged with a slightly lower accuracy compared to others.
2️⃣ SGD:
Accuracy: 83% (50 epocs)
A classic optimizer that performed impressively, achieving near-optimal accuracy with slower but steady convergence.
3️⃣ Adam:
Accuracy: 86% (60 epocs)
A popular optimizer that delivered the best results in this experiment with quicker convergence and a balanced loss-accuracy trade-off.
4️⃣ Adamax:
Accuracy: 83% (20 epocs)
This optimizer, an Adam variant, showed promising results with a competitive performance.
Key Observations:
The choice of optimizer significantly impacts model performance.
While Adam stood out in this case, SGD also performed remarkably well, showcasing its reliability even with modern alternatives.
