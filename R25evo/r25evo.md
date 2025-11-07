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