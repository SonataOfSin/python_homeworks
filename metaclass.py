import types

class MethodNameValidatorMeta(type):
    def __new__(mcs, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if attr_name.startswith('__') and attr_name.endswith('__'):
                continue
                
            if isinstance(attr_value, (types.FunctionType, types.MethodType)) or callable(attr_value):
                if not attr_name.startswith('_'):
                    raise ValueError(
                        f"validation error: class method names '{attr_name}' "
                        f"it should start with an underscore!"
                    )
        
        return super().__new__(mcs, name, bases, dct)