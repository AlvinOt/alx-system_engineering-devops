# Enable user holberton to login and open files without error

# Increase user holberton hard file limit
exec { 'incr-hard-file-limit-hbtn-usr':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase user holberton soft life limit
exec { 'incr-soft-file-limit-hbtn-usr':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
