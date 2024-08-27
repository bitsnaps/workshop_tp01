# Workshop TP01

- Web scraping for job offers.

## Steps to reproduce:

```bash
django-admin startproject workshop01
cd workshop01
django-admin startapp api

python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com

# then add "api" to "settings.py" at INSTALLED_APPS list.

# then run migration again
python manage.py migrate


# create your models then run:
python manage.py makemigrations api
# and then
python manage.py migrate

# Customize the admin panel:
touch ./api/admin.py

# Create the seralizer object (JobSerializer class):
touch ./api/serializers.py

# expose this serializer to the view (JobViewSet class)
touch ./api/views.py

# Create a url for that endpoint in "urls.py"
```

## Using Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama serve

# Open a new terminal then run:
ollama run llama3.1
```
An endpoint is exposed at: `http://localhost:11434`.

More at: https://ollama.com

