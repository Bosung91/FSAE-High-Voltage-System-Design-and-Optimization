# Context of Problem

<p style='text-align: justify'>
Based on R25E's performance in Formula SAE EV 2025, the team identified that motor controller (<b>BAMOCAR D3 400-400</b>) is performance limited.
</p>

## Overview of Tractive System
<center><img src='./Figures/26 Vehicle TS Schematic.jpg'></center>
<center><i>Figure 5: R26E Tractive System</i></center>  

<p style='text-align: justify'>
As mentioned in the previous section, major HV components affected when <b>CM200DX</b> is integrated to R26E Tractive System are within the Tractive Battery Enclosure, as shown in <i>Figure 5</i> above.
</p>

## BAMOCAR Performance
### Current Limited
<p style='text-align: justify'>The team analysed <b>BAMOCAR</b>'s competition accleration performance based on the data extracted using <b>Energy Meter</b> and discovered as under:</p>  

<center><img src='./Figures/R25E Competition Acceleration Data.png'></center>  
<center><i>Figure 6: R25E Competition Acceleration Data</i></center>  

#### Key Parameters
To aid understanding of <i>Figure 6</i>, the following relationships are introduced:
- Tractive Voltage ∝ Speed
- Tractive Current ∝ Torque

#### Initial Pickup (Red)
- Torque Command: 100%
- Peak Current: 234.6A
- Peak Power: 66.32 kW

#### Wheel Slippage (Orange)
- Current drops due to wheel slip
- Current plateau @ 100% torque command

#### Reaching Maximum Speed (Green)
- Current rises as tyres regain traction
- Current Ramp Rate: 0.39A/ms
- **Acceleration Time: 4.271s**  

### Findings  
<p style='text-align: justify'>
After analysing the data, the team has concluded that there is a potential to reach <b>maximum possible current earlier</b> to achieve <b>higher top speed</b> as the car crosses the finish line due to the following reason: tractive voltage can increase up to maximum of 330V before crossing the finish line if tractive current peaks earlier after tyres regain traction. This is backed up by <u>lower than expected</u> peak power of 66.32kW (rule limit: 80kW, R25E limit: 72.6kW) and tractive voltage <u>continuing to increase</u> after tractive current peaks in the section highlighted in green.
</p>

## Transition to CM200DX
<p style='text-align: justify'>
Due to the limited current ramp rate of <b>BAMOCAR</b> and potential to accelerate faster, the team has decided to use <b>CM200DX</b> for R26E due to its superior performance. For more detailed justification on switching to <b>CM200DX</b>, please refer to <a href='#'>FTS 435 Cascadia System Integration (HV & LV)</a>.
</p>  

---

[Previous Section: Objective and Scope](objective-and-scope.md)

[Next Section: R25Evo](./R25evo/r25evo.md)  

[List of Abbreviations](list-of-abbrev.md)