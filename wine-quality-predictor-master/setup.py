import setuptools

setuptools.setup(
    name='wqp',
    version='1.0.0',
    author='yazenwaked@gmail.com',
    description='Wine quality predictor - a packaged machine learning algorithm to predict wine quality',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn==1.5.0",
        "pandas==1.0.1"
    ]
)