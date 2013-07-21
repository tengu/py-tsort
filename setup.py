from setuptools import setup
# a workaround for a gross bug: http://bugs.python.org/issue15881#msg170215
try: 
    import multiprocessing
except ImportError: 
    pass
    
setup(
    name="tsort",
    version="0.0.1",
    # defer to tsort(1) for commandline use.
    #entry_points=
    py_modules=['tsort'],
    license = "LGPL",
    description = "topological sort",
    long_description="Topologically sort vertices in a DAG. Useful for dependency resolution.",
    author = "tengu",
    author_email = "karasuyamatengu@gmail.com",
    url = "https://github.com/tengu/py-tsort",
    classifiers = [
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Environment :: Console",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities", 
        ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
