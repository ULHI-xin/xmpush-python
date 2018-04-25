from distutils.core import setup

kw = dict(
    name='xmpush-python',
    version='1.0.3',
    description='Python3 xiaomi push sdk',
    author='hatevol',
    author_email='hatevol@gmail.com',
    url='https://github.com/ULHI-xin/xmpush-python',
    packages=['xmpush', 'xmpush.base'],
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])

setup(**kw)
