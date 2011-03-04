GOOGLE_SDK_VERSION = 1.4.2
BUILDS_DIRECTORY   = app/builds
SOURCES_DIRECTORY  = rightjs

bootstrap:
	wget -c http://googleappengine.googlecode.com/files/google_appengine_$(GOOGLE_SDK_VERSION).zip
	unzip google_appengine_$(GOOGLE_SDK_VERSION).zip
	rm google_appengine_$(GOOGLE_SDK_VERSION).zip

update: clean download build

build:
	python app/build.py

clean:
	rm -rf $(SOURCES_DIRECTORY)

download:
	git clone --depth 1 -q git://github.com/rightjs/rightjs-core.git    $(SOURCES_DIRECTORY)/core
	git clone --depth 1 -q git://github.com/rightjs/rightjs-plugins.git $(SOURCES_DIRECTORY)/plugins
	git clone --depth 1 -q git://github.com/rightjs/rightjs-ui.git      $(SOURCES_DIRECTORY)/ui

server:
	python google_appengine/dev_appserver.py app/

deploy:
	python google_appengine/appcfg.py update app/