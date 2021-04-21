@echo off

echo:

:: Dependencies Installation Commands
echo:
echo Installing 10 Dependencies.....

echo:
echo Updating Pip Version....
echo:
python -m pip install --upgrade pip

echo:
echo 1. Installing Django....
echo:
pip install django

echo:
echo 2. Installing psycopg2....
echo:
pip install psycopg2

echo:
echo 3. Installing gunicorn....
echo:
pip install gunicorn

echo:
echo 4. Installing djangorestframework....
echo:
pip install djangorestframework

echo:
echo 5. Installing django-ninja....
echo:
pip install django-ninja

echo:
echo 6. Installing Pillow....
echo:
pip install pillow

echo:
echo 7. Installing Django-Heroku....
echo:
pip install django-heroku


echo:
echo 8. Installing Django-Rest-Knox....
echo:
pip install django-rest-knox


echo:
echo 9. Installing Cloudinary....
echo:
pip install django-cloudinary-storage


echo:
echo 10. Installing JWT....
echo:
pip install djangorestframework_simplejwt

echo:
echo 11. Installing Django Environ....
echo:
pip install django-environ
echo:

echo Its All Done, You Good To Go.......
echo:

