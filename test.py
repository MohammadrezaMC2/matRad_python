from dataclasses import dataclass, field
from typing import List, Union
import os


def is_meta_class(obj):
    """Check if the object is a meta class object (as in MATLAB's `meta.class`)"""
    # Placeholder for meta-class validation. Replace as needed.
    return hasattr(obj, '__class__')


@dataclass
class MatRadFindSubclassesInput:
    superClass: Union[str, object]  # Can be a string or a meta-class object
    packages: List[Union[str, object]] = field(
        default_factory=list)  # List of packages (strings or meta.package objects)
    folders: List[str] = field(default_factory=list)  # List of folder paths (strings)
    includeAbstract: bool = False  # Boolean flag to include abstract classes
    includeSubfolders: bool = False  # Boolean flag to include subfolders
    usePath: bool = False  # Boolean flag to use path

    def __post_init__(self):
        # Validate `superClass`
        if not isinstance(self.superClass, str) and not is_meta_class(self.superClass):
            raise ValueError("`superClass` must be a string or a meta-class object.")

        # Validate `packages`
        if not isinstance(self.packages, list) or not all(
                isinstance(pkg, str) or is_meta_class(pkg) for pkg in self.packages
        ):
            raise ValueError("`packages` must be a list of strings or meta-class objects.")

        # Validate `folders`
        if not isinstance(self.folders, list) or not all(
                isinstance(folder, str) and os.path.isdir(folder) for folder in self.folders
        ):
            raise ValueError("`folders` must be a list of valid folder paths.")

        # Validate `includeAbstract`
        if not isinstance(self.includeAbstract, bool):
            raise ValueError("`includeAbstract` must be a boolean.")

        # Validate `includeSubfolders`
        if not isinstance(self.includeSubfolders, bool):
            raise ValueError("`includeSubfolders` must be a boolean.")

        # Validate `usePath`
        if not isinstance(self.usePath, bool):
            raise ValueError("`usePath` must be a boolean.")


# Example Usage:
def find_subclasses(superClass: Union[str, object], **kwargs):
    try:
        # Parse inputs using the dataclass
        input_data = MatRadFindSubclassesInput(superClass=superClass, **kwargs)
        print(f"Validated input: {input_data}")

        # Perform subclass finding logic here (this part is just an example)
        # For now, let's return a mock result
        class_list = ["SubClass1", "SubClass2", "SubClass3"]
        return class_list

    except ValueError as e:
        print(f"Input error: {e}")
        return []


# Example 1: Valid input
result = find_subclasses('BaseClass', packages=['pkg1', 'pkg2'], folders=['/path/to/folder'], includeAbstract=True,
                         usePath=False)
print(result)  # Expected output: ['SubClass1', 'SubClass2', 'SubClass3']

# Example 2: Invalid input (invalid folder)
result = find_subclasses('BaseClass', packages=['pkg1'], folders=['/invalid/path'], includeAbstract=False)
# Expected output: Input error: `folders` must be a list of valid folder paths.

# Example 3: Invalid input (incorrect superClass type)
result = find_subclasses(123, packages=['pkg1'])
# Expected output: Input error: `superClass` must be a string or a meta-class object.
