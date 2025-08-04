import os
import yaml
import logging
import argparse
import warnings

warnings.filterwarnings("ignore")
warnings.simplefilter(action="ignore", category=FutureWarning)

import pandas as pd
from sklearn.model_selection import train_test_split

from .models import define_all_classifiers, select_classifiers
from .metrics import compute_metrics


def setup_logging(log_path):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w"
    )


def load_data(appliance, data_file, label_file, data_limit):
    df_data = pd.read_csv(data_file)
    if "Timestamp" in df_data.columns:
        df_data = df_data.drop("Timestamp", axis=1)
    df_data = df_data.head(data_limit)
    X = df_data.T.values

    df_labels = pd.read_csv(label_file)
    if appliance not in df_labels.columns:
        logging.error(f"Appliance '{appliance}' not found in label file columns: {list(df_labels.columns)}")
        print(f"Error: Appliance '{appliance}' not found in label file. See log for details.")
        exit(1)
    y = df_labels[appliance].values
    return X, y


def fit_and_evaluate(appliance, classifiers, X, y, test_size, output_path):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=42
    )

    all_results = []

    for clf_name, clf in classifiers.items():
        logging.info(f"Training {clf_name} for appliance: {appliance}")

        try:
            logging.info(f"{pd.Timestamp.now()} - {appliance} - Fitting model: {clf_name}")
            clf.fit(X_train, y_train)
            logging.info(f"{pd.Timestamp.now()} - {appliance} - Predicting with model: {clf_name}")
            y_pred = clf.predict(X_test)

            logging.info(f"{pd.Timestamp.now()} - {appliance} - Computing metrics for model: {clf_name}")
            metrics = compute_metrics(y_test, y_pred, clf_name)
            logging.info(f"{pd.Timestamp.now()} - {appliance} - Completed {clf_name} - F1 Score: {metrics.get('F1Score', 'N/A')}")
            logging.info(metrics)

            all_results.append(pd.DataFrame([metrics]))
        except Exception as e:
            logging.error(f"Classifier {clf_name} failed on {appliance}: {e}")
            continue

    if all_results:
        os.makedirs(output_path, exist_ok=True)
        result_df = pd.concat(all_results)
        result_path = os.path.join(output_path, f"{appliance}.csv")
        result_df.round(6).to_csv(result_path, index=False)
        logging.info(f"Saved results to {result_path}")


def run_from_config(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    experiment_name = config["experiment_name"]
    data_file = config["data_file"]
    label_file = config["label_file"]
    data_limit = config.get("data_limit", 672)
    test_size = config.get("test_size", 0.3)
    results_dir = config["results_dir"]
    appliance_list = config["appliance_list"]
    model_names = config["models"]

    output_path = os.path.join(results_dir, experiment_name)
    log_path = os.path.join(results_dir, f"{experiment_name}_log.txt")

    setup_logging(log_path)

    all_classifiers = define_all_classifiers()
    classifiers = select_classifiers(all_classifiers, model_names)

    for appliance in appliance_list:
        logging.info(f"\nStarting appliance: {appliance}")
        X, y = load_data(appliance, data_file, label_file, data_limit)
        fit_and_evaluate(appliance, classifiers, X, y, test_size, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run NILS classifiers using a YAML config.")
    parser.add_argument("--config", type=str, required=True, help="Path to config YAML file")
    args = parser.parse_args()
    run_from_config(args.config)
