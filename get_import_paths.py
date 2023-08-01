import inspect
import shapely

method_name = "is_prepared"

def find_method_in_module(module, method_name):
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            # Check if the class has the method
            if hasattr(obj, method_name):
                # Get the method
                method = getattr(obj, method_name)
                return method

# Search for the method in the module
method = find_method_in_module("shapely", method_name)

if method:
    print(f"Method '{method_name}' found in class '{method.__self__.__class__.__name__}'.")
    # Call the method if needed
    method()
else:
    print(f"Method '{method_name}' not found in any class within the module.")
