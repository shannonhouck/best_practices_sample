from distutils.core import setup
  
setup(
    name='sample',
    version='0.1.0',
    author='Shannon E. Houck',
    author_email='shouck@vt.edu',
    packages=['sample', 'sample.test'],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='Sample package.',
    long_description=open('README.md').read(),
)

