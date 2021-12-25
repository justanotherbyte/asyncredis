from setuptools import setup, find_packages

with open('requirements.txt',  'r') as f:
    requirements = f.read().splitlines()


with open('README.md', encoding='utf-8') as f:
    readme = f.read()


setup(
    name='asyncredis',
    author='justanotherbyte',
    python_requires='>=3.7.0',
    url='https://github.com/justanotherbyte/asyncredis',
    version="0.3.0",
    packages=find_packages(),
    license='GNU',
    description='An asyncio compatible Redis driver. Just a pet-project.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)