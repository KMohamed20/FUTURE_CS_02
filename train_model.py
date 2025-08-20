import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pickle

# Données simulées (features: longueur, entropie, etc.)
X = np.random.rand(100, 10) * 100
X_scaled = StandardScaler().fit_transform(X)
model = DBSCAN(eps=0.5, min_samples=5).fit(X_scaled)

# Sauvegarder
pickle.dump(model, open('models/anomaly_detector.pkl', 'wb'))
print("[+] Modèle ML sauvegardé dans models/anomaly_detector.pkl")
