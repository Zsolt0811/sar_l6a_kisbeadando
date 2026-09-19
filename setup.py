import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'sar_l6a_kisbeadando'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sárközi Zsolt Ferenc',
    maintainer_email='sarkozi.zsolt.ferenc@hallgato.sze.hu',
    description='Futószalag minőségellenőrző ROS 2 csomag',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'conveyor_node = sar_l6a_kisbeadando.conveyor_node:main',
            'inspector_node = sar_l6a_kisbeadando.inspector_node:main',
        ],
    },
)
