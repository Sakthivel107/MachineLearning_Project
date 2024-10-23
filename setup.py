from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    HYPEN_E_DOT="-e ."
    with open(file_path) as file_obj:
       requirements=file_obj.readlines()
       requirements=[ require.replace("\n","") for require in requirements ]
       if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)
       return requirements
setup(name="MachineLearning Projetcs",
      version="0.0.1",
      author="Sakthivel",
      author_email="sakthivel107g@gmail.com",
      packages=find_packages(),
      install_requirenmets=get_requirements('requirements.txt')


)




