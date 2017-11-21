from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='message_wiper_ng',
    version='0.0.1',
    description='MessageWiperNG',
    long_description=readme(),
    url='https://github.com/resurtm/message_wiper_ng',
    download_url='https://github.com/resurtm/message_wiper_ng/archive/v0.0.1.tar.gz',
    author='resurtm',
    author_email='resurtm@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['message_wiper_ng'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'telethon',
    ],
)
