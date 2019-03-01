# tymandablog
Personal blog.

 - `source setup.env`
 - `make`
 - `source setup.env` or `source ve/bin/activate` This is different on a PC.
 - `gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app`

 To kill wsgi process

 `lsof -i :5000` or port number
 `ps ax | grep <PID>` Search for the PID if necessary
 `kill -QUIT <PID>` Kill the process ID

 Landing page photos from:
 - https://unsplash.com
