from setuptools import setup, Extension, find_packages

# Define the extension module
patch_modules = \
[
    Extension('patchint', sources=['./src/step_counting/patch/c_modules/customint.c'], extra_compile_args=['-g', '-O0']),
    Extension('patchtuple', sources=['./src/step_counting/patch/c_modules/customtuple.c'], extra_compile_args=['-g', '-O0']),
    Extension('patchdictionary', sources=['./src/step_counting/patch/c_modules/customdict.c'], extra_compile_args=['-g', '-O0']),
    Extension('patchlist', sources=['./src/step_counting/patch/c_modules/customlist.c'], extra_compile_args=['-g', '-O0'])
]

# Run the setup
setup(
    name='CustomTuple',
    version='1.0',
    description='Python module to patch tuple operations',
    packages=find_packages('src/step_counting/patch/bin'),
    package_dir={'': 'src/step_counting/patch/bin'},
    ext_modules=patch_modules,
)
