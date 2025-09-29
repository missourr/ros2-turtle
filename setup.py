from setuptools import find_packages, setup

package_name = 'my_turtle_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='misara',
    maintainer_email='misara@todo.todo',
    description='ROS2 turtlesim shape drawing project',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "realturtle = my_turtle_package.realturtle:main",
            "turtle_commander = my_turtle_package.turtle_commander:main"
        ],
    },
)
