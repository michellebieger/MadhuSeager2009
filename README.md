# MadhuSeager2009: a TauREx 3.1 plugin to replicate the Madhusudhan Seager 2009 temperature-pressure profile

## Requirements

- You will need a working installation of TauREx 3.1 on your machine or computer server, with associated required Python packages: https://taurex3-public.readthedocs.io/

## Installation

You can install _MadhuSeager2009_ by cloning this Github and installing via the terminal. This is done by:

Cloning the directory using:

```console
$ git clone https://github.com/michellebieger/MadhuSeager2009
```

Move into the downloaded folder:

```console
$ cd MadhuSeager2009
```

Install by then typing in:

```console
$ pip install .
```

You can check the installation by importing the plugin into Python:

```console
$ python -c "import MadhuSeager2009"
```

To check that TauREx 3.1 has correctly registered your plugin:

```console
$ taurex --plugins
```

If there are no errors, you have been successful!

## License

Distributed under the terms of the [GPL 3.0 license][license],
_MadhuSeager2009_ is free and open source software.

## Issues

If you encounter any problems, please email michellebieger@live.com with a detailed description of the issue.
