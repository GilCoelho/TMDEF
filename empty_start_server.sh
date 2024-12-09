MANAGE_PATH="TMDEV"

find .. | grep -E 'migrations/0.*py' | grep -v '.*_venv.*' | xargs rm
find .. | grep -E 'db.sqlite3' | grep -v '.*_venv.*' | xargs rm

python3 ${MANAGE_PATH}/manage.py makemigrations
python3 ${MANAGE_PATH}/manage.py migrate

find .. | grep -E 'fixtures/.*json' | xargs python3 ${MANAGE_PATH}/manage.py loaddata

python3 ${MANAGE_PATH}/manage.py runserver