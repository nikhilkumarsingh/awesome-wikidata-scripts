# awesome-wikidata-scripts

Awesome Wikidata SPARQL Scripts

To learn about Wikidata and SPARQL, check out these [notes](https://github.com/nikhilkumarsingh/awesome-wikidata-scripts/blob/main/wikidata.ipynb)


## How to run?

1. Save SPARQL query to `scripts` directory. Every script can have a list of params which are of the format `${n}` where `n` is a non-negative integer. 
   Example:
    ```
    # Returns all the descendants of a person.
    # Params:
    # 1. person id (example: Q1001)

    SELECT ?descendant ?descendantLabel
    WHERE{
      ?descendant (wdt:P25|wdt:P22)+ wd:${0}.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ```


2. Run:
  ```bash
  $ python3 query_runner.py <script-name> <param-1> <param-2> ... <param-n>
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
