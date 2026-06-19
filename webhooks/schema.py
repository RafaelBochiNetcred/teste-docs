def documented_endpoint(fn):
    fn.schema_documented = True
    return fn
