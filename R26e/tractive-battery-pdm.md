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
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg"><thead>
  <tr>
    <th class="tg-1wig">No</th>
    <th class="tg-1wig">Port</th>
    <th class="tg-1wig">Type</th>
    <th class="tg-1wig">Voltage / V</th>
    <th class="tg-1wig">Current / A</th>
    <th class="tg-1wig">Description</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax">1</td>
    <td class="tg-0lax">12V IN</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">10</td>
    <td class="tg-0lax">12V power from LV PDM</td>
  </tr>
  <tr>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">AIR+</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">12V signal to energise voltage controlled IR+ coil</td>
  </tr>
  <tr>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">AIR-</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">12V signal to energise voltage controlled IR- coil</td>
  </tr>
  <tr>
    <td class="tg-0lax">4</td>
    <td class="tg-0lax">AMBER+</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.02</td>
    <td class="tg-0lax">12V signal controlled by Ready to Move PCB to energise Ready to Move light</td>
  </tr>
  <tr>
    <td class="tg-0lax">5</td>
    <td class="tg-0lax">BMS AOP</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">Always on battery source. Required for J1772 support during TB charging</td>
  </tr>
  <tr>
    <td class="tg-0lax">6</td>
    <td class="tg-0lax">BMS CHARGE</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">12V power that signals BMS is in a defined charging period</td>
  </tr>
  <tr>
    <td class="tg-0lax">7</td>
    <td class="tg-0lax">BMS CHARGE ENABLE</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.5</td>
    <td class="tg-0lax">12V on/off signal used to control an intermittent charging source, such as regenerative braking</td>
  </tr>
  <tr>
    <td class="tg-0lax">8</td>
    <td class="tg-0lax">BMS CHASSIS</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for the supply power sources for the BMS</td>
  </tr>
  <tr>
    <td class="tg-0lax">9</td>
    <td class="tg-0lax">BMS OK (MPO1)</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">Open drain output which pulls down to ground when on. When BMS has no error, the output is pulled to ground</td>
  </tr>
  <tr>
    <td class="tg-0lax">10</td>
    <td class="tg-0lax">BMS Ready</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">Causes BMS to wake up and resume operation from sleep</td>
  </tr>
  <tr>
    <td class="tg-0lax">11</td>
    <td class="tg-0lax">CAN GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for CAN bus lines</td>
  </tr>
  <tr>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">CAN1 HI</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">3.5</td>
    <td class="tg-0lax">0.029</td>
    <td class="tg-0lax">CAN bus line 1 high signal</td>
  </tr>
  <tr>
    <td class="tg-0lax">13</td>
    <td class="tg-0lax">CAN1 LO</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">1.5</td>
    <td class="tg-0lax">0.013</td>
    <td class="tg-0lax">CAN bus line 1 low signal</td>
  </tr>
  <tr>
    <td class="tg-0lax">14</td>
    <td class="tg-0lax">CAN2 HI</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">3.5</td>
    <td class="tg-0lax">0.029</td>
    <td class="tg-0lax">CAN bus line 2 high signal</td>
  </tr>
  <tr>
    <td class="tg-0lax">15</td>
    <td class="tg-0lax">CAN2 LO</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">1.5</td>
    <td class="tg-0lax">0.013</td>
    <td class="tg-0lax">CAN bus line 2 low signal</td>
  </tr>
  <tr>
    <td class="tg-0lax">16</td>
    <td class="tg-0lax">Charge IN</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Charger interlock (input)</td>
  </tr>
  <tr>
    <td class="tg-0lax">17</td>
    <td class="tg-0lax">Charge OUT</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Charger interlock (output)</td>
  </tr>
  <tr>
    <td class="tg-0lax">18</td>
    <td class="tg-0lax">Charge SD</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Charger Shutdown line signal</td>
  </tr>
  <tr>
    <td class="tg-0lax">19</td>
    <td class="tg-0lax">Charger GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for TB charger</td>
  </tr>
  <tr>
    <td class="tg-0lax">20</td>
    <td class="tg-0lax">Charger PWR</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">5</td>
    <td class="tg-0lax">12V power from TB charger</td>
  </tr>
  <tr>
    <td class="tg-0lax">21</td>
    <td class="tg-0lax">Charger Splice GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">TB charger ground to pull down Proximity MPI2</td>
  </tr>
  <tr>
    <td class="tg-0lax">22</td>
    <td class="tg-0lax">CHASSIS GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Common GLV ground</td>
  </tr>
  <tr>
    <td class="tg-0lax">23</td>
    <td class="tg-0lax">CT 5V</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">5</td>
    <td class="tg-0lax">0.015</td>
    <td class="tg-0lax">5V power for BSPD</td>
  </tr>
  <tr>
    <td class="tg-0lax">24</td>
    <td class="tg-0lax">CT GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for BSPD</td>
  </tr>
  <tr>
    <td class="tg-0lax">25</td>
    <td class="tg-0lax">CT Test IN</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Test signal to simulate TS current</td>
  </tr>
  <tr>
    <td class="tg-0lax">26</td>
    <td class="tg-0lax">CT Test OUT</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Test signal to simulate TS current</td>
  </tr>
  <tr>
    <td class="tg-0lax">27</td>
    <td class="tg-0lax">CT Uout</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">5</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">TS current hall effect sensor signal</td>
  </tr>
  <tr>
    <td class="tg-0lax">28</td>
    <td class="tg-0lax">CT Uref</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">2.5</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">TS current hall effect sensor internal reference</td>
  </tr>
  <tr>
    <td class="tg-0lax">29</td>
    <td class="tg-0lax">FAN GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for TB cooling fans</td>
  </tr>
  <tr>
    <td class="tg-0lax">30</td>
    <td class="tg-0lax">FAN PWM Control</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">PWM output to control TB cooling fans</td>
  </tr>
  <tr>
    <td class="tg-0lax">31</td>
    <td class="tg-0lax">FAN PWM Signal</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.175</td>
    <td class="tg-0lax">Open drain output from BMS to control TB cooling fans via PWM</td>
  </tr>
  <tr>
    <td class="tg-0lax">32</td>
    <td class="tg-0lax">FAN PWR</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">12V power to TB cooling fans</td>
  </tr>
  <tr>
    <td class="tg-0lax">33</td>
    <td class="tg-0lax">FAN PWR1</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">Parallel branch from FAN PWR for one TB cooling fan</td>
  </tr>
  <tr>
    <td class="tg-0lax">34</td>
    <td class="tg-0lax">FAN PWR2</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">Parallel branch from FAN PWR for one TB cooling fan</td>
  </tr>
  <tr>
    <td class="tg-0lax">35</td>
    <td class="tg-0lax">FAN PWR3</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">Parallel branch from FAN PWR for one TB cooling fan</td>
  </tr>
  <tr>
    <td class="tg-0lax">36</td>
    <td class="tg-0lax">FAN PWR4</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">3</td>
    <td class="tg-0lax">Parallel branch from FAN PWR for one TB cooling fan</td>
  </tr>
  <tr>
    <td class="tg-0lax">37</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for Diagnostic Lights LEDs</td>
  </tr>
  <tr>
    <td class="tg-0lax">38</td>
    <td class="tg-0lax">IMD CHASSIS</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground pin in IMD dedicated for chassis ground</td>
  </tr>
  <tr>
    <td class="tg-0lax">39</td>
    <td class="tg-0lax">IMD GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground pin in IMD dedicated for common ground</td>
  </tr>
  <tr>
    <td class="tg-0lax">40</td>
    <td class="tg-0lax">IMD OK</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">IMD high side status output (high when there is no fault)</td>
  </tr>
  <tr>
    <td class="tg-0lax">41</td>
    <td class="tg-0lax">IMD PWM</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">IMD data output, PWM</td>
  </tr>
  <tr>
    <td class="tg-0lax">42</td>
    <td class="tg-0lax">IMD PWR</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.15</td>
    <td class="tg-0lax">12V power to IMD</td>
  </tr>
  <tr>
    <td class="tg-0lax">43</td>
    <td class="tg-0lax">INT IN</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Interlock from Master Panel and MSD to TB</td>
  </tr>
  <tr>
    <td class="tg-0lax">44</td>
    <td class="tg-0lax">INT OUT</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Shutdown line signal from Master Panel interlock</td>
  </tr>
  <tr>
    <td class="tg-0lax">45</td>
    <td class="tg-0lax">MSD</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Shutdown line signal from MSD interlock</td>
  </tr>
  <tr>
    <td class="tg-0lax">46</td>
    <td class="tg-0lax">Pilot MPI1</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.012</td>
    <td class="tg-0lax">J1772 control pilot (active high). Primary control conductor to verify vehicle connection during charging</td>
  </tr>
  <tr>
    <td class="tg-0lax">47</td>
    <td class="tg-0lax">Proximity MPI2</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">0</td>
    <td class="tg-0lax">0</td>
    <td class="tg-0lax">J1772 proximity detection (active low). Allows vehicle to detect presence of charge connector</td>
  </tr>
  <tr>
    <td class="tg-0lax">48</td>
    <td class="tg-0lax">Pre Dis GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for Precharge-Discharge PCB</td>
  </tr>
  <tr>
    <td class="tg-0lax">49</td>
    <td class="tg-0lax">Pre Dis PWR</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.060</td>
    <td class="tg-0lax">12V power for Precharge-Discharge PCB</td>
  </tr>
  <tr>
    <td class="tg-0lax">50</td>
    <td class="tg-0lax">Pre Dis SD</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Shutdown line signal from Precharge-Discharge PCB</td>
  </tr>
  <tr>
    <td class="tg-0lax">51</td>
    <td class="tg-0lax">Pre Sig</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">0.025</td>
    <td class="tg-0lax">Precharge signal from ECU</td>
  </tr>
  <tr>
    <td class="tg-0lax">52</td>
    <td class="tg-0lax">RTM GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for Ready to Move light</td>
  </tr>
  <tr>
    <td class="tg-0lax">53</td>
    <td class="tg-0lax">TEMP BUS</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">0</td>
    <td class="tg-0lax">0</td>
    <td class="tg-0lax">Supply voltage for 1-wire digital thermometer monitoring TB cell temperatures</td>
  </tr>
  <tr>
    <td class="tg-0lax">54</td>
    <td class="tg-0lax">TEMP GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for 1-wire digital thermometer monitoring TB cell temperatures</td>
  </tr>
  <tr>
    <td class="tg-0lax">55</td>
    <td class="tg-0lax">THERM GND</td>
    <td class="tg-0lax">GND</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">Ground for 10K NTC thermistors with a B25/50 value of 3380K</td>
  </tr>
  <tr>
    <td class="tg-0lax">56</td>
    <td class="tg-0lax">THERM PWR</td>
    <td class="tg-0lax">PWR</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">NA</td>
    <td class="tg-0lax">12V power for 10K NTC thermistors with a B25/50 value of 3380K</td>
  </tr>
  <tr>
    <td class="tg-0lax">57</td>
    <td class="tg-0lax">TO MSD</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Interlock from TB enclosure to MSD</td>
  </tr>
  <tr>
    <td class="tg-0lax">58</td>
    <td class="tg-0lax">TO TSMP</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Interlock from TB enclosure to TSMP</td>
  </tr>
  <tr>
    <td class="tg-0lax">59</td>
    <td class="tg-0lax">TSMP</td>
    <td class="tg-0lax">SIG</td>
    <td class="tg-0lax">12</td>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">Shutdown line signal from TSMP</td>
  </tr>
