from setuptools import find_packages, setup

setup(
  name='blahblah',
  version='0.6.1',
  description='Fake data generator for district42 schema',
  url='https://github.com/nikitanovosibirsk/blahblah',
  author='Nikita Tsvetkov',
  author_email='nikitanovosibirsk@yandex.com',
  license='MIT',
  packages=find_packages(),
  install_requires=[
    'district42==0.6.2',
    'exrex==0.9.4'
  ],
  dependency_links=[
    'https://github.com/nikitanovosibirsk/district42/tarball/3c2b823322ef874b9540beccb2fcefb4938bb161#egg=district42-0.6.1'
  ]
)
