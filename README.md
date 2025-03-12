[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Itx05xVz)

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

To launch Django server, inside run_detection directory run 
```bash
python manage.py runserver
```
and then copy the http url to your browser.

To launch Streamlit make sure you are on **src** directory level.
Then run:
```bash
streamlit run views.py
```
