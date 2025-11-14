# Objective and Scope

## Team Goal
<p style='text-align: justify'>
Based on R25E's performance in 2025 FSAE Michigan, the team has formed the following goal:  
<h3><center><i>Decrease average lap time in Endurance by <b>10%</b> through <b>improved reliability</b></i></center></h3>
</p>

## High Voltage Department Goal
<p style='text-align: justify'>
To achieve the team goal, High Voltage (HV) department's goal is as following:  
<h3><center><i><b>System integration and optimization</b> of CM200DX motor controller</i></center></h3>  

Reliability can only be achieved when <b>CM200DX</b> is seamlessly integrated into the HV system. Once <b>CM200DX</b> is properly integrated, the team can then aim to decrease average lap time in endurance.
</p>

<p style='text-align: justify'>
The testbed for <b>CM200DX</b> is called, <i>R25Evo</i>, as modifications have been made to R25E to integrate <b>CM200DX</b> into R25E powertrain architecture.  

Brief explanation of changing motor controller from <b>BAMOCAR D3 400-400</b> to <b>CM200DX</b> will be explained in the next section, <i>Context of Problem</i>.
</p>

## Timeline
<p style='text-align: justify'>
Introducing a new motor controller to an existing HV architecture is a tremendous technical challenge, which requires thorough planning and execution months before R26E design phase.
</p>  

<center><img src='./Figures/Timeline.png'></center>  
<center><i>Figure 2: Timeline</i></center>

---

For HV System Design and Optimization, emphasis is on the following tasks:
1. Finalise EE shelf, PCBs for R25Evo & R26E, wires for R25Evo
2. R25Evo testbench
3. R25Evo test run  

### Finalise EE shelf, PCBs for R25Evo & R26E, wires for R25Evo
<p style='text-align: justify'>
Changes were identified for R25E powertrain architecture to accommodate <b>CM200DX</b> and to ensure 2026 season rule compliancy. Based on the changes identified, new PCBs need to be designed, prototyped and tested.  

No changes were required for HV PCBs prior to R25Evo test run as they were <b>CM200DX</b> compatible and 2026 season rule compliant.
</p>

### R25Evo testbench
<p style='text-align: justify'>
R25Evo testbench was designed to validate compatibility and functionality of exisiting and modified components required.
</p>  

<center><img src='./Figures/R25Evo Testbench.jpg'></center>  
<center><i>Figure 3: R25Evo Testbench</i></center>

---

<p style='text-align: justify'>
The testbench was set up as shown in <i>Figure 3</i>, which represents the entire powertrain architecture in R25E.</p>  

Using the testbench, following HV functionalities of R25Evo were tested:
- Precharge Sequence
- Closing TS Circuit
- Discharge Sequence

<p style='text-align: justify'>
HV PCBs responsible for the above functionalities were installed in Tractive Battery enclosure as shown in <i>Figure 4</i> below.
</p>  

<center><img src='./Figures/Breakdown of HV PCBs in TB Enclosure.png'></center>  
<center><i>Figure 4: R25E Tractive Battery Enclosure Internals</i></center>  

---

<p style='text-align: justify'>
HV PCBs are: HV Distribution (green), TB PDM (orange) and Precharge-Discharge (blue).
</p>

### R25Evo test run
<p style='text-align: justify'>
After validating powertrain functionalities with <b>CM200DX</b> on the testbench, test runs were conducted to determine whether HV system functions as designed when R25Evo is running with <b>CM200DX</b> and to finalise HV system design for R26E based on results gathered from the test runs.
</p>

## Scope
<p style='text-align: justify'>
This report focuses on R25Evo and how it affects HV system design and optimization of R26E, which comprises Precharge-Discharge PCB, Tractive Battery PDM PCB and HV Distribution PCB.
</p>

---

[Previous Section: Introduction](introduction.md)

[Next Section: Context of Problem](context-of-problem.md)  

[List of Abbreviations](list-of-abbrev.md)