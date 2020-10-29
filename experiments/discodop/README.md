# Main experiment

The parameter file of the main experiment can be found in `main-exp.prm`.  It
is based on the officially distributed parameter file of the [Tiger
grammar](https://staff.fnwi.uva.nl/a.w.vancranenburgh/grammars/).

### Prerequisites

* `discodop`
* `produce`

### Reproduction

Run:
```bash
produce
```
This will produce the evaluation statistics in the following file:
* `main-exp/dev.eval` (for development set)
* `main-exp/test.eval` (for test set)

The experiment can be reproduced using the following command (assuming
`discodop` is installed on the system):
```
discodop runexp main-exp.prm
```

To tag the test set:
```
discodop treetransforms ../data/data_for_discodop/test_for_discodop.export --inputfmt=export --sentid --outputfmt=tokens | discodop parser --sentid --fmt=export main-exp/ > main-exp/dop.test.export
```


### Results

The result of the experiment can be found in the `main-exp` directory.
In particular:
* `export.dop`: dev set parsed with the extracted grammar
* `export.test.dop`: test set parsed with the extracted grammar

### Evaluation

To evaluate the test set:
```
discodop eval --functions=leave ../data/data_for_discodop/test_for_discodop.export main-exp/dop.test.export discodop_evaluation/evalparam.prm
```
You can also use `--disconly` to evaluate the discintinuous constituents only.
```
discodop eval --functions=leave --disconly ...
```


# Other experiments

Files for other experiments can be found in `obsolete-experiments`.
