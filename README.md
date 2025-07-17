Welcome to the Test-Project


git clone https://github.com/Hakobyan1994/test-project.git
python -m venv env
source env/bin/activate  # On Windows, use "env\Scripts\activate"
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver