
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
