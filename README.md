
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
    heroku config:set BUILDPACK_URL=https://github.com/heroku/heroku-buildpack-python
    heroku config:set SECRET_KEY="wn4hujnbjhijrujhujhjzhzadfadf"
    heroku run python manage.py collectstatic --noinput