</tbody></table>
</center>
<center><i>Figure 24: TB PDM PCB System Requirements</i></center>

<br>

### Trace Width
<p style='text-align: justify'>
Based on the system requirements, PCB copper trace width has been calculated using Altium Designer under IPC-2221 standard.
</p>

### Diagnostic Lights
<p style='text-align: justify'>
This set of LEDs will light up when there is no fault in the Shutdown line components: TB Charger, Interlock, IR+, IR-, MSD, Precharge-Discharge, TSMP.
</p>

### Diodes
<p style='text-align: justify'>
All diodes protect power supply from ECU or TB charger.
</p>

### Resistors
<p style='text-align: justify'>
Termination resistors are used for CAN2 bus lines, pull-down resistor is used for Proximity MPI2, pull-up resistor is used for PWM control circuit and current-limiting resistors are used for Diagnostic Lights.
</p>

### Connectors
<p style='text-align: justify'>
Total of 18 connectors are used on TB PDM PCB. Deustch Autosport connectors are used due to their superior pin density, vibration resistance and waterproofness (motorsport grade), while Hirose DF63 series connectors are used due to their compactness and vibration resistance (<a href='https://www.hirose.com/en/product/series/DF63' target='_blank'>meant for motors and motor drives</a>).
</p>

<p style='text-align: justify'>
R25Evo stopped approximately 20 times due to loose wire harness connections between TB PDM PCB to other components in TB enclosure. Hirose DF63 series connectors are chosen to deal with this issue as they present crimp profile and locking mechanism that ensure secure connection even under vibration. <i>Figure 25</i> shows the design of Hirose DF63 series connector (<a href='https://drive.google.com/file/d/10Ltabzmpp26rV4KXxHFZl8xF2f_CsPVx/view?usp=sharing' target='_blank'>Hirose, 2025</a>).
</p>

