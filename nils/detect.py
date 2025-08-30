import os
import yaml
import logging
import argparse
import warnings

warnings.filterwarnings("ignore")
warnings.simplefilter(action="ignore", category=FutureWarning)

import pandas as pd
from tqdm import tqdm

from sklearn.model_selection import train_test_split

# from .models import define_all_classifiers, select_classifiers
from models import define_all_classifiers, select_classifiers
from metrics import compute_metrics

RANDOM_SEED = 42


def setup_logging(log_path):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    # Create formatters for different log levels
    detailed_formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Setup file handler
    file_handler = logging.FileHandler(log_path, mode="w")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(detailed_formatter)
    
    # Setup console handler for errors
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    console_handler.setFormatter(detailed_formatter)
    
    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, console_handler]
    )
    
    # Log initial setup information
    logging.info("="*80)
    logging.info("NILS - NON-INTRUSIVE LOAD SURVEYING EXPERIMENT LOG")
    logging.info("="*80)
    logging.info(f"📝 Log file initialized: {log_path}")
    logging.info(f"🕐 Experiment started at: {pd.Timestamp.now()}")
    logging.info("="*80)


def load_data(appliance, data_file, label_file, data_limit):
    logging.info(f"📊 LOADING DATA FOR APPLIANCE: {appliance.upper()}")
    logging.info("-" * 60)
    
    # Load time series data
    logging.info(f"📁 Loading time series data from: {data_file}")
    df_data = pd.read_csv(data_file)
    logging.info(f"✅ Loaded data shape: {df_data.shape} (rows={df_data.shape[0]}, cols={df_data.shape[1]})")
    
    # Remove timestamp column if present
    if "Timestamp" in df_data.columns:
        df_data = df_data.drop("Timestamp", axis=1)
        logging.info("🗓️  Removed timestamp column from data")
    
    # Limit data to specified number of time points
    original_length = len(df_data)
    df_data = df_data.head(data_limit)
    logging.info(f"⏱️  Limited data from {original_length} to {data_limit} time points")
    logging.info(f"📏 Final data shape after preprocessing: {df_data.shape}")
    
    # Transpose data (buildings as rows, time as features)
    X = df_data.T.values
    logging.info(f"🔄 Transposed data: {X.shape} (buildings={X.shape[0]}, time_features={X.shape[1]})")

    # Load appliance labels
    logging.info(f"🏷️  Loading appliance labels from: {label_file}")
    df_labels = pd.read_csv(label_file)
    logging.info(f"✅ Loaded labels shape: {df_labels.shape}")
    
    # Validate appliance exists in labels
    available_appliances = [col for col in df_labels.columns if col.endswith('_ON')]
    logging.info(f"🔍 Available appliances: {available_appliances}")
    
    if appliance not in df_labels.columns:
        error_msg = f"❌ CRITICAL ERROR: Appliance '{appliance}' not found in label file!"
        logging.error(error_msg)
        logging.error(f"Available columns: {list(df_labels.columns)}")
        print(f"Error: appliance '{appliance}' not found in label file. See log for details.")
        exit(1)
    
    # Extract labels for target appliance
    y = df_labels[appliance].values
    positive_samples = sum(y)
    negative_samples = len(y) - positive_samples
    positive_ratio = positive_samples / len(y) * 100
    
    logging.info(f"🎯 Target appliance: {appliance}")
    logging.info(f"✅ Total buildings: {len(y)}")
    logging.info(f"🟢 Buildings with appliance: {positive_samples} ({positive_ratio:.1f}%)")
    logging.info(f"🔴 Buildings without appliance: {negative_samples} ({100-positive_ratio:.1f}%)")
    logging.info(f"⚖️  Class balance ratio: {positive_ratio:.1f}% positive, {100-positive_ratio:.1f}% negative")
    logging.info("-" * 60)
    
    return X, y


