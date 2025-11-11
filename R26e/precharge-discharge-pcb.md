# Precharge-Discharge PCB

## Design
### Rules
<p style='text-align: justify'>
FSAE rule sections EV.5.6 and EV.7.2.2 highlighted in red in <i>Figure 15</i> govern the design of Precharge-Discharge PCB
</p>

<center><img src='../Figures/Rules_Precharge-Discharge PCB.png'></center>
<center><i>Figure 15: FSAE Rules EV.5.6 & EV.7.2.2</i></center>

### Schematic
<p style='text-align: justify'>
Based on the rules and lessons learned from R25Evo, the following schematic has been designed as shown in <i>Figure 16</i>.
</p>

<center><img src='../Figures/26 Precharge-Discharge PCB Schematic.png'></center>
<center><i>Figure 16: 26 Precharge-Discharge PCB Schematic</i></center>

### Components
#### Diodes (D1~D6)
<p style='text-align: justify'>
Surge diodes are connected in anti-parallel to either relay coils, contacts or solid state relay (SSR) diode to protect them from inductive load.
</p>

#### MOSFET (Q1, Q3, Q4, PMOS2)
<p style='text-align: justify'>
MOSFETs are used to control the analogue logic of the board. Refer to <i>Figure 14</i> for the logic of the board.
</p>

#### Capacitor (C1)
<p style='text-align: justify'>
Capacitor is added to stabilise transient response of the entire circuit whenever IR+ coil is energised.
</p>

#### RC Circuits (C2 & R5, C3 & R6)
<p style='text-align: justify'>
RC circuits are implemented to vary opening of relays when there is a fault. RC time constant for C2 and R5 is lower than that of C3 and R6 to ensure IRs open first whatever happens to Precharge Relay. Discharge Relay closes first, IRs open next, then Precharge Relay stays open. 
</p>

<p style='text-align: justify'>
For C2 and R5, this ensures IRs open as quickly as possible by drawing any residual current away from G6DN1ALDC24 coil (pins 1 & 2) to GND.
</p>

<p style='text-align: justify'>
For C3 and R6, this prevents accidental closure of Precharge Relay when gate voltage to PMOS2 falls below its gate threshold voltage due to removal of 12V and presence of SDC_IN.
</p>

## Simulation
_Content_

## Transient Analysis
_Content_

## Prototyping
_Content_

---

[Previous Section: R25Evo](../R25evo/r25evo.md)

[Next Section: R26E: Tractive Battery PDM PCB](tractive-battery-pdm.md)  

[List of Abbreviations](list-of-abbrev.md)