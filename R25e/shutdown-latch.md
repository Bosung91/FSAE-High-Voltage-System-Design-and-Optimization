# Shutdown Latch PCB

## Design
### Rule
![EV.7.1](../Figures/Rule_Shutdown%20Circuit%201.png)  
_Figure 1: Screenshot of FSAE Rule EV.7.1_

---

![EV.7.2](../Figures/Rule_Shutdown%20Circuit%202.png)  
_Figure 2: Screenshot of FSAE Rule EV.7.2_

---

The purpose of Shutdown Latch PCB is to incorporate normally open and independent BMS, IMD and BSPD circuits as dictated by the rules shown in Figure 1, while opening the entire Shutdown Circuit when any of the three error signals is sent to the PCB as dictated by the rules shown in Figure 2.

### Schematic
To fulfill the requirements set by the rule, the following schematic has been designed.  

![Shutdown Latch PCB Detailed Schematic](../Figures/Shutdown%20Latch%20PCB%20Detailed%20Schematic.png)  
_Figure 3: Shutdown Latch PCB Altium Schematic_

---

The Shutdown Latch PCB consists normally open double-pole-single-throw relays which act as series switches in the Shutdown Circuit for BMS, IMD and BSPD each. BMS, IMD and BSPD circuits in the Shutdown Latch PCB function the same way. The following block diagram explains the functionality of Shutdown Latch PCB.  

![Shutdown Latch PCB Block Diagram](../Figures/Shutdown%20Latch%20PCB%20Block%20Diagram.jpg)  
_Figure 4: Shutdown Latch PCB Block Diagram_

---

### Speccing Components


## Simulation
### Falstad
_Explain how the schematic is being tested as per car start up sequence (refer to 26 Electrical Powertrain 101 for Falstad links)_

## Prototyping
### Manufacturing
_Interhorizon Pte. Ltd. manufactures PCBs for us, just briefly go through this section_

### Testbench
_Mention car start up sequence and how we induced errors to check Shutdown Latch functionality_

## Testing and Validation
### Test Run
_Mention how the team was able to troubleshoot the car immediately thanks to dashboard indicators connected to Shutdown Latch_

### Technical Inspection
_Talk about ESF & EV Active_

---

[Previous Section: R25e](r25e.md)

[Next Section: R25e: Ready to Move PCB](ready-to-move.md)  

[List of Abbreviations](list-of-abbrev.md)