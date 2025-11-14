# Precharge-Discharge PCB

## Design
### Schematic
<p style='text-align: justify'>
Based on the rules (Figure 7) and lessons learned from R25Evo, the following schematic has been designed as shown in <i>Figure 17</i>.
</p>

<center><img src='../Figures/26 Precharge-Discharge PCB Schematic.png'></center>
<center><i>Figure 17: 26 Precharge-Discharge PCB Schematic</i></center>

<br>

### Components
### LV
#### Diodes (D1~D6)
<p style='text-align: justify'>
Surge diodes are connected in anti-parallel to either relay coils, contacts or solid state relay (SSR) diode to protect them from inductive load.
</p>

#### MOSFET (Q1, Q3, Q4, PMOS2)
<p style='text-align: justify'>
MOSFETs are used to control the analogue logic of the board. Refer to <i>Figure 15</i> for the logic of the board. PMOS is used to control Precharge Relay due to its simpler gate drive requirements for high-side switching.
</p>

#### Capacitor (C1)
<p style='text-align: justify'>
Capacitor is added to stabilise transient response of the entire circuit whenever IR+ coil is energised.
</p>

#### RC Circuits (C2 & R5, C3 & R6)
<p style='text-align: justify'>
RC circuits are implemented to vary opening time of relays when <b>there is a fault</b>. RC time constant for C2 and R5 is lower than that of C3 and R6 to ensure IRs open first whatever happens to Precharge Relay. Discharge Relay closes first, IRs open next, then Precharge Relay stays open. 
</p>

<p style='text-align: justify'>
For C2 and R5, IRs will open as quickly as possible by drawing any residual current away from G6DN1ALDC24 coil (pins 1 & 2) to GND when 12V is removed.
</p>

<p style='text-align: justify'>
For C3 and R6, accidental closure of Precharge Relay is avoided when gate voltage to PMOS2 falls below its gate threshold voltage due to removal of 12V and presence of SDC_IN, since gate voltage slowly discharges.
</p>

#### Resistors
<p style='text-align: justify'>
Majority of resistors are current-limiting except R4, which is a pull-down for Precharge signal.
</p>

#### Connector
<p style='text-align: justify'>
Hirose DF63 series PCB through-hole 6-pin connector rated for 630VDC and 6A is used.
</p>

### HV
#### Relays
<p style='text-align: justify'>
SSR is used for Discharge Relay, while electromechanical relay is used for Precharge Relay.
</p>

#### Resistors
<p style='text-align: justify'>
Non-inductive and high power TO-247 1.5kOhms resistor is used for Discharge and Precharge each.
</p>

#### Heat Sink
<p style='text-align: justify'>
TO-247 compatible aluminium heat sink is directly mounted to the resistors for effective cooling. Refer to <a href='#' target='_blank'>Appendix #</a> for calculations behind selecting the heat sink.
</p>

#### Metal Oxide Varistor (MOV)
<p style='text-align: justify'>
MOV is used to protect Discharge Relay from output spike voltages due to inductance.
</p>

#### Connectors
<p style='text-align: justify'>
Hirose DF63 series PCB through-hole 2-pin connectors rated for 630VDC and 8A are used.
</p>

## Simulation
<p style='text-align: justify'>
Falstad simulation has been set up to validate the functionality of the schematic as shown in <i>Figure 18</i>.
</p>
<center><img src='../Figures/Falstad_Precharge-Discharge.png'></center>
<center><i>Figure 18: <a href='https://tinyurl.com/2cjbjfbx' target='_blank'>Precharge-Discharge PCB Simulation</a></i></center>

<br>

<p style='text-align: justify'>
<i>Figure 19</i> shows all possible scenarios of Precharge-Discharge PCB functionality.
</p>
<center>
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-266k{background-color:#9b9b9b;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">S1</th>
    <th class="tg-0pky">S2</th>
    <th class="tg-0pky">S3</th>
    <th class="tg-0pky">S4</th>
    <th class="tg-0pky">Remarks</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">Precharge Signal</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky" rowspan="2">0: LOW<br>1: HIGH</td>
  </tr>
  <tr>
    <td class="tg-0pky">Shutdown OK</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">1</td>
  </tr>
  <tr>
    <td class="tg-266k" colspan="6"></td>
  </tr>
  <tr>
    <td class="tg-0pky">Precharge Relay</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky" rowspan="4">0: Open<br>1: Closed</td>
  </tr>
  <tr>
    <td class="tg-0pky">Discharge Relay</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">0</td>
  </tr>
  <tr>
    <td class="tg-0pky">AIR+</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">0</td>
  </tr>
  <tr>
    <td class="tg-0pky">AIR-</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">1</td>
    <td class="tg-0pky">0</td>
    <td class="tg-0pky">1</td>
  </tr>
</tbody></table>
</center>
<center><i>Figure 19: Precharge-Discharge PCB Truth Table</i></center>

<br>

## Transient Analysis
<p style='text-align: justify'>
R25Evo testing exposed insufficient cooling by heat sinks, which led to failure of Precharge resistors. Transient analysis has been conducted on Precharge resistor to determine whether peak power during transient state will exceed its maximum power rating. <i>Figure 20</i> shows power against time plot of Precharge resistor.
</p>
<center><img src='../Figures/Altium SPICE_Precharge Resistor P-t Plot.png'></center>
<center><i>Figure 20: P vs t Plot of Precharge Resistor</i></center>

<br>

The findings are as under:
- Peak Power: 86.0W
- Average Power: 10.8W

<p style='text-align: justify'>
The peak power is lower than the resistor maximum power rating of 100W, and the average power dissipated is in the same order of magnitude as Electric Systems Form (ESF) value of 18.2W; ESF is a document that the team needs to submit for technical inspection prior to competition. <i>Figure 21</i> shows the Precharge segment of ESF. Detailed analysis setup and data extraction are in <a href='#' target='_blank'>Appendix #</a>.
</p>
<center><img src='../Figures/ESF Precharge Segment.png'></center>
<center><i>Figure 21: ESF Precharge Segment</i></center>

<br>

<p style='text-align: justify'>
Detailed calculations behind ESF are shown in <a href='#' target='_blank'>Appendix #</a>.
</p>

## Prototyping
<p style='text-align: justify'>
Based on the schematic, specced components and simulation results, 26 Precharge-Discharge PCB has been prototyped as shown in <i>Figure 22</i>.
</p>
<center><img src='../Figures/26 Precharge-Discharge PCB Front View.png'></center>
<center><i>Figure 22: 26 Precharge-Discharge PCB</i></center>

<br>

<p style='text-align: justify'>
Humiseal 1B73 conformal coat is applied to ensure electrical isolation from surrounding components and to keep galvanic isolation spacing to a minimum of 4 mm as stated in FSAE rules EV.6.5.7. It is mounted vertically to prevent water accumulation on it in case there is water ingress in TB enclosure.
</p>
<center><img src='../Figures/EV.6.5.7.png'></center>
<center><i>Figure 23: EV.6.5.7</i></center>

---

[Previous Section: R25Evo](../R25evo/r25evo.md)

[Next Section: R26E: Tractive Battery PDM PCB](tractive-battery-pdm.md)  

[List of Abbreviations](../list-of-abbrev.md)