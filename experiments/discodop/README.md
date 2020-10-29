# Main experiment

The parameter file for the main experiment can be found in `main-exp.prm`.  It
is based on the officially distributed parameter file of the [Tiger
grammar](https://staff.fnwi.uva.nl/a.w.vancranenburgh/grammars/).

### Prerequisites

Install:
* `discodop`
* `produce`

### Reproduction

Run:
```bash
produce
```
This will produce the following files, with the development and test set
evaluation results, respectively.
* `main-exp/dev.eval`
* `main-exp/test.eval`
