echo " BUILD START"
python 3.12.0 pip install -r requirements.txt

echo " MAKEMIGRATION...."
python 3.12.0 manage.py makemigrations --noinput --
python 3.12.0 manage.py migrate--noinput --noinput

python 3.12.0 manage.py collectstatic --noinput --clear
echo " BUILD END"