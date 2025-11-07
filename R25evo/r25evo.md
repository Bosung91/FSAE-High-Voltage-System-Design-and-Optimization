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
Precharge resistors completely melted down, and it could be due to two possible reasons: 
- Under-specced resistor
- Insufficient heat dissipation by heat sink  

### Under-specced resistor
<p style='text-align: justify'>
To determine whether overvoltage, overcurrent, or exceeding power limit or maximum operating temperature caused the meltdown, calculated values for those parameters were compared against datasheet values.
</p>

<div>
<center>

|                         | Datasheet | Actual | Exceeded Datasheet? |
|-------------------------|-----------|--------|---------------------|
| Rated Power/W           | 45        | 7.212  | No                  |
| Max Operating Temp/°C   | 175       | 150    | No                  |
| Max Operating Current/A | 10        | 0.223  | No                  |
| Max Operating Voltage/V | 500       | 333.75 | No                  |

</center>
</div>

<center><i>Figure 7: Parameter Comparison</i></center>
<p style='text-align: justify'>
Based on the comparison of parameters, resistor meltdown is unlikely due to underspeccing for R25Evo precharge circuit.  

Refer to <a href='#'>Appendix A</a> for calculations of actual parameters.
</p>

### Insufficient heat dissipation by heat sink


## PCB board-to-wire Connectors
<p style='text-align: justify'>

</p>

---

[Previous Section: Context of Problem](../context-of-problem.md)

[Next Section: R26E](../R26e/r26e.md)  

[List of Abbreviations](list-of-abbrev.md)