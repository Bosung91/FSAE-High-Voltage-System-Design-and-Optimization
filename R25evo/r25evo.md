# R25Evo
<p style='text-align: justify'>
This section will discuss about the issues faced in the HV system during R25Evo test runs.
</p>

## Precharge Resistor
### Symptom
<p style='text-align: justify'>
R25Evo lost drive and could not start after power cycling. 
</p>

### Diagnosis
Precharge resistors on 25 Precharge-Discharge PCB completely melted down as shown in <i>Figure 7</i>, and it could be due to two possible reasons: 
- Under-specced resistor
- Insufficient heat dissipation by heat sink

<center><img src='../Figures/Burnt Precharge Resistors Top View.jpg'></center>
<center><i>Figure 7: Burnt Precharge Resistors</i></center>

### Under-specced resistor
<p style='text-align: justify'>
To determine whether overvoltage, overcurrent, or exceeding power limit or maximum operating temperature caused the meltdown, calculated values for those parameters were compared against datasheet values. One must take note that the datasheet assumes the resistors are properly heat sinked.
</p>

<center>
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Datasheet</th>
    <th class="tg-0pky">Actual</th>
    <th class="tg-0pky">Exceeded Datasheet?</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">Rated Power/W</td>
    <td class="tg-0pky">45</td>
    <td class="tg-0pky">7.212</td>
    <td class="tg-0pky">No</td>
  </tr>
  <tr>
    <td class="tg-0pky">Max Operating Temp/°C</td>
    <td class="tg-0pky">175</td>
    <td class="tg-0pky">150</td>
    <td class="tg-0pky">No</td>
  </tr>
  <tr>
    <td class="tg-0pky">Max Operating Current/A</td>
    <td class="tg-0pky">10</td>
    <td class="tg-0pky">0.223</td>
    <td class="tg-0pky">No</td>
  </tr>
  <tr>
    <td class="tg-0pky">Max Operating Voltage/V</td>
    <td class="tg-0pky">500</td>
    <td class="tg-0pky">333.75</td>
    <td class="tg-0pky">No</td>
  </tr>
</tbody>
</table>
</center>

<center><i>Figure 8: Parameter Comparison</i></center>
<p style='text-align: justify'>
Based on the comparison of parameters, resistor meltdown is <b>unlikely</b> due to underspeccing for R25Evo precharge circuit.  

Refer to <a href='#'>Appendix #</a> for calculations of actual parameters.
</p>

### Insufficient heat dissipation by heat sink
<p style='text-align: justify'>
After concluding that the resistors were specced properly, mechanical design of 25 Precharge-Discharge PCB was scrutinized. The following shows the layers comprising 25 Precharge-Discharge PCB in <i>Figure 9</i>.
</p>

<center><img src='../Figures/R25E Precharge-Discharge PCB Layer.png'></center>
<center><i>Figure 9: 25 Precharge-Discharge PCB Layers</i></center>
<p style='text-align: justify'>
There are a total of three <b>thermal insulators</b> making up the PCB layers: solder resist, PP-006 and FR-4. Their thermal conductivities are shown in <i>Figure 10</i>.
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
    <th class="tg-0lax">Material</th>
    <th class="tg-0lax">Thermal Conductivity / W/m/K</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax">Air</td>
    <td class="tg-0lax">0.0275</td>
  </tr>
  <tr>
    <td class="tg-0lax">Solder Resist (Solder Mask)</td>
    <td class="tg-0lax">0.245</td>
  </tr>
  <tr>
    <td class="tg-0lax">Prepreg (PP-006)</td>
    <td class="tg-0lax">0.4</td>
  </tr>
  <tr>
    <td class="tg-0lax">FR-4</td>
    <td class="tg-0lax">0.25</td>
  </tr>
  <tr>
    <td class="tg-0lax">Aluminium</td>
    <td class="tg-0lax">237</td>
  </tr>
</tbody>
</table>
</center>
<center><i>Figure 10: Thermal Conductivities of PCB Layers</i></center>

<p style='text-align: justify'>
As one can notice from <i>Figure 10</i>, placing heat sink on surface opposite to precharge resistors, as shown in <i>Figure 11</i> is <b>as ineffective as not placing the heat sink</b>, since the layers insulate heat generated from precharge resistors, preventing proper heat dissipation by the heat sink. Thus, the earlier comparison of datasheet and actual values is <b>invalid</b> since the resistors were not properly heat sinked.
</p>

<center><img src='../Figures/Burnt Precharge Resistors Side View.jpg'></center>
<center><i>Figure 11: Heat Sink Position</i></center>

<p style='text-align: justify'>
It can therefore be concluded with confidence that the precharge resistors melted down due to <b><u>insufficient heat dissipation during operation.</b></u>
</p>

## PCB board-to-wire Connectors
### Symptom
<p style='text-align: justify'>
R25Evo lost power intermittently mid drive.
</p>

### Diagnosis
<center><img src='../Figures/Precharge Signal_Abnormal.png'></center>
<center><i>Figure 12: Abnormal Precharge Signal</i></center>

<p style='text-align: justify'>
Precharge signal (blue graph) oscillated as shown in <i>Figure 12</i> due to <b><u>loose connection from 25 TB PDM to IR+.</b></u>
</p>

<center><img src='../Figures/Precharge Signal_Normal.png'></center>
<center><i>Figure 13: Normal Precharge Signal</i></center>

<p style='text-align: justify'>
The precharge signal state should be set as HIGH by ECU only when car is starting, then be set as LOW for the rest of the run as shown in <i>Figure 13</i>. Detailed precharge sequence is explained in <i>Figure 14</i> below.
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
    <th class="tg-8v2c" colspan="2">Logic</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-8v2c">1</td>
    <td class="tg-8v2c">Precharge relay is normally open, while discharge relay is normally closed</td>
  </tr>
  <tr>
    <td class="tg-8v2c">2</td>
    <td class="tg-8v2c">GLVMS on</td>
  </tr>
  <tr>
    <td class="tg-8v2c">3</td>
    <td class="tg-8v2c">Precharge relay closes &amp; Discharge relay opens</td>
  </tr>
  <tr>
    <td class="tg-8v2c">4</td>
    <td class="tg-8v2c">IR- closes</td>
  </tr>
  <tr>
    <td class="tg-8v2c">5</td>
    <td class="tg-8v2c">TSMS on</td>
  </tr>
  <tr>
    <td class="tg-8v2c">6</td>
    <td class="tg-8v2c">Inverter DC bus voltage reaches 90% of Tractive Battery capacity</td>
  </tr>
  <tr>
    <td class="tg-8v2c"><span style="font-weight:700;text-decoration:underline">7</span></td>
    <td class="tg-8v2c"><span style="font-weight:700;text-decoration:underline">ECU sets precharge signal to LOW (it is HIGH by default)</span></td>
  </tr>
  <tr>
    <td class="tg-8v2c">8</td>
    <td class="tg-8v2c">Precharge relay opens</td>
  </tr>
  <tr>
    <td class="tg-8v2c">9</td>
    <td class="tg-8v2c">IR+ closes</td>
  </tr>
</tbody></table>
</center>
<center><i>Figure 14: Precharge Sequence</i></center>

<p style='text-align: justify'>
The following sections will explain the design changes implemented to <b>rectify</b> the above-mentioned issues for R26E HV system.
</p>

---

[Previous Section: Context of Problem](../context-of-problem.md)

[Next Section: R26E: Precharge-Discharge PCB](../R26e/precharge-discharge-pcb.md)  

[List of Abbreviations](../list-of-abbrev.md)