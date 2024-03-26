#this code creates a file named school inside the /tmp directory
file { '/tmp/school':
  ensure  =>  file,
  content =>  'I love Puppet',
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
}
