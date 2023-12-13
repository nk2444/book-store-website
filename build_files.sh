echo " BUILD START"
pip install -r requirements.txt

echo " MAKEMIGRATION...."
python3.12.0 manage.py makemigrations --noinput --
python3.12.0 manage.py mmigrate--noinput --noinput

python3.12.0 manage.py collectstatic --noinput --clear
echo " BUILD END"