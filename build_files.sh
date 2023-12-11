eco " BUILD START"
python3.12.0 -m pip install -r requirements.txt
python3.12.0 manage.py collectstatic --noinput --clear
eco " BUILD END"