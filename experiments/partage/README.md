Prerequisites
-------------

#### ParTAGe Supertagger

```bash
pip install -r requirements.txt
```
You might need to additionally install [disco-dop][discodop-install].

### ParTAGe for TWG

Install [Haskell Stack](https://docs.haskellstack.org/en/stable/README/), then:
```bash
git submodule update --init --recursive partage-twg
cd partage-twg
stack install
```
<!--
```bash
git clone https://github.com/kawu/partage-twg.git
cd partage-twg
stack install
```
-->

See also the [partage installation instructions][partage-install].


Reproduction
------------

Run:
```bash
produce
```


[partage-install]: https://github.com/kawu/partage-twg/tree/internal-wrapping-dev#installation "ParTAGe for TWG installation instructions"
[discodop-install]: https://github.com/andreasvc/disco-dop#installation "DiscoDOP installation"
