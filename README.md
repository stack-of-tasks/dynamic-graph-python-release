dynamic-graph-python
====================

[![Building Status](https://travis-ci.org/stack-of-tasks/dynamic-graph-python.svg?branch=master)](https://travis-ci.org/stack-of-tasks/dynamic-graph-python)
[![Pipeline status](https://gitlab.laas.fr/stack-of-tasks/dynamic-graph-python/badges/master/pipeline.svg)](https://gitlab.laas.fr/stack-of-tasks/dynamic-graph-python/commits/master)
[![Coverage report](https://gitlab.laas.fr/stack-of-tasks/dynamic-graph-python/badges/master/coverage.svg?job=doc-coverage)](http://projects.laas.fr/stack-of-tasks/doc/stack-of-tasks/dynamic-graph-python/master/coverage/)

Python bindings for dynamic-graph.


**Warning:** this repository contains [Git
submodules][git-submodules]. Please clone this repository using the
`git clone --recursive` command. If you already have cloned the
repository, you can run `git submodule init && git submodule update`
to retrieve the submodules.


Documentation
-------------

To get started with this library, please read the [online Doxygen
documentation][doxygen-documentation].

It can also be generated locally by running the `make doc`
command. After the package is installed, the documentation will be
located in the `$prefix/share/doc/dynamic-graph` directoy where
`$prefix` is your installation prefix (`/usr/local` by default).


Getting Help
------------

Support is provided through:
 * the HPP mailing-list: hpp@laas.fr
 * the following HipChat room: http://www.hipchat.com/gh4wQrZeV


How can I install dynamic-graph?
--------------------------------

### Installing dependencies

The matrix abstract layer depends on several packages which
have to be available on your machine.

 - Libraries:
   - [Boost][] (>= 1.40)
     Its detection is controled by the `BOOST_ROOT` variable, see next section
     for more information.
   - [Lapack][] library
     Use the generic purpose `CMAKE_CXX_FLAGS` and `CMAKE_EXE_LINKER_FLAGS`
     to insert the flags required for the compiler to find your Lapack library
     if it is installed in a non-standard directory.
   - [jrl-mal][] library
   - [dynamic-graph][] library
 - System tools:
   - [CMake][] (>=2.6)
   - [pkg-config][]
   - usual compilation tools (GCC/G++, make, etc.)
     If you are using Ubuntu, these tools are gathered in the `build-essential` package.



### Compiling and installing the package

The manual compilation requires two steps:

 1. configuration of the build and generation of the build files
 2. compilation of the sources and installation of the package

dynamic-graph uses [CMake][] to generate build files. It is
recommended to create a separate build directory:

```sh
mkdir _build         # (1) Create a build directory
cd _build            # (2) Go to the newly created build directory
cmake [options] ..   # (3) Generate the build files
```

Options which can be passed to CMake are detailed in the next section.

```sh
make                 # (4) Compile the package
make test            # (5) Execute the package tests
make install         # (6) Install the package into the prefix (see step 3)
```


### Options

Additional options can be set on the command line through the
following command: `-D<option>=<value>`.

For instance: `cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..` will set
the `CMAKE_BUILD_TYPE` option to the value `RelWithDebInfo`.


Available options are:

- `CMAKE_BUILD_TYPE` set the build profile that should be used (debug,
  release, etc.). We recommend `RelWithDebInfo` as it will provide
  performances while keeping debugging symbols enabled.
- `CMAKE_INSTALL_PREFIX` set the installation prefix (the directory
  where the software will be copied to after it has been compiled).


### Running the test suite

The test suite can be run from your build directory by running:

```sh
   make test
```

Please open a ticket if some tests are failing on your computer, it
should not be the case.

Credits
-------

This package authors are credited in the [AUTHORS](AUTHORS) file.
