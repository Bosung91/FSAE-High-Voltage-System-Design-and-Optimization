# HV Distribution PCB

## Design
<p style='text-align: justify'>
Purpose of HV Distribution PCB is to provide branched HV paths to systems that require HV. FSAE rule EV.6.6.6 states that lower stream conductors with lower ampacity must be fused.
</p>
<center><img src='../Figures/Rules_Overcurrent Protection.png'></center>
<center><i>Figure 29: FSAE Rule EV.6.6.6</i></center>

<br>

<p style='text-align: justify'>
Schematic designed for HV Distribution is shown in <i>Figure 29</i>, which mainly consists of connectors, fuses and resistors.
</p>
<center><img src='../Figures/HV Distribution PCB Schematic.png'></center>
<center><i>Figure 30: 26 HV Distribution PCB Schematic</i></center>

<br>

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
<center><i>Figure 31: HV Distribution System Requirements</i></center>

<br>

<p style='text-align: justify'>
Based on the system requirements shown in <i>Figure 29</i> and EV.6.6.6, fuses are added only for systems without external overcurrent protection. The systems that require overcurrent protection are: IMD, Energy Meter, Voltage Indicator and Ready to Move PCB.
</p>

### Fuse Selection
#### Current
<p style='text-align: justify'>
AWG 22 wires are used for the systems that require overcurrent protection, and the ampacity is shown in <i>Figure 32</i> below.
</p>
<center>
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-0lax" colspan="6"><span style="font-weight:bolder">AMPACITY CHART</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:bolder">AWG</span></td>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:bolder">Mili-Ohms /FT</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:bolder">35º C Rise</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:bolder">10º C Rise</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:bolder">Amps</span></td>
    <td class="tg-0lax"><span style="font-weight:bolder">Max Feet</span></td>
    <td class="tg-0lax"><span style="font-weight:bolder">Amps</span></td>
    <td class="tg-0lax"><span style="font-weight:bolder">Max Feet</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">2</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">0.0156</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">100</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">44</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">54</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">83</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">4</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">0.249</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">72</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">39</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">40</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">70</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">6</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">0.395</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">54</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">33</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">30</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">59</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">8</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">0.628</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">40</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">28</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">20</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">55</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">10</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">1</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">30</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">23</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">15</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">47</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">12</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">1.59</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">20</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">22</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">12.5</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">35</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">14</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">2.53</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">15</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">18</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">10</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">28</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">16</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">4.01</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">12.5</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">14</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">7</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">25</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">18</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">6.39</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">10</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">11</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">5</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">22</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">20</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">10.2</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">7</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">10</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">4</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">17</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">22</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">16.1</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">5</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">7</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">3</span></td>
    <td class="tg-0lax"><span style="background-color:var(--bs-table-bg)">15</span></td>
  </tr>
</tbody></table>
</center>
<center><i>Figure 32: Amapcity Chart of Milspec Wires (<a href='https://www.prowireusa.com/tefzel-amperage-chart' target='_blank'>PROWIREUSA, 2025</a>)</i></center>

<br>

<p style='text-align: justify'>
The team anticipates only a 10ºC rise, so the fuse needs to be rated for 3A. Littelfuse axial lead and cartridge fuse average time current curves are shown below, which will be referenced to select the fuse.
</p>

<center><img src='../Figures/Fuse_T vs I plot.png'></center>
<center><i>Figure 33: Average Time Current Curves (<a href='https://drive.google.com/file/d/1TmnjSHS8LeXFVinmKBrlm3u4hg1fqOzP/view?usp=sharing' target='_blank'>Littelfuse, 2018</a>)</i></center>

<br>

<p style='text-align: justify'>
Littelfuse is the sponsor for the team, and it offers cartridge fuses with 3 different ratings only as shown in <i>Figure 33</i>. Based on the options available, 1A fuse is chosen as it has the highest current rating. Based on the system requirements and AWG 22 wire ampacity, 1A fuse rating is high enough to allow normal operation and low enough to protect the wire from overcurrent.
</p>

#### Form Factor
<p style='text-align: justify'>
Cartridge and blade fuses are common for automotive applications, but for FSAE electric race car, cartridge fuse has been chosen according to criteria shown in <i>Figure 34</i>.
</p>
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
    <th class="tg-1wig">Requirement</th>
    <th class="tg-1wig">Cartridge Fuse</th>
    <th class="tg-1wig">Blade Fuse</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax">HV rating</td>
    <td class="tg-0lax">✅ 1000 V</td>
    <td class="tg-0lax">❌ low-voltage only</td>
  </tr>
  <tr>
    <td class="tg-0lax">Interrupt rating</td>
    <td class="tg-0lax">✅ high (10kA)</td>
    <td class="tg-0lax">❌ low</td>
  </tr>
  <tr>
    <td class="tg-0lax">Thermal stability</td>
    <td class="tg-0lax">✅ good (MIL STD 202, Method 107)</td>
    <td class="tg-0lax">❌ limited</td>
  </tr>
  <tr>
    <td class="tg-0lax">Mechanical robustness</td>
    <td class="tg-0lax">✅ high (MIL STD 202, Method 201)</td>
    <td class="tg-0lax">❌ lower</td>
  </tr>
</tbody>
</table>
</center>
<center><i>Figure 34: Cartridge Fuse vs Blade Fuse</i></center>

## Prototyping
<center><img src='../Figures/HV Distribution PCB 3D.png'></center>
<center><i>Figure 35: 26 HV Distribution PCB</i></center>

<br>

<p style='text-align: justify'>
The PCB is vertically mounted to prevent water accumulation if there is water ingress in TB enclosure. Hirose DF63 series connectors are used to ensure stable wire harness connection, cartridge fuse holders are used for ease of fuse replacement, and Humiseal 1B73 conformal coating is applied for electrical insulation and moisture protection. <i>Figure 35</i> shows the 3D render of 26 HV Distribution PCB.
</p>

---

[Previous Section: R26E: Tractive Battery PDM PCB](tractive-battery-pdm.md)

[Next Section: Shortcomings](../shortcomings.md)  

[List of Abbreviations](../list-of-abbrev.md)