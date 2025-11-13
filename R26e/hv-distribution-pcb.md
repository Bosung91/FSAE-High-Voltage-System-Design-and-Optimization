# HV Distribution PCB

## Design
<p style='text-align: justify'>
Purpose of HV Distribution PCB is to provide branched HV paths to systems that require HV. FSAE rule EV.6.6.6 states that lower stream conductors with lower ampacity must be fused.
</p>
<center><img src='../Figures/Rules_Overcurrent Protection.png'></center>
<center><i>Figure 27: FSAE Rule EV.6.6.6</i></center>

<p style='text-align: justify'>
Schematic designed for HV Distribution is shown in <i>Figure 28</i>, which mainly consists of connectors, fuses and resistors.
</p>
<center><img src='../Figures/HV Distribution PCB Schematic.png'></center>
<center><i>Figure 28: 26 HV Distribution PCB Schematic</i></center>

HV Distribution PCB provides HV to the following systems:
- Precharge-Discharge PCB
- IMD
- TSMP
- Voltage Indicator
- Ready to Move PCB
- MSD

<center>
<style type="text/css">
.tg  {border-collapse:collapse;border-color:#ccc;border-spacing:0;}
.tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:0px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:0px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-1wig">No</th>
    <th class="tg-1wig">Port</th>
    <th class="tg-1wig">Voltage / V</th>
    <th class="tg-1wig">Resistance / Ohm</th>
    <th class="tg-1wig">Current / A</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">Pre ACC+</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">1500</td>
    <td class="tg-0lax">0.22</td>
  </tr>
  <tr>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">IMD+</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">1.2e+6</td>
    <td class="tg-0lax">2.75e-4</td>
  </tr>
  <tr>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">IMD-</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">1.2e+6</td>
    <td class="tg-0lax">2.75e-4</td>
  </tr>
  <tr>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">Pre VEH+</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">1500</td>
    <td class="tg-0lax">0.22</td>
  </tr>
  <tr>
    <td class="tg-0lax">5</td>
    <td class="tg-0lax">Dis VEH+</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">1500</td>
    <td class="tg-0lax">0.22</td>
  </tr>
  <tr>
    <td class="tg-0lax">6</td>
    <td class="tg-0lax">EM+</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">11e+3</td>
    <td class="tg-0lax">30e-3</td>
  </tr>
  <tr>
    <td class="tg-0lax">7</td>
    <td class="tg-0lax">TSMP+</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">10e+3</td>
    <td class="tg-0lax">0.033</td>
  </tr>
  <tr>
    <td class="tg-0lax">8</td>
    <td class="tg-0lax">Volt IND+</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">15e+3</td>
    <td class="tg-0lax">20e-3</td>
  </tr>
  <tr>
    <td class="tg-0lax">9</td>
    <td class="tg-0lax">RTM+</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">2.25e+6</td>
    <td class="tg-0lax">1.47e-4</td>
  </tr>
  <tr>
    <td class="tg-0lax">10</td>
    <td class="tg-0lax">MSD-</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">1500</td>
    <td class="tg-0lax">0.22</td>
  </tr>
  <tr>
    <td class="tg-0lax">11</td>
    <td class="tg-0lax">Dis VEH-</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">1500</td>
    <td class="tg-0lax">0.22</td>
  </tr>
  <tr>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">TSMP-</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">10e+3</td>
    <td class="tg-0lax">0.033</td>
  </tr>
  <tr>
    <td class="tg-0lax">13</td>
    <td class="tg-0lax">Volt IND-</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">15e+3</td>
    <td class="tg-0lax">20e-3</td>
  </tr>
  <tr>
    <td class="tg-0lax">14</td>
    <td class="tg-0lax">RTM-</td>
    <td class="tg-0lax">330</td>
    <td class="tg-0lax">2.25e+6</td>
    <td class="tg-0lax">1.47e-4</td>
  </tr>
</tbody></table>
</center>
<center><i>Figure 29: HV Distribution System Requirements</i></center>

<p style='text-align: justify'>
Based on the system requirements shown in <i>Figure 29</i> and EV.6.6.6, fuses are added only for systems without explicit overcurrent protection. The systems that require overcurrent protection are: IMD, Energy Meter, Voltage Indicator and Ready to Move PCB.
</p>

### Fuse Selection
#### Current
_Show AWG22 ampacity (3A ~ 5A) & fuse average time current curves_

#### Material
_Compare different fuse materials, such as glass, ceramic, etc_

#### Form Factor
_Cylindrical, SMD, Blade, etc_

## Prototyping
_Vertical mounting to prevent water accumulation if there is water ingress in TB enclosure, highlight Hirose Df63 series connector, easily replaceable fuse, conformal coating_

---

[Previous Section: R26E: Tractive Battery PDM PCB](tractive-battery-pdm.md)

[Next Section: Shortcomings](../shortcomings.md)  

[List of Abbreviations](list-of-abbrev.md)