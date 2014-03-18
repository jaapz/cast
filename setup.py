from setuptools import setup


setup(
    name='cast',
    version='0.1.1',
    license='MIT',
    url='https://github.com/jaapz/cast',
    author='Jaap Broekhuizen',
    author_email='jaapz.b@gmail.com',
    description='Command line utility to control your Google Chromecast.',
    py_modules=['cast'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    # PyChromecast is not yet pushed to PyPI so for now this next option will
    # not work.
    #install_requires=['pychromecast'],
    install_requires=['docopt'],
    entry_points={
        'console_scripts': [
            'cast = cast:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: POSIX'
    ]
)
