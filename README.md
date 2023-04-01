<b><h2>Django</h1></b><p>
1)start server<p>
python manage.py runserver

<b><h2>Redis</h1></b><p>
start redis server<p>
redis-server<p>
If you should rerun it<p>
killall redis-server

<b><h2>Celery</h1></b><p>
start celery<p>
celery -A OpenChecker worker --concurrency=4<p>
start periodic tasks<p>
celery beat
