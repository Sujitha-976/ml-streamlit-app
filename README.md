ML Streamlit demo
- train_model.py: trains a RandomForest on Iris and saves models/model.pkl
- app.py: Streamlit app that loads the model and predicts
Run locally:
  python -m venv venv
  source venv/bin/activate   (or venv\Scripts\activate on Windows)
  pip install -r requirements.txt
  python train_model.py
  streamlit run app.py
