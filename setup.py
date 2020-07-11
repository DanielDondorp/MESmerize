from setuptools import setup, find_packages


entry_points = {'console_scripts': ['mesmerize=mesmerize.__main__:main']}

install_requires = \
    [
        "cycler==0.10.0",
        "dask>=1.1.1",
        "future>=0.18.2",
        "h5py>=2.10.0",
        "ipykernel>=4.10",
        "ipython>=7.15.0",
        "ipyparallel>=6.3",
        "MarkupSafe>=1.1.1",
        "matplotlib>=3.2.2",
        "opencv-contrib-python>=4.2",
        "opencv-python>=4.2",
        "pandas~=0.25.3",  # do not change
        "Pillow>=5.4.1",
        "psutil~=5.7.0",
        "PyQt5>=5.9.2,<=5.12",
        "python-dateutil>=2.8.0",
        "QtPy>=1.6.0",
        "qtap",
        "scikit-image==0.17.2",  # do not change
        "scikit-learn>=0.20.2",  # do not change
        "scipy>=1.2.1",  # do not change
        "seaborn==0.9.0",  # do not change
        "spyder==3.3.3",  # do not change
        "tifffile",  # do not change
        "tqdm>=4.37.0",
        "PeakUtils",
        "tables>=3.6.1",
        "joblib>=0.15.1",
        #"tslearn~=0.2.2",  # had to remove because of windows
        "graphviz>=0.13",
        "numba>=0.50.0",
        "bottleneck==1.2.1",  # do not change
        "holoviews",
        "jupyter",
        "pynwb",
        "pyqtgraph",
        "tensorflow~=1.15",  # do not change
        "tk",  # do not change
        "tcl",
        "yapf"
    ]

classifiers = \
    [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Intended Audience :: Science/Research"
    ]

with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name='mesmerize',
    version='0.2.15',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    entry_points=entry_points,
    url='https://github.com/kushalkolar/MESmerize',
    license='GNU General Public License v3.0',
    author='Kushal Kolar, Daniel Dondorp',
    author_email='kushalkolar@gmail.com',
    description='Calcium imaging analysis platform',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    python_requires='~=3.6,<3.7',
    install_requires=install_requires
)
