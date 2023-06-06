from setuptools import setup, find_packages

setup(
    name='db_rsk_pred',
    version='0.1.0',
    author='gupo',
    python_requires='>=3.8',  # python版本必须>=3.8
    packages=find_packages(),  # ['db_rsk_pred'],  自动找到该路径下的所有package
    install_requires=['pandas==1.5.3', 'lightgbm==3.3.3',
                      'python-configuration', 'PyMySQL',
                      'tqdm', 'numpy==1.23.5',
                      'optuna', 'shap==0.41.0', 'numba==0.56.4',
                      'schedule', 'fastapi', 'uvicorn']
)