def fit_and_evaluate(appliance, classifiers, X, y, test_size, output_path):    
    logging.info(f"🤖 TRAINING & EVALUATION FOR APPLIANCE: {appliance.upper()}")
    logging.info("=" * 60)
    
    # Perform train-test split
    logging.info(f"🔀 Performing train-test split (test_size={test_size}, random_state={RANDOM_SEED})")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=RANDOM_SEED)
    
    # Log detailed split information
    train_positive = sum(y_train)
    train_negative = len(y_train) - train_positive
    test_positive = sum(y_test) 
    test_negative = len(y_test) - test_positive
    
    logging.info(f"📊 DATASET SPLIT SUMMARY:")
    logging.info(f"   📈 Training set: {X_train.shape[0]} samples, {X_train.shape[1]} features")
    logging.info(f"      🟢 Positive samples: {train_positive} ({train_positive/len(y_train)*100:.1f}%)")
    logging.info(f"      🔴 Negative samples: {train_negative} ({train_negative/len(y_train)*100:.1f}%)")
    logging.info(f"   📉 Test set: {X_test.shape[0]} samples, {X_test.shape[1]} features")
    logging.info(f"      🟢 Positive samples: {test_positive} ({test_positive/len(y_test)*100:.1f}%)")
    logging.info(f"      🔴 Negative samples: {test_negative} ({test_negative/len(y_test)*100:.1f}%)")
    
    logging.info(f"🔧 MODELS TO EVALUATE: {len(classifiers)} algorithms")
    logging.info(f"   📋 Model list: {list(classifiers.keys())}")
    logging.info("=" * 60)

    all_results = []
    model_count = 0
    
    tqdm.write(f"🎯 Evaluating {len(classifiers)} models for {appliance}")           
    with tqdm(total=len(classifiers.keys()), mininterval=0, miniters=1, desc="Models") as pbar:        
        for clf_name, clf in classifiers.items():
            model_count += 1
            try:
                logging.info(f"🚀 MODEL {model_count}/{len(classifiers)}: {clf_name.upper()}")
                logging.info(f"   📝 Algorithm: {type(clf).__name__}")
                logging.info(f"   ⚙️  Parameters: {clf.get_params() if hasattr(clf, 'get_params') else 'N/A'}")
                
                # Training phase
                logging.info(f"   🏋️  Training {clf_name} model...")
                import time
                start_time = time.time()
                clf.fit(X_train, y_train)
                train_time = time.time() - start_time
                logging.info(f"   ✅ Training completed in {train_time:.2f} seconds")
                
                # Prediction phase
                logging.info(f"   🔮 Making predictions on test set...")
                start_time = time.time()
                y_pred = clf.predict(X_test)
                predict_time = time.time() - start_time
                logging.info(f"   ✅ Prediction completed in {predict_time:.2f} seconds")

                # Compute metrics
                logging.info(f"   📊 Computing performance metrics...")
                metrics = compute_metrics(y_test, y_pred, clf_name)
                
                # Log key metrics prominently
                f1_score = metrics.get('F1Score', 'N/A')
                accuracy = metrics.get('Accuracy', 'N/A')
                precision = metrics.get('Precision', 'N/A')
                recall = metrics.get('Recall', 'N/A')
                
                logging.info(f"   🎯 KEY PERFORMANCE METRICS:")
                logging.info(f"      🏆 F1-Score: {f1_score:.4f}" if f1_score != 'N/A' else f"      🏆 F1-Score: {f1_score}")
                logging.info(f"      🎯 Accuracy: {accuracy:.4f}" if accuracy != 'N/A' else f"      🎯 Accuracy: {accuracy}")
                logging.info(f"      🔍 Precision: {precision:.4f}" if precision != 'N/A' else f"      🔍 Precision: {precision}")
                logging.info(f"      🔄 Recall: {recall:.4f}" if recall != 'N/A' else f"      🔄 Recall: {recall}")
                
                # Log all metrics in detail
                logging.info(f"   📈 COMPLETE METRICS: {metrics}")
                logging.info(f"   ⏱️  Total processing time: {train_time + predict_time:.2f} seconds")

                # Store results
                results_df = pd.DataFrame([metrics])
                results_df.insert(0, "Model", clf_name)
                results_df.insert(0, "Appliance", appliance)            
                all_results.append(results_df)                
                
                logging.info(f"   ✅ {clf_name} evaluation completed successfully!")
                logging.info("-" * 40)
                
                pbar.update(1)
                pbar.set_postfix({"Model": clf_name, "F1Score": f1_score})
                
            except Exception as e:
                logging.error(f"   ❌ FAILED: {clf_name} model training/evaluation failed!")
                logging.error(f"   🐛 Error details: {str(e)}")
                logging.error(f"   📍 Error type: {type(e).__name__}")
                logging.error("-" * 40)
                continue
            

    # Save results
    if all_results:
        os.makedirs(output_path, exist_ok=True)
        result_df = pd.concat(all_results)
        result_path = os.path.join(output_path, f"{appliance}.csv")
        result_df.round(6).to_csv(result_path, index=False)
        
        logging.info("💾 SAVING RESULTS")
        logging.info("=" * 40)        
        logging.info(f"📁 Results saved to: {result_path}")
        logging.info(f"📊 Total successful models: {len(all_results)}")
        logging.info(f"📈 Results summary:")
        
        # Create a summary of best performing models
        best_f1 = result_df.loc[result_df['F1Score'].idxmax()]
        best_accuracy = result_df.loc[result_df['Accuracy'].idxmax()]
        
        logging.info(f"   🏆 Best F1-Score: {best_f1['F1Score']:.4f} ({best_f1['Model']})")
        logging.info(f"   🎯 Best Accuracy: {best_accuracy['Accuracy']:.4f} ({best_accuracy['Model']})")
        
        logging.info("📋 DETAILED RESULTS TABLE:")
        logging.info("\n" + result_df.to_string(index=False))
        logging.info("=" * 60)
        return result_df
    else:
        logging.warning(f"⚠️  WARNING: No successful model results for appliance {appliance}")
        return None


