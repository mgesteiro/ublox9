# ublox9
**u-blox generation 9** GNSS receivers handling library.

Based on the [ZED-F9P (u-blox F9 high precision GNSS receiver)
documentation](https://www.u-blox.com/en/docs/UBX-18010854).

This is a **work in progress** project, as I'm implementing what I need
along the way. My goal is to keep it as simple and clean as possible, while
being as close to the specification as possible too. Everything is related
to the official document with links to specific pages/sections in comments
(see [ubxdefs.py](ublox9/ubxdefs.py) for examples).

## EXAMPLE

As easy as it gets:

```python
# dump u-blox gen9 module messages

import serial
from ublox9 import ublox9stream

sport = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
ub9stream = ublox9stream.Ublox9Stream(sport)

for message in ub9stream:
    print(message)
```

You can parse **UBX messages** too:  *(beware: not all implemented yet ...)*

```python
# parse u-blox gen9 module UBX messages

from ublox9 import ublox9stream, ubxmessage

message = ub9stream.read_ubxmessage()
print( UBXMessage.parse_bytes(message) )
```


## INSTALL
`pip install https://github.com/mgesteiro/ublox9/archive/main.zip`

## LICENSE
This work is licensed under the [GNU Affero General Public License v3.0](LICENSE).

More information about licenses in [Opensource licenses](https://opensource.org/licenses/) and [Creative Commons licenses](https://creativecommons.org/licenses/).
