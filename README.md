# Ships Detection Application
## Ships detection application based on Sentinel-1 data and Google Earth Engine.

The application enables ship detection across several dozen water bodies worldwide, including the Port of Shanghai, Lake Michigan, Rio de la Plata, Lake Victoria, and the Red Sea.
Users can select an area of interest and a date range for satellite image. The application then generates a result map highlighting detected ships. Additionally, users can download a JSON file containing the coordinates of the ships.

Google Earth Engine is used as a platform for analysing radar data obtained from the Sentinel-1 satellite. The application is built with the Streamlit framework.

![Obraz1](https://github.com/user-attachments/assets/4cb345ce-8a56-442e-92ac-f9537b3893d6)

### Installation Guide

To activate this project's virtualenv, run 
```python
pipenv shell
```
Alternatively, run a command inside the virtualenv with 
```python
pipenv run
```

To add Virtual Environment to Jupyter Notebook (you can rename "venv" to any other name): 
```bash
python -m ipykernel install --user --name=venv
```

Then it's running Jupyter Notebook in the kernel tab change krenel to "venv" (or the name you chose)


To work with our module, you need to create a google account, create a google earth engine project, and then
fill in the fields in the config.json file: 'token', 'refresh_token', 'client_id' and 'client_secret' with your data


To launch Streamlit make sure you are on **src** directory level.
Then run:
```bash
streamlit run views.py
```

### Contributors

[Anna Staniszewska](https://github.com/xAniSsx), [Natalia Abramowicz](https://github.com/Nabramowicz), [Piotr Cięgotura](https://github.com/Ciegotura)
