# MadhuSeager2009: a TauREx 3.1 plugin to replicate the Madhusudhan Seager 2009 temperature-pressure profile

## Requirements

- You will need a working installation of TauREx 3.1 on your machine or computer server, with associated required Python packages: https://taurex3-public.readthedocs.io/

## Installation

You can install _MadhuSeager2009_ with PyPi:

```console
pip install taurex-madhuseager2009
```

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

## Usage

You can use the ExampleNotebook in the repository, which runs this PT profile with TauREx as a forward model in a Jupyter Notebook. You can further modify the Notebook and include retrievals if desired.

To use the MadhuSeager2009 PT profile in a `.par` file and run TauREx on a command line, you can call the profile with either the keywords 'MadhuSeager2009' or 'madhuseager2009' under the "[Temperature]" parameter:

```console
$ profile_type = MadhuSeager2009
```

An example `.par` file exists in this repository with all the parameters relevant to this PT profile--just add in your desired values/further parameters as normal when using TauREx and any other TauREx plugins.

## License

Distributed under the terms of the [GPL 3.0 license][license],
_MadhuSeager2009_ is free and open source software.

## Issues

If you encounter any problems, please email michellebieger@live.com with a detailed description of the issue.
