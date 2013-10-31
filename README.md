minimalKB
=========

![Screenshot of a minimalKB knowledge model viewed with oro-view](doc/oroview.jpg)

minimalKB is a SQLite-backed minimalistic knowledge base, initially designed
for robots (in particular human-robot interaction or multi-robot interaction).

It stores triples (like RDF/OWL triples), and provides a mostly conformant
[KB-API](http://homepages.laas.fr/slemaign/wiki/doku.php?id=kb_api_robotics)
API accessible via a simple socket protocol.

[pykb](https://github.com/severin-lemaignan/pykb) provides an idiomatic Python
binding, making easy to integrate the knowledge base in your applications.

It has almost no features, except it is fast and simple. Basic RDFS reasoning
is provided (cf below for details).

Written in Python. The only required dependency is `sqlite3`. If `rdflib` is
also available, you can easily import existing ontologies in RDF/OWL/n3/Turtle
formats in the knowledge base.

Installation
------------

```
$ git clone https://github.com/severin-lemaignan/minimalkb.git
$ cd minimalkb
$ python setup.py install
$ minimalkb
```

Run `minimalkb --help` for available options.

Features
--------

### Multi-models

The `minimalKB` is intended for dynamic environments, with possibly several
contexts/agents requiring separate knowledge models.

New models can be created at any time and each operation (like knowledge
addition/retractation/query) can operate on a specific subset of models.

### Reasoning

`minimalKB` only provides basic RDFS reasoning capabilities: it honors the
transitive closure of the `rdfs:subClassOf` relation.

The reasoner runs in its own thread, and classify the model at a given rate, by
default 5Hz. It is thus needed to wait ~200ms before the results of the
classification become visible in the model.

### Transient knowledge

`minimalKB` allows to attach 'lifespans' to statements: after a given duration,
they are automatically collected.

### Ontology walking

`minimalKB` exposes several methods to explore the different ontological models
of the knowledge base. It is compatible with the visualization tool
[oro-view](https://github.com/severin-lemaignan/oro-view).

