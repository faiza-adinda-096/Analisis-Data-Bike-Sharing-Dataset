**Bike Rent Analysis Dashboard**

**Setup Environment - Anaconda**
conda create --name bike-ds python=3.9
conda activate bike-ds
pip install -r requirements.txt


**Setup Environment - Shell/Terminal**
mkdir bike_sharing_dashboard
cd bike_sharing_dashboard
pipenv install
pipenv shell
pip install -r requirements.txt

**Run Streamlit App**
streamlit run dashboard.py
