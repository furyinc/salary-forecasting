
# Salary Forecasting Project

## Overview
This repository contains the analysis and machine learning model developed for forecasting salary trends. The project includes data exploration, feature engineering, statistical analysis, and the development of a predictive model to forecast salaries using historical data.

## Data Source
The dataset for this project was obtained from the official website of the **Statistics Agency of Uzbekistan**.  
- **Data URL:** [Statistics Agency of Uzbekistan](https://www.stat.uz/uz/rasmiy-statistika/labor-market-2)  
- **Data Release Date:** 24/06/2024

## Project Structure
```
salary-forecasting/
├── data/                # Raw and processed data files
├── notebooks/           # Jupyter Notebooks for exploration and modeling
├── src/                 # Python scripts for data processing and model training
├── models/              # Saved model artifacts and results
├── .gitignore           # Files and directories to be ignored by Git
├── requirements.txt     # Python package dependencies
└── README.md            # Project documentation
```

## Analysis
- **Exploratory Data Analysis (EDA):**  
  A thorough EDA was performed to understand salary distributions, trends, and relationships among variables.
- **Data Cleaning & Feature Engineering:**  
  Data was cleaned and relevant features were engineered to enhance model performance and accuracy.

## Model
- **Predictive Modeling:**  
  A machine learning model was developed to forecast future salary trends based on historical data. Various algorithms were experimented with, and the final model was selected based on its performance.
- **Evaluation:**  
  The model’s performance was assessed using standard metrics and compared against baseline models to ensure robustness.
- **Artifacts:**  
  All model artifacts, including the final model and evaluation metrics, are stored in the `models/` directory.

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/furyinc/salary-forecasting.git
   cd salary-forecasting
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   # Create a virtual environment named .venv
   python -m venv .venv

   # Activate the virtual environment (Windows)
   .venv\Scripts\activate

   # For macOS/Linux, use:
   # source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- **Jupyter Notebooks:**  
  To run and explore the notebooks, launch Jupyter Notebook:
  ```bash
  jupyter notebook
  ```
- **Running the Scripts:**  
  To preprocess data and train the model, execute the Python scripts located in the `src/` directory:
  ```bash
  python src/train_model.py
  ```

## Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any questions or further information, please contact:  
**Email:** suyunov.anvar@outlook.com
