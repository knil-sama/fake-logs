import pip
from distutils.core import setup

# new versions of pip requires a session
requirements = pip.req.parse_requirements(
    'requirements.txt', session=pip.download.PipSession()
)

for item in requirements:
    if getattr(item, 'link', None):  # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req)) # always the package name 


setup(name='fake-logs',
      version='1.0',
      description='Python server fake log generator',
      author='s4tori',
      url='https://github.com/s4tori/fake-logs',
      packages=['fake_logs'],
      install_requires=requires,
      dependency_links=links,
      scripts=['fake-logs.py']
)