
from setuptools import setup, find_packages
  
# reading long description from file 
with open('DESCRIPTION.txt') as file: 
    long_description = file.read() 
  
  
# specify requirements of your package here 
REQUIREMENTS = [
'certifi==2022.12.7',
'pygame==1.9.6'
] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 2 - Pre-Alpha', 
    'Intended Audience :: Developers', 
    'Topic :: Internet', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.3', 
    'Programming Language :: Python :: 3.4', 
    'Programming Language :: Python :: 3.5', 
    ] 
  
# calling the setup function  
setup(name='raceUP', 
      version='1.0.0', 
      description='2D car racing game based on pygame', 
      long_description="interesting game", 
      url='https://github.com/deepak7376/raceUP', 
      author='Deepak Yadav', 
      author_email='dky.united@gmail.com', 
      license='MIT', 
      packages=find_packages(), 
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='car race pygame',
      include_package_data=True,
      zip_safe=False

      ) 


