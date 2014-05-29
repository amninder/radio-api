from techops.fab.django import *

# env comes from fab.api. It's a <class 'fabric.utils._AttributeDict'>
env.project = 'radio'
env.proxy_project = 'to' # techops.cmich.edu proxies to apartments
env.url_name = 'radio'
env.site = 'techops.cmich.edu-radio'
env.chronograph = False
env.south = False
env.django_version = 1.5
env.user = 'techopsadmin'


# Note that hosts should be defined as IP addresses, so that they can be passed to nginx config
def test(rev='tip'):
    env.hosts = ['10.209.28.106']
    env.settings_file = 'settings_test'
    env.debug = True
    env.rev = rev
    env.filepath = '/tmp/{proj}-{rev}.tgz'.format(proj=env.project, rev=env.rev)

def spock(rev='tip'):
    env.hosts = ['141.209.28.104']
    env.settings_file = 'settings_production'
    env.debug = True
    env.rev = rev
    env.filepath = '/tmp/{proj}-{rev}.tgz'.format(proj=env.project, rev=env.rev)

def khan(rev='tip'):
    env.hosts = ['141.209.28.105']
    env.settings_file = 'settings_production'
    env.debug = True
    env.rev = rev
    env.filepath = '/tmp/{proj}-{rev}.tgz'.format(proj=env.project, rev=env.rev)
