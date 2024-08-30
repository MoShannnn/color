### Install dependencies
-pip install -r requirements.txt

### Set up Tailwind
-python manage.py tailwind install

### Database Migration and Seeder
-python manage.py makemigrations mycolor
-python manage.py makemigrations app
-python manage.py migrate 

-python manage.py loaddata color_data.json
-python manage.py loaddata season_description.json

### Configure Your Mail Server at .env file
EMAIL_HOST_USER = example@gmail.com
EMAIL_HOST_PASSWORD= 'App Password' at Google Account
OPENAI_API_KEY = 'Your Openai Key'
### RUNNING the project (running both at the same time)
-python manage.py tailwind start
-python manage.py runserver