# Set up my SSH config file
file_line { 'specify file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school'
}
file_line { 'etc/ssh_config':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no'
}

