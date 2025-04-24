from setuptools import find_packages, setup 
from typing import List

HYPEHNE_E_DOT = '-e .'  
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file path.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEHNE_E_DOT in requirements:
            requirements.remove(HYPEHNE_E_DOT)  
        
        return requirements
setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Raksha',
    author_email = 'raksharaj.2683@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)  