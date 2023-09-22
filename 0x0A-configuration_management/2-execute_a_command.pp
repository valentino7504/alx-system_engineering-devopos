# kills a process
exec { 'killmenow':
  path    => '/bin',
  command => 'pkill killmenow'
}
