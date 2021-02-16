from json import JSONEncoder

def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default

class JsonSerializable(object):
    def to_json(that):
        return that.camel_cased_keys()

    def camel_cased_keys (that):
        newDict = {}
        for key in list(that.__dict__.keys()):
            newDict[that.to_camel_case(key)] = that.__dict__[key]
        return newDict
    
    def to_camel_case(that, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])
