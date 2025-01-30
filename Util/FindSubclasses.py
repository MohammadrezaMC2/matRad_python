from dataclasses import dataclass, field
from typing import List, Union
import os

def is_meta_class(obj):
    return hasattr(obj, '__class__')


@dataclass
class FindSubClassesInput:
    super_class: Union[str, object]
    packages: List[Union[str, object]] = field(default_factory=list)
    folder: List[str] = field(default_factory=list)
    include_abstract: bool=False
    include_subfolder: bool=False
    use_path: bool=False


    def __post_init__(self):
        if not isinstance(self.super_class, str) and not is_meta_class(self.super_class):
            raise ValueError("'super_class' must be a string or meta-class object.")

        if not isinstance(self.packages, list) or not all(
          isinstance(pkg, str) or is_meta_class(pkg) for pkg in self.packages
        ):
            raise ValueError("'package' must be a list of strings or meta-class object")

        if not isinstance(self.include_abstract, bool):
            raise ValueError("'include_abstract' must be a boolean")

        if not isinstance(self.use_path, bool):
            raise ValueError("'use_path' must be a boolean")


def find_sub_classes(super_class: Union[str, object], **kwargs):
    p = FindSubClassesInput(super_class=super_class, **kwargs)
    print(f"Validated input: {p}")

    super_class = p.super_class
    packages = p.packages
    folders = p.folder
    include_abstract = p.include_abstract
    include_subfolders = p.include_subfolder
    use_path = p.use_path

    if isinstance(super_class, str):
        super_class = super_class.__class__.mro()

    add_path = None
    if use_path:
        pass
    else:
        add_path = []

    for folder in folders:
        if include_subfolders:
            pass
        else:
            add_path.append(folder)


    folders = add_path

    # if all(isinstance(y, meta.package) for y in packages)

    for folder in folders:
        if include_subfolders:
            add_path = [add_path, folder]
        else:
            add_path = [add_path, folder]



def get_classes_from_folder(folder, package_name=None):
    meta_class_list = []
    full_folder = None

    if folder:
        return

    if package_name is not None:
        full_folder = folder
    else:
        pass


































