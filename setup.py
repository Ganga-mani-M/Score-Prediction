from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='ScorePrediction',
version='0.0.1',
author='Ganga mani',
author_email='gangamani15@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)

# from setuptools import find_packages, setup
# from typing import List

# def get_requirements(file_path: str) -> List[str]:
#     """
#     Returns a list of requirements from a file
#     """
#     with open(file_path, 'r') as f:
#         requirements = f.read().splitlines()  # removes \n automatically
#     # Remove editable install if present
#     requirements = [req for req in requirements if not req.startswith('-e')]
#     return requirements

# setup(
#     name='scoreprediction',
#     version='0.0.1',
#     author='ganga mani',
#     author_email='gangamani15@gmail.com',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')  # fixed filename
# )


# from setuptools import find_packages, setup
# from typing import List


# def get_requirements(file_path : str) ->List[str] :
#     '''
#     this function will return the list of requirments 

#     '''
#     requirements = []
#     with open(file_path) as file_obj:
#          requirements = file_obj.readlines()
#          requirements[req.replace("\n","" ) for req in requirements]

#          if HYPEN_E_DOT in requirements:
#             requirements.remove(HYPEN_E_DOT)

#     return requirements      

# setup (
#     name = 'scoreprediction',
#     version = '0.0.1',
#     author ='ganga mani',
#     author_email = 'gangamani15@gmail.com',
#     packages = find_packages(),
#     install_requires = get_requirements('requirements.txt')
# )
