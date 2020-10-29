Prerequisites
-------------

* Install `discoparset` (see the `discoparset` directory) as well as `discodop`
* (Remember to use the corresponding discoparset conda environment)
* Install `produce` (`pip install produce`)

Reproduction
------------

To run the experiment without BERT:  
```bash
produce data/dev.plain.eval
```
With BERT:
```bash
produce data/dev.bert.eval
```
