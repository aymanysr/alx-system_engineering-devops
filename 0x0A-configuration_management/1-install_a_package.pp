#!/usr/bin/pup
# This code will install Flask and Werkzeug via pip3 with specific versions
package { 'flask':
    ensure  =>  '2.1.0',
    provider  =>  'pip3',
}

package { 'werkzeug':
    ensure  =>  '2.0.2', # adjust this version as needed
    provider  =>  'pip3',
}
