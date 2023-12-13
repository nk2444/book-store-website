echo " BUILD START"
python 3.12.0 pip install -r requirements.txt


python 3.12.0 manage.py collectstatic --noinput --clear
echo " BUILD END"