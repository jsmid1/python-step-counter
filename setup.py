from setuptools import setup, Extension, find_packages


# Define the extension modules
patch_modules = [
    Extension(
        'src.step_counting.patch.bin.patchbytearray',
        sources=['./src/step_counting/patch/c_modules/custombytearray.c'],
        extra_compile_args=['-g', '-O0'],
    ),
    Extension(
        'src.step_counting.patch.bin.patchint',
        sources=['./src/step_counting/patch/c_modules/customint.c'],
        extra_compile_args=['-g', '-O0'],
    ),
    Extension(
        'src.step_counting.patch.bin.patchtuple',
        sources=['./src/step_counting/patch/c_modules/customtuple.c'],
        extra_compile_args=['-g', '-O0'],
    ),
    Extension(
        'src.step_counting.patch.bin.patchdictionary',
        sources=['./src/step_counting/patch/c_modules/customdict.c'],
        extra_compile_args=['-g', '-O0'],
    ),
    Extension(
        'src.step_counting.patch.bin.patchlist',
        sources=['./src/step_counting/patch/c_modules/customlist.c'],
        extra_compile_args=['-g', '-O0'],
    ),
    Extension(
        'src.step_counting.patch.bin.patchstr',
        sources=['./src/step_counting/patch/c_modules/customstr.c'],
        extra_compile_args=['-g', '-O0'],
    ),
]

# Run the setup
setup(
    name='stepcounter',
    version='1.0.6',
    description='Python step counter',
    author='Jan Šmíd',
    license='Apache License 2.0',
    packages=find_packages(),
    ext_modules=patch_modules,
    entry_points={'console_scripts': ['stepcounter = src.step_counter:main']},
    python_requires='>=3.10, <3.13',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
)
