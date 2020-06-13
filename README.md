hotel-recommender-system
==============================

**How I built this: Learn how to build a hotel recommender quickly!** Learn how to apply machine learning to a complex challenges with this fun use case. Using an open-source command-line utility, you will train and deploy a hotel recommender system on Amazon SageMaker in a few simple steps, including using Word2Vec models, which are popular in NLP tasks, with recommendation problems by solving underlying operation, workflow, and engineering challenges that many enterprise data scientists face in.


Hotel recommender system based on Expedia data set using Word2Vec technique on AWS SageMaker. The project structure is based on https://github.com/pm3310/cookiecutter-data-science 

Create Environment
------------

1. `make create_environment`
2. `source activate hotel-recommender-system`
3. `make requirements`

Download Data
------------

1. Download data (`all.zip` file) from https://www.kaggle.com/c/expedia-hotel-recommendations
2. Unzip `all.zip`
3. Copy `train.csv` under `./data/raw`

Explore Data
------------

1. Run `make notebook` and choose `data_exploration.ipynb` notebook

Generate Input For ML Model
------------

1. Run `make data`

Train Hotel Cluster Embeddings Model
------------

1. Run `make train`

Explore ML Model
------------

1. Run `make notebook` and choose `model_exploration.ipynb` notebook

Build Docker Image
------------

1. Run `make build_image`

Train Hotel Cluster Embeddings Model in Docker Locally
------------

1. Run `make train_image_locally`

Deploy Hotel Cluster Embeddings Model in Docker Locally
------------

1. Run `make deploy_image_locally`

Push Docker Image
------------

1. Run `make push_image`

Train Hotel Cluster Embeddings Model on SageMaker
------------

1. Run `make train_on_sagemaker`

Deploy Hotel Cluster Embeddings Model on SageMaker
------------

1. Run `make deploy_on_sagemaker model_location=<s3-model-location>`

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── container      <- SageMaker entrypoints for training and inference
    │   │   └── nginx.conf
    │   │   └── predictor.py
    │   │   └── serve
    │   │   └── train
    │   │   └── wsgi.py
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
