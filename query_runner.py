import re
import sys

from SPARQLWrapper import SPARQLWrapper, JSON
from tabulate import tabulate

WIKIDATA_ENDPOINT = "https://query.wikidata.org/sparql"
DUMMY_USER_AGENT = "XYZ/3.0"


def load_query(script_name, params):
    """
    Loads SPARQL query with given `script_name` from the "scripts" directory and substitutes the query
    placeholders with given `params` list.
    Note: Pass the `script_name` without ".txt" suffix.
    """
    query = open(f"scripts/{script_name}.txt", "r").read()
    return substitute_query_params(query, params)


def substitute_query_params(query, params):
    """
    Substitutes the placeholders of the format ${n} (where n is a non-negative integer) in the query. Example, ${0}.
    ${n} is substituted with params[n] to generate the final query.
    """
    placeholders = re.findall("((\${)(\d+)(}))", query)
    for placeholder in placeholders:
        placeholder_str, placeholder_index = placeholder[0], placeholder[2]
        value = params[int(placeholder_index)]
        query = query.replace(placeholder_str, value)
    return query


def print_tabular_results(results):
    table = []
    for result in results['results']['bindings']:
        row = {}
        for key, value in result.items():
            row[key] = value['value']
        table.append(row)
    print(tabulate(table, headers="keys"))


def get_results(query):
    sparql_call = SPARQLWrapper(WIKIDATA_ENDPOINT, returnFormat=JSON, agent=DUMMY_USER_AGENT)
    sparql_call.setQuery(query)
    return sparql_call.queryAndConvert()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        script_name = sys.argv[1]
        params = sys.argv[2:] if len(sys.argv) > 2 else []
        results = get_results(load_query(script_name, params))
        print_tabular_results(results)
