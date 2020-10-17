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
    descendant                                 descendantLabel
    -----------------------------------------  -------------------------
    http://www.wikidata.org/entity/Q185403     Ramdass Gandhi
    http://www.wikidata.org/entity/Q732728     Devdas Gandhi
    http://www.wikidata.org/entity/Q1280678    Manilal Gandhi
    http://www.wikidata.org/entity/Q1390715    Harilal Gandhi
    http://www.wikidata.org/entity/Q100147817  Sumitra Gandhi Kulkarni
    http://www.wikidata.org/entity/Q734521     Rajmohan Gandhi
    http://www.wikidata.org/entity/Q1595192    Ramchandra Gandhi
    http://www.wikidata.org/entity/Q3347330    Gopalkrishna Gandhi
    http://www.wikidata.org/entity/Q100146686  Tara Gandhi Bhattacharjee
    http://www.wikidata.org/entity/Q1324757    Ela Gandhi
    http://www.wikidata.org/entity/Q3426281    Arun Manilal Gandhi
    http://www.wikidata.org/entity/Q19664973   Sonali Kulkarni
    http://www.wikidata.org/entity/Q5625451    Leela Gandhi
    http://www.wikidata.org/entity/Q5625256    Tushar Gandhi
  ```
