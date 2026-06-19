from django.conf import settings


def only_documented_endpoints(endpoints):
    if settings.DEBUG:
        return endpoints

    documented = []

    for path, path_regex, method, callback in endpoints:
        view_cls = getattr(callback, "cls", None)
        actions = getattr(callback, "actions", {})
        action_name = actions.get(method.lower())
        view_method = (
            getattr(view_cls, action_name, None)
            if view_cls and action_name
            else None
        )

        if getattr(view_method, "schema_documented", False):
            documented.append((path, path_regex, method, callback))

    return documented
