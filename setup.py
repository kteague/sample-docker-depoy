import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    ]

setup(name='sample-docker-deploy',
      version='1.0dev',
      description='Build the sample-app into a Docker image',
      long_description=README + '\n\n' + CHANGES,
      author='Kevin Teague',
      author_email='kevin@bud.ca',
      url='',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      entry_points="""\
      [console_scripts]
      build_docker_image = deploy:main
      """,
)