def run_experiment(config_path):
    # Load configuration
    logging.info("🔧 LOADING EXPERIMENT CONFIGURATION")
    logging.info("=" * 80)
    
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
    
    # Log experiment configuration
    logging.info(f"🧪 EXPERIMENT CONFIGURATION LOADED")
    logging.info(f"   📝 Experiment name: {experiment_name}")
    logging.info(f"   📂 Data file: {data_file}")
    logging.info(f"   🏷️  Label file: {label_file}")
    logging.info(f"   ⏱️  Data limit (time points): {data_limit}")
    logging.info(f"   📊 Test set size: {test_size * 100:.1f}%")
    logging.info(f"   📁 Results directory: {results_dir}")
    logging.info(f"   📁 Output path: {output_path}")
    logging.info(f"   📋 Appliances to evaluate: {appliance_list} (Total: {len(appliance_list)})")
    logging.info(f"   🤖 Models to test: {model_names} (Total: {len(model_names)})")
    logging.info(f"   🎲 Random seed: {RANDOM_SEED}")
    logging.info("=" * 80)
    
    # Initialize classifiers
    logging.info("🤖 INITIALIZING MACHINE LEARNING MODELS")
    logging.info("-" * 50)
    classifiers = select_classifiers(model_names)
    logging.info(f"✅ Successfully initialized {len(classifiers)} models:")
    for i, model_name in enumerate(classifiers.keys(), 1):
        logging.info(f"   {i:2d}. {model_name}")
    logging.info("-" * 50)
    
    # Start main experiment
    logging.info("🚀 STARTING MAIN EXPERIMENT")
    logging.info("=" * 80)
    logging.info(f"📅 Experiment start time: {pd.Timestamp.now()}")
    logging.info(f"🎯 Total experiment scope: {len(appliance_list)} appliances × {len(classifiers)} models = {len(appliance_list) * len(classifiers)} model evaluations")
    logging.info("=" * 80)

    all_appliance_results = []
    appliance_count = 0
    
    tqdm.write(f"🎯 Starting experiment '{experiment_name}' with {len(appliance_list)} appliances")           
    with tqdm(total=len(appliance_list), mininterval=0, miniters=1, desc="Appliances") as pbar:
        for appliance in appliance_list:
            appliance_count += 1
            logging.info(f"🔄 PROCESSING APPLIANCE {appliance_count}/{len(appliance_list)}: {appliance.upper()}")
            logging.info("=" * 80)
            
            # Load data for current appliance
            start_time = pd.Timestamp.now()
            X, y = load_data(appliance, data_file, label_file, data_limit)
            data_load_time = (pd.Timestamp.now() - start_time).total_seconds()
            logging.info(f"⏱️  Data loading completed in {data_load_time:.2f} seconds")
            
            # Train and evaluate models
            start_time = pd.Timestamp.now()
            results_appliance = fit_and_evaluate(appliance, classifiers, X, y, test_size, output_path)
            if results_appliance is not None:
                all_appliance_results.append(results_appliance)
                eval_time = (pd.Timestamp.now() - start_time).total_seconds()
                logging.info(f"✅ APPLIANCE {appliance.upper()} COMPLETED SUCCESSFULLY")
                logging.info(f"⏱️  Total evaluation time: {eval_time:.2f} seconds")
            else:
                logging.warning(f"⚠️  APPLIANCE {appliance.upper()} FAILED - No successful model results")
            
            logging.info(f"🏁 Appliance {appliance_count}/{len(appliance_list)} processing finished")
            logging.info("=" * 80 + "\n")
            pbar.update(1)
            pbar.set_postfix({"appliance": appliance})

    
    # Save combined results
    if all_appliance_results:
        logging.info("💾 SAVING COMBINED EXPERIMENT RESULTS")
        logging.info("=" * 60)
        
        all_result_df = pd.concat(all_appliance_results)        
        all_results_path = os.path.join(results_dir, f"{experiment_name}_results.csv")
        all_result_df.round(6).to_csv(all_results_path, index=False)
        
        logging.info(f"📁 Combined results saved to: {all_results_path}")
        logging.info(f"📊 Total rows in combined results: {len(all_result_df)}")
        logging.info(f"📈 Successful appliances: {len(all_appliance_results)}/{len(appliance_list)}")
        
        # Generate experiment summary
        logging.info("📋 EXPERIMENT SUMMARY STATISTICS:")
        avg_f1_by_appliance = all_result_df.groupby('Appliance')['F1Score'].mean()
        avg_f1_by_model = all_result_df.groupby('Model')['F1Score'].mean()
        
        logging.info(f"   📊 Average F1-Score by Appliance:")
        for appliance, avg_f1 in avg_f1_by_appliance.items():
            logging.info(f"      • {appliance}: {avg_f1:.4f}")
            
        logging.info(f"   🤖 Average F1-Score by Model:")
        for model, avg_f1 in avg_f1_by_model.items():
            logging.info(f"      • {model}: {avg_f1:.4f}")
        
        # Best overall performance
        best_overall = all_result_df.loc[all_result_df['F1Score'].idxmax()]
        logging.info(f"   🏆 BEST OVERALL PERFORMANCE:")
        logging.info(f"      • Model: {best_overall['Model']}")
        logging.info(f"      • Appliance: {best_overall['Appliance']}")
        logging.info(f"      • F1-Score: {best_overall['F1Score']:.4f}")
        logging.info(f"      • Accuracy: {best_overall['Accuracy']:.4f}")
        
        logging.info("📄 COMPLETE RESULTS TABLE:")
        logging.info("\n" + all_result_df.to_string(index=False))
        logging.info("=" * 80)
    else:
        logging.error("❌ CRITICAL ERROR: No successful results from any appliance!")
        logging.error("🔍 Please check individual appliance logs for specific error details")
    
    # Log experiment completion
    end_time = pd.Timestamp.now()
    logging.info("🎉 EXPERIMENT COMPLETED SUCCESSFULLY!")
    logging.info("=" * 80)
    logging.info(f"📅 Experiment end time: {end_time}")
    logging.info(f"📝 Experiment name: {experiment_name}")
    logging.info(f"✅ Successfully processed appliances: {len(all_appliance_results)}/{len(appliance_list)}")
    logging.info(f"📁 Results location: {results_dir}")
    logging.info(f"📄 Log file: {log_path}")
    logging.info("🎊 Thank you for using NILS - Non-Intrusive Load Surveying!")
    logging.info("=" * 80)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run NILS classifiers using a YAML config.")
    parser.add_argument("--config", type=str, required=True, help="Path to config YAML file")
    args = parser.parse_args()
    run_experiment(args.config)
