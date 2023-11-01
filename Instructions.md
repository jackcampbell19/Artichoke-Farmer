# Compressed Instruction Definition
Each instruction consists of an instruction byte (`inst` byte) and a subsequent series of parameter bytes depending on the `inst` byte.

The `inst` byte consists of a code and flag, each 4 bits in size.

| Instruction Code | Instruction Flag |
| :----------------: | :----------------: |
| 4 bits (`0-3`) | 4 bits (`4-7`) |

The code defines the instruction type, and the flag allows for additional information to be provided. The null flag is simply zeroed out.
# Available Instructions

### `home`
* Calibrates the machines home coordinate.
* Instruction Code: `0000`
* Instruction Flag: `null`
* Total Bytes: `1`
* Example: `home`

### `move` `x y z optional(e)`
* Moves the machine to the specified coordinates.
* Instruction Code: `0001`
* Instruction Flag: Speed ramp curve selection
  * `0000`: Ease-In-Out
  * `0001`: Linear
* Parameters:
  * `x`: 2 bytes
  * `y`: 2 bytes
  * `z`: 2 bytes
  * `e`: 4 bits (used for flag)
* Total Bytes: `7`
* Example: `move 1400 200 3145` or `move 1400 200 3145 1`

### `tool` `i`
* Performs a tool change and selects the tool at the specified index.
* Instruction Code: `0010`
* Instruction Flag: Tool index (as 4 bit integer)
* Total Bytes: `1`
* Example: `tool 3`

### `shift` `x y z optional(e)`
* Moves the machine relatively by the amount specified.
* Instruction Code: `0011`
* Instruction Flag: Speed ramp curve selection
  * `0000`: Ease-In-Out
  * `0001`: Linear
 * Parameters:
  * `x`: 2 bytes (1 bit for sign, 15 bits for int)
  * `y`: 2 bytes (1 bit for sign, 15 bits for int)
  * `z`: 2 bytes (1 bit for sign, 15 bits for int)
  * `e`: 4 bits (used for flag)
* Total Bytes: `7`
* Example: `shift -200 0 100`

### `cup` `i`
* Positions the painting cup in the given position.
* Instruction Code: `0100`
* Instruction Flag: Position
  * `0000`: Retracted
  * `0001`: Middle
  * `0010`: Extended
* Total Bytes: `1`
* Example: `cup 1`

### `paint` `b c m y k optional(r)`
* Dispensed paint into the paint cup. Will exchange the cup if required.
* Instruction Code: `0101`
* Instruction Flag: Retain cup?
  * `0000`: Exchange cup
  * `0001`: Retain cup
* Parameters:
  * `b`: Base (white) quantity, 2 bytes
  * `c`: Cyan quantity, 2 bytes
  * `m`: Magenta quantity, 2 bytes
  * `y`: Yellow quantity, 2 bytes
  * `k`: Black quantity, 2 bytes
  * `r`: 4 bits (used for flag)
* Total Bytes: `11`
* Example: `paint 1200 23 35 3 0 1`


