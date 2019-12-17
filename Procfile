web: gunicorn app:app --log-file=-
web: gunicorn -b 0.0.0.0:$PORT app:app
web: gunicorn app:app
web: gunicorn run:app
log.Fatal(http.ListenAndServe(":" + os.Getenv("PORT"), router))
web: gunicorn gettingstarted.wsgi --log-file -
