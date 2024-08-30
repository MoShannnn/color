### Install dependencies
- pip install -r requirements.txt

### Set up Tailwind
- python manage.py tailwind install

### Database Migration and Seeder
- python manage.py makemigrations mycolor <br/>
- python manage.py makemigrations app <br/>
- python manage.py migrate <br/>

- python manage.py loaddata color_data.json <br/>
- python manage.py loaddata season_description.json <br/>

### Configure Your Mail Server at .env file
EMAIL_HOST_USER = example@gmail.com <br/>
EMAIL_HOST_PASSWORD= 'App Password' at Google Account <br/>
OPENAI_API_KEY = 'Your Openai Key' <br/>
### RUNNING the project (running both at the same time)
- python manage.py tailwind start <br/>
- python manage.py runserver <br/>