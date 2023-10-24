import pprint
pp = pprint.PrettyPrinter(indent=4)

"""
1. Allt är dictionaries!
2. Varför är print() alltid tillgänglig? dir(__builtins__)
3. Global Namespace. globals()
4. Local namesapce. locals()
5. nonlocal för nästlade funktioner
6. global för local-scope
7. LGB
"""

def enclosing_function():
    var = "value"

    def nested_function():
        var = "new_value"

    nested_function()
    print(var)

enclosing_function()