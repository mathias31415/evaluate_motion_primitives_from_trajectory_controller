from setuptools import find_packages, setup

package_name = 'evaluate_motion_primitives_from_trajectory_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(include=[
        'evaluate_motion_primitives_from_trajectory_controller',
        'evaluate_motion_primitives_from_trajectory_controller.*'
    ]),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
    ],
    zip_safe=True,
    maintainer='Mathias Fuhrer',
    maintainer_email='mathias.fuhrer@b-robotized.com',
    description='Package to evaluate trajectory that is approximated using motion primitives',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'record_moprim_from_traj_data = evaluate_motion_primitives_from_trajectory_controller.record_moprim_from_traj_data:main',
            'compare = evaluate_motion_primitives_from_trajectory_controller.compare:main',
        ],
    },
)
