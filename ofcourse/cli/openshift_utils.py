import pkg_resources
      install_requires=['ofcourse>={version}'],
     )""".format(version=pkg_resources.get_distribution('ofcourse').version),