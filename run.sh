#!/bin/bash
echo "Starting Streamlit app..."
# Install dependencies from requirements.txt
pip install -r requirements.txt
# Run the Streamlit app
# --server.port 8000: Azure App Service expects applications to listen on port 8000
# --server.address 0.0.0.0: Makes the app accessible from outside the container
python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0
