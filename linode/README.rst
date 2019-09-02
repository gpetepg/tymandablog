Linode Deployment
=================

Place ``tymandablog`` in ``/etc/nginx/sites-enabled/``

I use ``pip`` for supervisor not apt-get so you can place ``supervisord.conf`` in the ``ve`` or virtual environment directory or in ``/etc/supervisord/``

- ``sudo ufw allow http/tcp``
- ``sudo ufw delete allow 5000``
- ``sudo ufw enable``
- ``sudo systemctl restart nginx``
