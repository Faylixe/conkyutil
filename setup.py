from distutils.core import setup

setup(
    name = 'conkyutil',
    packages = ['conkyutil'],
    version = '0.2.1',
    description = 'Simple wrapper for interact with Conky through live script, or generating Conky text file.',
    author = 'Felix Voituret',
    author_email = 'felix.voituret@gmail.com',
    url = 'https://github.com/Faylixe/conkyutil',
    download_url = 'https://github.com/Faylixe/conkyutil/tarball/0.2.1',
    keywords = ['conky', 'wrapper'],
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Utilities'
    ]
)
