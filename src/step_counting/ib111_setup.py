import inspect
import turtle, typing, math, fractions, gzip, http.client, re, zipfile, io, glob, sys, csv, datetime, calendar, json, shutil, os, sqlite3, random

from .utils.methods import get_class_methods

from .patch.patching import create_patch

from .ignor import ignored_object_methods

allow = {
    turtle: {
        'forward',
        'backward',
        'right',
        'left',
        'setheading',
        'done',
        'speed',
        'delay',
        'penup',
        'pendown',
    },
    typing: {
        'Annotated',
    },
    math: {
        'pi',
        'acos',
        'cos',
        'asin',
        'sin',
        'atan',
        'atan2',
        'tan',
        'sqrt',
        'isqrt',
        'degrees',
        'radians',
        'trunc',
        'floor',
        'ceil',
        'isclose',
        'gcd',
        'lcm',
        'factorial',
    },
    fractions: {
        'Fraction',
    },
    gzip: {'open'},
    http.client: {'HTTPSConnection', 'HTTPConnection'},
    re: {'findall', 'match', 'compile', 'sub', 'search'},
    zipfile: {'ZipFile', 'is_zipfile'},
    io: {'BytesIO'},
    glob: {'glob'},
    sys: {'stdin', 'stdout', 'stderr', 'argv'},
    csv: {'reader', 'writer', 'DictReader'},
    datetime: {'date', 'datetime', 'timedelta', 'time'},
    calendar: {'monthrange'},
    json: {'load', 'loads', 'dump', 'dumps'},
    shutil: {'rmtree', 'copyfile'},
    os: {
        'path',
        'remove',
        'getcwd',
        'mkdir',
        'listdir',
        'makedirs',
        'chdir',
        'scandir',
        'rmdir',
        'rename',
    },
    sqlite3: {'connect'},
    random: {
        'Random',
        'seed',
        'randint',
        'random',
        'shuffle',
        'choice',
        'sample',
    },
}


def decorate_all_methods_in_module(module, decorator):
    for name, obj in inspect.getmembers(module, predicate=inspect.isclass):
        for name, fn in inspect.getmembers(obj, predicate=inspect.isfunction):
            if name not in ignored_object_methods:
                create_patch(
                    module,
                    obj.__name__,
                    name,
                    decorator(fn, obj, name),
                )

    for name, obj in inspect.getmembers(module, predicate=inspect.isroutine):
        create_patch(module, None, name, decorator(obj, module, name))


def setup_ib111_modules(decorator):
    for module, object_names in allow.items():
        for obj_name in object_names:
            obj = getattr(module, obj_name)
            if inspect.ismodule(obj):
                decorate_all_methods_in_module(obj, decorator)
            if inspect.isclass(obj):
                for method_name in get_class_methods(obj):
                    if method_name in ignored_object_methods:
                        continue

                    method = getattr(obj, method_name)
                    create_patch(
                        module,
                        obj_name,
                        method_name,
                        decorator(method, obj, method_name),
                    )
            elif inspect.isroutine(obj):
                create_patch(module, None, obj_name, decorator(obj, module, obj_name))
