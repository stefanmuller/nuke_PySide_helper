# nuke_PySide_helper
## subclassing QWidgets, so that values are stored on nuke nodes automagically


We can create PySide widgets on nodes through PyCustom_Knob. But the problem is, that the widgets get destroyed when the panel is closed and all values inserted into the widgets are lost.

As a proof of concept, I subclassed QLineEdit and added functionality, so that QWidgets are able to "remember" values via hidden native nuke knobs.
The idea is to create a helper module which subclasses all (or at least all important) QWidgets so that one can create beautiful PySide UIs without the need to worry about this limitation anymore.

Link to the discussion which led to this repository.
Thanks to everyone, especially Nick who suggested to subclass :) <br>
http://community.foundry.com/discuss/topic/137389/pyside-for-node-s-properties-ui


## Release notes

- PySide2 works only with Nuke 11, but I imported everything into the main namespace, so it should be possible to replace 'PySide2' with 'PySide' and it should work in older Nuke versions as well. (haven't tested that, though...)

### version 1.0.0
- proof of concept
- run QLineEditNuke_proof_of_concept.py in nuke's script editor