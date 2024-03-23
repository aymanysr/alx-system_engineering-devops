#this code kills a process and works together with killmenow file which has been provided
exec { 'install_flask':
    command =>  '/usr/bin/pip3 install Flask==2.1.0',
    path    =>  ['/usr/bin'],
    unless  =>  '/usr/bin/flask --version | grep -q "Flask 2.1.0"',
}