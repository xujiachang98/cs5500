import json

# Subclass of JSONEncoder
class ExtendedEncoder(json.JSONEncoder):
    def default(self, obj):
        # Custom serialization for complex numbers
        if isinstance(obj, complex):
            return {'__complex__': True, 'real': obj.real, 'imag': obj.imag}
        # Custom serialization for range objects
        if isinstance(obj, range):
            return {'__range__': True, 'start': obj.start, 'stop': obj.stop, 'step': obj.step}
        return super().default(obj)

# Subclass of JSONDecoder
class ExtendedDecoder(json.JSONDecoder):
    def decode(self, s):
        obj = super().decode(s)
        # Custom deserialization for complex numbers
        if '__complex__' in obj:
            return complex(obj['real'], obj['imag'])
        # Custom deserialization for range objects
        if '__range__' in obj:
            return range(obj['start'], obj['stop'], obj['step'])
        return obj

def dumps(obj, **kwargs):
    return json.dumps(obj, cls=ExtendedEncoder, **kwargs)

def loads(s, **kwargs):
    return json.loads(s, cls=ExtendedDecoder, **kwargs)
