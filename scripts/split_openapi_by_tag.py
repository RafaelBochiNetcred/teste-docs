#!/usr/bin/env python3
import argparse
import copy
import re
from pathlib import Path

import yaml


REF_RE = re.compile(r"#/components/schemas/([^\"'\]\)\s]+)")


def collect_schema_refs(value):
    refs = set()

    if isinstance(value, dict):
        ref = value.get("$ref")
        if isinstance(ref, str):
            match = REF_RE.search(ref)
            if match:
                refs.add(match.group(1))

        for nested in value.values():
            refs.update(collect_schema_refs(nested))

    elif isinstance(value, list):
        for nested in value:
            refs.update(collect_schema_refs(nested))

    elif isinstance(value, str):
        refs.update(REF_RE.findall(value))

    return refs


def expand_schema_refs(components, initial_refs):
    schemas = components.get("schemas", {})
    refs = set(initial_refs)
    pending = list(initial_refs)

    while pending:
        name = pending.pop()
        schema = schemas.get(name)
        if schema is None:
            continue

        for nested_ref in collect_schema_refs(schema):
            if nested_ref not in refs:
                refs.add(nested_ref)
                pending.append(nested_ref)

    return refs


def filter_paths_by_tag(paths, tag):
    filtered_paths = {}

    for path, path_item in paths.items():
        filtered_item = {}

        for method, operation in path_item.items():
            if method.startswith("x-") or method == "parameters":
                filtered_item[method] = copy.deepcopy(operation)
                continue

            if tag in operation.get("tags", []):
                filtered_item[method] = copy.deepcopy(operation)

        operation_keys = [
            key for key in filtered_item
            if not key.startswith("x-") and key != "parameters"
        ]
        if operation_keys:
            filtered_paths[path] = filtered_item

    return filtered_paths


def split_openapi_by_tag(source, tag, output):
    with source.open() as source_file:
        document = yaml.safe_load(source_file)

    paths = filter_paths_by_tag(document.get("paths", {}), tag)
    refs = collect_schema_refs(paths)
    refs = expand_schema_refs(document.get("components", {}), refs)

    components = copy.deepcopy(document.get("components", {}))
    schemas = components.get("schemas", {})
    components["schemas"] = {
        name: schema for name, schema in schemas.items() if name in refs
    }

    tags = [
        item for item in document.get("tags", [])
        if item.get("name") == tag
    ]

    filtered = {
        "openapi": document.get("openapi", "3.0.3"),
        "info": copy.deepcopy(document.get("info", {})),
        "paths": paths,
        "components": components,
    }
    if tags:
        filtered["tags"] = tags

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w") as output_file:
        yaml.safe_dump(
            filtered,
            output_file,
            allow_unicode=True,
            sort_keys=False,
        )


def main():
    parser = argparse.ArgumentParser(
        description="Create a focused OpenAPI document containing one tag."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("tag")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    split_openapi_by_tag(args.source, args.tag, args.output)


if __name__ == "__main__":
    main()
