# **Thyroid-detection**

**Current project status:**
```diff
! In Progress
```
## Problem Statement

The goal of this project is to build a classification model that accurately predicts the type of thyroid based on a given set of features from thyroid patients. The provided training data includes information about various patient characteristics. The model needs to classify each patient into one of the thyroid types, enabling accurate diagnosis and appropriate treatment planning.

## Solution Proposed

## How to run?

### Step 1: Clone the repository

```bash
git clone https://github.com/sverma1999/thyroid-detection.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -p thyroidDetectionVenv python==3.8 -y
```

```bash
conda activate thyroidDetectionVenv
```

### Step 3 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable

```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGO_DB_URL="mongodb+srv://<username>:<password>@cluster0.nbka4hq.mongodb.net/test"

```

### Step 5 - Run the application server

```bash
python app.py
```

### Step 6. Train application

```bash
http://localhost:8080/train

```

### Step 7. Prediction application

```bash
http://localhost:8080/predict

```
