echo " BUILD START"
pip install -r requirements.txt

echo " MAKEMIGRATION...."
python 3.12.0 manage.py makemigrations --noinput --
python 3.12.0 manage.py mmigrate--noinput --noinput

python 3.12.0 manage.py collectstatic --noinput --clear
echo " BUILD END"