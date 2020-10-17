# awesome-wikidata-scripts

Awesome Wikidata SPARQL Scripts


## How to run?

1. Save SPARQL query to `scripts` directory.

2. Run:
  ```bash
  $ python3 query_runner.py <script-name> <optional-params>...
  ```

  Example:
  ```bash
  $ python3 query_runner.py descendants Q1001
  ```

  Output:
  ```
  {'head': {'vars': ['descendant', 'descendantLabel']}, 'results': {'bindings': [{'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q185403'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Ramdass Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q732728'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Devdas Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q1280678'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Manilal Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q1390715'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Harilal Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q100147817'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Sumitra Gandhi Kulkarni'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q734521'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Rajmohan Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q1595192'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Ramchandra Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q3347330'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Gopalkrishna Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q100146686'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Tara Gandhi Bhattacharjee'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q1324757'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Ela Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q3426281'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Arun Manilal Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q19664973'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Sonali Kulkarni'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q5625451'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Leela Gandhi'}}, {'descendant': {'type': 'uri', 'value': 'http://www.wikidata.org/entity/Q5625256'}, 'descendantLabel': {'xml:lang': 'en', 'type': 'literal', 'value': 'Tushar Gandhi'}}]}}
  ```
