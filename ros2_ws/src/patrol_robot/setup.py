from setuptools import find_packages, setup

package_name = 'patrol_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/patrol_robot/launch', ['patrol_robot/launch/patrol.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='190371040+Ivenson17@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'move_forward = patrol_robot.move_forward:main',
            'patrol_node = patrol_robot.patrol_node:main', 
        ],
    },
)
