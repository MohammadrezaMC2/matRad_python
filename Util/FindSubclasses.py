from dataclasses import dataclass, field
from typing import List, Union
import os


def is_meta_class(obj):
    """
    Check if an object has a __class__ attribute, determining if it is a meta-class object.
    """
    return hasattr(obj, '__class__')


@dataclass
class FindSubClassesInput:
    """
    Data class to validate and store input parameters for finding subclasses.
    """
    super_class: Union[str, object]  # The base class or its name
    packages: List[Union[str, object]] = field(default_factory=list)  # List of packages to search
    folder: List[Union[str, object]] = field(default_factory=list)  # List of folders to search
    include_abstract: bool = False  # Whether to include abstract classes
    include_subfolder: bool = False  # Whether to include subfolders in search
    use_path: bool = False  # Whether to use file system paths in searching

    def __post_init__(self):
        """
        Validate input parameters after initialization.
        """
        if not isinstance(self.super_class, str) and not is_meta_class(self.super_class):
            raise ValueError("'super_class' must be a string or meta-class object.")

        if not isinstance(self.packages, list) or not all(
                isinstance(pkg, str) or is_meta_class(pkg) for pkg in self.packages
        ):
            raise ValueError("'packages' must be a list of strings or meta-class objects.")

        if not isinstance(self.include_abstract, bool):
            raise ValueError("'include_abstract' must be a boolean.")

        if not isinstance(self.use_path, bool):
            raise ValueError("'use_path' must be a boolean.")


def find_sub_classes(super_class: Union[str, object], **kwargs):
    """
    Find all subclasses of a given superclass based on specified criteria.

    :param super_class: The base class or its name.
    :param kwargs: Additional filtering parameters.
    :return: A list of discovered subclasses.
    """
    # Validate and extract parameters using the data class
    p = FindSubClassesInput(super_class=super_class, **kwargs)
    print(f"Validated input: {p}")

    # Extract values from the validated input
    super_class = p.super_class
    packages = p.packages
    folders = p.folder
    include_abstract = p.include_abstract
    include_subfolders = p.include_subfolder
    use_path = p.use_path

    # Resolve superclass if given as a string
    if isinstance(super_class, str):
        super_class = super_class.__class__.mro()

    # Determine path handling strategy
    add_path = None if use_path else []

    # Process folders based on whether subfolders should be included
    for folder in folders:
        if include_subfolders:
            pass  # Placeholder for logic to include subfolders
        else:
            add_path.append(folder)

    folders = add_path

    """
        Codes still need to be implemented
    """

    # Placeholder for additional class discovery logic
    class_list = []
    for folder in folders:
        class_list.append(get_classes_from_folder(folder=folder))

    return class_list


def get_classes_from_folder(folder, package_name=None):
    """
    Retrieve a list of class files from a specified folder.

    :param folder: The folder path to scan.
    :param package_name: (Optional) The package name associated with the folder.
    :return: A list of file names representing class definitions.
    """
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
