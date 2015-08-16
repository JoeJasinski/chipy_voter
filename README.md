
# INSTALL

Install system requirements

    aptitude install nodejs

Install python requirements

    cd chipy_voter/
    pip install -r requirements.txt

Install node requirements

	cd chipy_voter/
    npm install


# BUILD ASSETS

Compile SASS

    ./node_modules/.bin/gulp sass

Collectstatic

    ./manage.py collectstatic


# DEVELOPMENT

Automatically detect changes to sass or react js and livereload

    ./node_modules/.bin/gulp

Install or update bower packages in the 'static/vendor' dir

    bower install

Copy .envs.example to .envs and edit:

    cp .envs.example .envs

Migrate the database

    ./manage.py migrate

# HEROKU DEPLOYMENT

    git push heroku master
    heroku addons:create heroku-postgresql:hobby-dev
    heroku config:set BUILDPACK_URL=https://github.com/heroku/heroku-buildpack-python
    heroku config:set SECRET_KEY="wn4hujnbjhijrujhujhjzhzadfadf"
    heroku config:set DATABASE_URL="postgres://USER:PASS@HOST:5432/DB"
    heroku config:set SOCIAL_AUTH_TWITTER_KEY=""
    heroku config:set SOCIAL_AUTH_TWITTER_SECRET=""
    heroku run python manage.py collectstatic --noinput
    heroku run python manage.py migrate
    heroku run python manage.py createsuperuser
