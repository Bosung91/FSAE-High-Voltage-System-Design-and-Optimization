# Objective and Scope

## Team Goal
Based on R25E's performance in 2025 FSAE Michigan, the team has formed the following goal:  
_Decrease average lap time in Endurance by **10%** through **improved reliability**_

## High Voltage Department Goal
To achieve the team goal, High Voltage (HV) department's goal is as following:  
_**System integration and optimization** of CM200DX motor controller_  

The testbed for CM200DX called, _R25Evo_, as modifications have been made to R25E to integrate CM200DX into R25E powertrain architecture.  

Detailed explanation of changing motor controller from BAMOCAR D3 400-400 to CM200DX will be explained in the next section, _Context of Problem_.

## Timeline
Introducing a new motor controller to an existing HV architecture is a tremendous challenge, which requires thorough planning and execution months before R26E design phase.  

<center><img src='./Figures/Timeline.png'></center>  
<center><i>Figure 2: Timeline</i></center>

---

For HV System Design and Optimization, emphasis is on the following tasks:  
1. Finalise EE shelf, PCBs for R25Evo & R26E, wires for R25Evo
2. R25Evo testbench
3. R25Evo test run  

### Finalise EE shelf, PCBs for R25Evo & R26E, wires for R25Evo
Changes were identified for R25E powertrain architecture to accommodate CM200DX and to ensure 2026 season rule compliancy. Based on the changes identified, new PCBs need to be designed, prototyped and tested.  

No changes were required for HV PCBs prior to R25Evo test run as they were CM200DX compatible and 2026 season rule compliant.

### R25Evo testbench
R25Evo testbench was designed to validate compatibility and functionality of exisiting and modified components required.  

<center><img src='./Figures/R25Evo Testbench.jpg'></center>  
<center><i>Figure 3: R25Evo Testbench</i></center>

---

The testbench was set up as shown in _Figure 3_, which represents the entire powertrain architecture in R25E.  

Using the testbench, following HV functionalities of R25Evo were be tested:
- Precharge Sequence
- Closing TS Circuit
- Discharge Sequence

HV PCBs involved in the above functionalities were installed in Tractive Battery enclosure as shown in _Figure 4_ below.  

<center><img src='./Figures/R25E Tractive Battery Internals.jpg'></center>  
<center><i>Figure 4: R25E Tractive Battery Enclosure Internals</i></center>  

---

HV PCBs involved are: Precharge-Discharge PCB (blue), Tractive Battery PDM PCB (orange) and HV Distribution PCB (green), as shown in _Figure 4_.

### R25Evo test run
After validating powertrain functionalities with CM200DX on the testbench, test runs were conducted to determine whether HV system functions as designed when R25Evo is running with CM200DX and to finalise HV system design for R26E based on results gathered from the test runs.

## Scope
This report focuses on R25Evo and how it affects HV system design and optimization of R26E, which comprises Precharge-Discharge PCB, Tractive Battery PDM PCB and HV Distribution PCB.

---

[Previous Section: Introduction](introduction.md)

[Next Section: Context of Problem](context-of-problem.md)  

[List of Abbreviations](list-of-abbrev.md)