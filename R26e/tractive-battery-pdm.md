# Tractive Battery PDM PCB

## Design
<p style='text-align: justify'>
The primary purpose of TB PDM PCB is to distribute power and signals within the TB enclosure. There are total of 59 power, signal and ground ports. The specifications of each port are shown in the table below.
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
    <th class="tg-0lax">Port</th>
    <th class="tg-0lax">Type</th>
    <th class="tg-0lax">Voltage / V</th>
    <th class="tg-0lax">Current / A</th>
    <th class="tg-0lax">Description</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax">12V IN</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">10</td>
    <td class="tg-0lax">12V power from LV PDM</td>
  </tr>
  <tr>
    <td class="tg-0lax">AIR+</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">12V signal to energise voltage controlled IR+ coil</td>
  </tr>
  <tr>
    <td class="tg-0lax">AIR-</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">12V signal to energise voltage controlled IR- coil</td>
  </tr>
  <tr>
    <td class="tg-0lax">AMBER+</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.02</td>
    <td class="tg-0lax">12V signal controlled by Ready to Move PCB to energise Ready to Move light</td>
  </tr>
  <tr>
    <td class="tg-0lax">BMS AOP</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">Always on battery source. Required for J1772 support during TB charging</td>
  </tr>
  <tr>
    <td class="tg-0lax">BMS CHARGE</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">12V power that signals BMS is in a defined charging period</td>
  </tr>
  <tr>
    <td class="tg-0lax">BMS CHARGE ENABLE</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.5</td>
    <td class="tg-0lax">12V on/off signal used to control an intermittent charging source, such as regenerative braking</td>
  </tr>
  <tr>
    <td class="tg-0lax">BMS CHASSIS</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for the supply power sources for the BMS</td>
  </tr>
  <tr>
    <td class="tg-0lax">BMS OK (MPO1)</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">Open drain output which pulls down to ground when on. When BMS has no error, the output is pulled to ground</td>
  </tr>
  <tr>
    <td class="tg-0lax">BMS Ready</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">Causes BMS to wake up and resume operation from sleep</td>
  </tr>
  <tr>
    <td class="tg-0lax">CAN GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for CAN bus lines</td>
  </tr>
  <tr>
    <td class="tg-0lax">CAN1 HI</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">3.5</td>
    <td class="tg-0lax">0.029</td>
    <td class="tg-0lax">CAN bus line 1 high signal</td>
  </tr>
  <tr>
    <td class="tg-0lax">CAN1 LO</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">1.5</td>
    <td class="tg-0lax">0.013</td>
    <td class="tg-0lax">CAN bus line 1 low signal</td>
  </tr>
</tbody></table>
</center>

## Simulation
_Content_

## Prototyping
_Content_

---

[Previous Section: R26E: Precharge-Discharge PCB](precharge-discharge-pcb.md)

[Next Section: R26E: HV Distribution PCB](hv-distribution-pcb.md)  

[List of Abbreviations](list-of-abbrev.md)