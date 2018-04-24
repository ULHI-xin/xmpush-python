from distutils.core import setup
from xmpush.base.APIConstants import Constants

kw = dict(
    name='xmpush-python',
    version=Constants.__VERSION__,
    description='xiaomi push python sdk',
    long_description=open('README.md', 'r').read(),
    author='mi_push',
    author_email='mipush-support@xiaomi.com',
    url='http://dev.xiaomi.com/mipush/downpage',
    download_url='http://dev.xiaomi.com/mipush/downpage',
    packages=['xmpush', 'xmpush.base'],
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