<center><img src='../Figures/Hirose Vibration Resistant Feature.png'></center>
<center><i>Figure 25: Hirose DF63 Vibration Resistant Features (<a href='https://drive.google.com/file/d/10Ltabzmpp26rV4KXxHFZl8xF2f_CsPVx/view?usp=sharing' target='_blank'>Hirose, 2025</a>)</i></center>

<br>

<p style='text-align: justify'>
TB PDM PCB schematic is shown in <i>Figure 26</i>.
</p>
<center><img src='../Figures/Tractive Battery PDM PCB Schematic.png'></center>
<center><i>Figure 26: 26 TB PDM PCB Schematic</i></center>

<br>

<p style='text-align: justify'>
Refer to <a href='https://bosung91.github.io/FSAE-High-Voltage-System-Design-and-Optimization/appendix.html#e' target='_blank'>Appendix E</a> for calculations behind selecting the components.
</p>

## Prototyping
Deutsch Autosports connectors are panel mounted to TB enclosure for external connections, while Hirose DF63 series connectors are for internal connections within TB enclosure.
<center><img src='../Figures/Tractive Battery PDM PCB Front.png'></center>
<center><i>Figure 27: 26 TB PDM PCB Front View</i></center>

<br>

<center><img src='../Figures/Tractive Battery PDM PCB Rear.png'></center>
<center><i>Figure 28: 26 TB PDM PCB Rear View</i></center>

<br>

<p style='text-align: justify'>
The board is mounted vertically to prevent water accumulation on it in case there is water ingress in TB enclosure. Humiseal 1B73 conformal coat is applied for electrical insulation and moisture protection.
</p>

---

[Previous Section: R26E: Precharge-Discharge PCB](precharge-discharge-pcb.md)

[Next Section: R26E: HV Distribution PCB](hv-distribution-pcb.md)  

[List of Abbreviations](../list-of-abbrev.md)