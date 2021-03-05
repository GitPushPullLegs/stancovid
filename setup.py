from setuptools import setup

setup(
    name="stancovid",
    version="0.0.1",
    description="Used to gather COVID data from the Stanislaus COVID Dashboard.",
    url="https://github.com/GitPushPullLegs/stancovid",
    author="Joe Aguilar",
    author_email="Jose.Aguilar.6694@gmail.com",
    license="GNU General Public License",
    packages=["stancovid"],
    install_requires=["requests"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)