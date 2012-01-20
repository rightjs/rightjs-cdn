#
# A simple scripts building and reorganizing tools
#
# Copyright (C) 2011 Nikolay Nemshilov
#

import os
import re
import sys

# hooking up the google stuff to use templates
sys.path.append('google_appengine')
sys.path.append('google_appengine/lib')
sys.path.append('google_appengine/lib/webob')

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext.webapp import template

BUILD_DIR   = 'app/builds'
DOMAIN_NAME = 'http://cdn.rightjs.org'


def get_version_num(filename):
    """ Parses out the version number out of the file"""
    file = open(filename)
    head = file.read(100)
    file.close()

    return re.search(r'(\d+\.\d+\.\d+)', head).group(0)


def make_latest_link(category, name):
    """ Makes the latest version sym-link """

    directory = '%s/%s' % (BUILD_DIR, category)

    versions = [
        re.search(r'(\d+\.\d+\.\d+)', version).group(1) for version in os.listdir(directory)
            if re.match(re.compile('^'+name+'\-(\d+\.\d+\.\d+)\.js$'), version)
    ]

    versions.sort()
    versions.reverse()
    version = versions[0]

    os.system('rm %s/%s.js &> /dev/null' % (directory, name))
    os.system('cd %s; ln -s %s-%s.js %s.js' % (directory, name, version, name))


def build_core():
    print "== Creating Core Builds =========================================="
    os.system('mkdir -p %s/core' % BUILD_DIR)


    print " - Making a standard build"
    os.system('cd rightjs/core; nake build OPTIONS=no-olds &>/dev/null')
    version = get_version_num('rightjs/core/build/right.js')
    os.system('cp rightjs/core/build/right.js %s/core/right-%s.js' % (BUILD_DIR, version))
    os.system('cp rightjs/core/build/right-olds.js %s/core/right-olds-%s.js' % (BUILD_DIR, version))

    print " - Making the safe-mode build"
    os.system('cd rightjs/core; nake build:safe &>/dev/null')
    os.system('cp rightjs/core/build/right-safe.js %s/core/right-safe-%s.js' % (BUILD_DIR, version))

    print " - Making the latest links"
    make_latest_link('core', 'right')
    make_latest_link('core', 'right-olds')
    make_latest_link('core', 'right-safe')


def build_plugins():
    print "== Building The Plugins =========================================="
    print " - Building scripts"
    os.system('mkdir -p %s/plugins' % BUILD_DIR)
    os.system('cd rightjs/plugins; nake build &>/dev/null')

    print " - Moving modules in place"
    for script in os.listdir('rightjs/plugins/build'):
        if script.endswith('.js') and not script.endswith('-src.js'):
            module = re.match(r'right\-(.+?)\.js', script).group(1)
            print '   + ' + module.capitalize()

            version = get_version_num('rightjs/plugins/build/%s' % script)
            os.system('cp rightjs/plugins/build/%s %s/plugins/%s-%s.js' % (script, BUILD_DIR, module, version))
            make_latest_link('plugins', module)



def build_ui():
    print "== Building UI Modules ==========================================="
    print " - Building scripts"
    os.system('mkdir -p %s/ui' % BUILD_DIR)
    os.system('cd rightjs/ui; nake build &>/dev/null')

    print " - Moving modules in place"
    for script in os.listdir('rightjs/ui/build'):
        if script.endswith('.js') and not script.endswith('-src.js'):
            module = re.match(r'right\-(.+?)\.js', script).group(1)
            print '   + ' + module.capitalize()

            version  = get_version_num('rightjs/ui/build/%s' % script)
            filename = '%s/ui/%s-%s.js' % (BUILD_DIR, module, version)
            os.system('cp rightjs/ui/build/%s %s' % (script, filename))

            # patching depending images location
            file = open(filename, 'r')
            content = file.read()
            file.close()

            match = re.search(r':url\(.+?\/([^\/]+?\.png)\)', content)
            if match:
                content = content.replace(match.group(0), ':url(%s/img/%s)' % (DOMAIN_NAME, match.group(1)))

                file = open(filename, 'w')
                file.write(content)
                file.close()

            make_latest_link('ui', module)


    print " - Copying images in place"
    os.system('mkdir -p %s/img' % BUILD_DIR)
    for image in os.listdir('rightjs/ui/img'):
        if image.endswith('.png') and os.path.exists('%s/ui/%s.js' % (BUILD_DIR, image[0:-4])):
            os.system('cp rightjs/ui/img/%s %s/img/' % (image, BUILD_DIR))

    print " - Copying i18n modules"
    os.system('rm -rf %s/i18n' % BUILD_DIR)
    os.system('mkdir -p %s/i18n' % BUILD_DIR)
    os.system('cp rightjs/ui/i18n/*.js %s/i18n' % BUILD_DIR)



def build_index():
    print "== Building The Index File ======================================="

    print ' - Reading the files'
    modules = {}

    for key in ['core', 'plugins', 'ui']:
        print '   + '+ key
        modules[key] = {}

        for filename in os.listdir('%s/%s' % (BUILD_DIR, key)):
            match = re.search(r'^(.+?)\-(\d+\.\d+\.\d+)\.js', filename)
            if match:
                module  = match.group(1)
                version = match.group(2)

                if not module in modules[key]:
                    modules[key][module] = []

                modules[key][module].append(version)

        for module in modules[key]:
            modules[key][module].sort()
            modules[key][module].reverse()

        if key == 'plugins' or key == 'ui':
            modules[key] = modules[key].items()
            modules[key].sort()

    modules['i18n'] = []
    for name in os.listdir('%s/i18n' % BUILD_DIR):
        modules['i18n'].append(name[0:-3])
    modules['i18n'].sort()

    print ' - Building index.html'
    file = open('app/static/index.html', 'w')
    file.write(template.render('app/index.html', {
        'core':    modules['core']['right'],
        'safe':    modules['core']['right-safe'],
        'plugins': modules['plugins'],
        'ui':      modules['ui'],
        'i18n':    modules['i18n']
    }))
    file.close()



if __name__ == '__main__':
    build_core()
    build_plugins()
    build_ui()
    build_index()