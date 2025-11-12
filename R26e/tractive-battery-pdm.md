# Tractive Battery PDM PCB

## Design
<p style='text-align: justify'>
The primary purpose of TB PDM PCB is to distribute power and signals within the TB enclosure. There are total of 59 power, signal and ground ports. The specifications of each port are shown in the table below.
</p>
<center>
<style type="text/css">
.tg  {border-collapse:collapse;border-color:#ccc;border-spacing:0;}
.tg td{background-color:#fff;border-color:#ccc;border-style:solid;border-width:0px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#f0f0f0;border-color:#ccc;border-style:solid;border-width:0px;color:#333;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-6e8n{background-color:#c0c0c0;border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-6e8n">Port</th>
    <th class="tg-6e8n">Type</th>
    <th class="tg-6e8n">Voltage / V</th>
    <th class="tg-6e8n">Current / A</th>
    <th class="tg-6e8n">Description</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">12V IN</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">10</td>
    <td class="tg-0pky">12V power from LV PDM</td>
  </tr>
  <tr>
    <td class="tg-0pky">AIR+</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">12V signal to energise voltage controlled IR+ coil</td>
  </tr>
  <tr>
    <td class="tg-0pky">AIR-</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">12V signal to energise voltage controlled IR- coil</td>
  </tr>
  <tr>
    <td class="tg-0pky">AMBER+</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">0.02</td>
    <td class="tg-0pky">12V signal controlled by Ready to Move PCB to energise Ready to Move light</td>
  </tr>
  <tr>
    <td class="tg-0pky">BMS AOP</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">0.175</td>
    <td class="tg-0pky">Always on battery source. Required for J1772 support during TB charging</td>
  </tr>
  <tr>
    <td class="tg-0pky">BMS CHARGE</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">0.175</td>
    <td class="tg-0pky">12V power that signals BMS is in a defined charging period</td>
  </tr>
  <tr>
    <td class="tg-0pky">BMS CHARGE ENABLE</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">0.5</td>
    <td class="tg-0pky">12V on/off signal used to control an intermittent charging source, such as regenerative braking</td>
  </tr>
  <tr>
    <td class="tg-0pky">BMS CHASSIS</td>
    <td class="tg-0pky">GND</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">Ground for the supply power sources for the BMS</td>
  </tr>
  <tr>
    <td class="tg-0pky">BMS OK (MPO1)</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">0.175</td>
    <td class="tg-0pky">Open drain output which pulls down to ground when on. When BMS has no error, the output is pulled to ground</td>
  </tr>
  <tr>
    <td class="tg-0pky">BMS Ready</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">0.175</td>
    <td class="tg-0pky">Causes BMS to wake up and resume operation from sleep</td>
  </tr>
  <tr>
    <td class="tg-0pky">CAN GND</td>
    <td class="tg-0pky">GND</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">Ground for CAN bus lines</td>
  </tr>
  <tr>
    <td class="tg-0pky">CAN1 HI</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">3.5</td>
    <td class="tg-0pky">0.029</td>
    <td class="tg-0pky">CAN bus line 1 high signal</td>
  </tr>
  <tr>
    <td class="tg-0pky">CAN1 LO</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">1.5</td>
    <td class="tg-0pky">0.013</td>
    <td class="tg-0pky">CAN bus line 1 low signal</td>
  </tr>
  <tr>
    <td class="tg-0pky">CAN2 HI</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">3.5</td>
    <td class="tg-0pky">0.029</td>
    <td class="tg-0pky">CAN bus line 2 high signal</td>
  </tr>
  <tr>
    <td class="tg-0pky">CAN2 LO</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">1.5</td>
    <td class="tg-0pky">0.013</td>
    <td class="tg-0pky">CAN bus line 2 low signal</td>
  </tr>
  <tr>
    <td class="tg-0pky">Charge IN</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">Charger interlock (input)</td>
  </tr>
  <tr>
    <td class="tg-0pky">Charge OUT</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">Charger interlock (output)</td>
  </tr>
  <tr>
    <td class="tg-0pky">Charge SD</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">2</td>
    <td class="tg-0pky">Charger Shutdown line signal</td>
  </tr>
  <tr>
    <td class="tg-0pky">Charger GND</td>
    <td class="tg-0pky">GND</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">Ground for TB charger</td>
  </tr>
  <tr>
    <td class="tg-0pky">Charger PWR</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">5</td>
    <td class="tg-0pky">12V power from TB charger</td>
  </tr>
  <tr>
    <td class="tg-0pky">Charger Splice GND</td>
    <td class="tg-0pky">GND</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">TB charger ground to pull down Proximity MPI2</td>
  </tr>
  <tr>
    <td class="tg-0pky">CHASSIS GND</td>
    <td class="tg-0pky">GND</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">Common GLV ground</td>
  </tr>
  <tr>
    <td class="tg-0pky">CT 5V</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">5</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">CT GND</td>
    <td class="tg-0pky">GND</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">CT Test IN</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">CT Test OUT</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">CT Uout</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">CT Uref</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky">FAN GND</td>
    <td class="tg-0pky">GND</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">NA</td>
    <td class="tg-0pky">Ground for TB cooling fans</td>
  </tr>
  <tr>
    <td class="tg-0pky">FAN PWM Control</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">0.175</td>
    <td class="tg-0pky">PWM output to control TB cooling fans</td>
  </tr>
  <tr>
    <td class="tg-0pky">FAN PWM Signal</td>
    <td class="tg-0pky">SIG</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">0.175</td>
    <td class="tg-0pky">Open drain output from BMS to control TB cooling fans via PWM</td>
  </tr>
  <tr>
    <td class="tg-0pky">FAN PWR</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">12V power to TB cooling fans</td>
  </tr>
  <tr>
    <td class="tg-0pky">FAN PWR1</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">Parallel branch from FAN PWR for one TB cooling fan</td>
  </tr>
  <tr>
    <td class="tg-0pky">FAN PWR2</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">Parallel branch from FAN PWR for one TB cooling fan</td>
  </tr>
  <tr>
    <td class="tg-0pky">FAN PWR3</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">Parallel branch from FAN PWR for one TB cooling fan</td>
  </tr>
  <tr>
    <td class="tg-0pky">FAN PWR4</td>
    <td class="tg-0pky">PWR</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">3</td>
    <td class="tg-0pky">Parallel branch from FAN PWR for one TB cooling fan</td>
  </tr>
  <tr>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for Diagnostic Lights LEDs</td>
  </tr>
  <tr>
    <td class="tg-0lax">IMD CHASSIS</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground pin in IMD dedicated for chassis ground</td>
  </tr>
  <tr>
    <td class="tg-0lax">IMD GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground pin in IMD dedicated for common ground</td>
  </tr>
  <tr>
    <td class="tg-0lax">IMD OK</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">IMD high side status output (high when there is no fault)</td>
  </tr>
  <tr>
    <td class="tg-0lax">IMD PWM</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">IMD data output, PWM</td>
  </tr>
  <tr>
    <td class="tg-0lax">IMD PWR</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.15</td>
    <td class="tg-0lax">12V power to IMD</td>
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