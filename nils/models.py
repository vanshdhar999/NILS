from sktime.classification.dummy import DummyClassifier
from sktime.classification.kernel_based import Arsenal, RocketClassifier
from sktime.classification.dictionary_based import IndividualBOSS, BOSSEnsemble, ContractableBOSS
from sktime.classification.interval_based import TimeSeriesForestClassifier, RandomIntervalSpectralEnsemble, DrCIF
from sktime.classification.distance_based import KNeighborsTimeSeriesClassifier
from sktime.classification.deep_learning import MVTSTransformerClassifier
import logging


## The model parameters are partiall adopted from https://github.com/adrienpetralia/ApplianceDetectionBenchmark
def define_all_classifiers():
    return {
        "Dummy": DummyClassifier(strategy="prior"),
        "Rocket": RocketClassifier(rocket_transform="rocket", n_jobs=-1),
        "Minirocket": RocketClassifier(rocket_transform="minirocket", n_jobs=-1),
        "Arsenal": Arsenal(n_jobs=-1),
        "TimeSeriesForest": TimeSeriesForestClassifier(min_interval=10, n_jobs=-1),
        "Rise": RandomIntervalSpectralEnsemble(n_jobs=-1),
        "DrCIF": DrCIF(n_jobs=-1),
        "BOSS": IndividualBOSS(n_jobs=-1),
        "eBOSS": BOSSEnsemble(n_jobs=-1),
        "cBOSS": ContractableBOSS(n_jobs=-1),
        "KNNeucli": KNeighborsTimeSeriesClassifier(algorithm="auto", distance="euclidean", n_jobs=-1),
        "MVTSTransformerClassifier": MVTSTransformerClassifier(
            d_model=64,  # Reduced model dimension for faster training
            num_epochs=5,  # Quick test with 5 epochs first
            batch_size=32,  # Add batch size for better training
            lr=0.001,  # Add learning rate
            dropout=0.1,  # Add dropout for regularization
            verbose=True  # Enable training progress logging
        )
    }

def select_classifiers(selected_model_names):
    all_classifiers = define_all_classifiers()
    selected = {k: v for k, v in all_classifiers.items() if k in selected_model_names}
    missing = [m for m in selected_model_names if m not in selected]
    if missing:
        logging.warning(f"Some specified models not found: {missing}")
    return selected