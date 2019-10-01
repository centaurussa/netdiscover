<p align="center">
  <b>Send an ARP request to a certain range and wait for a response from the active devices to monitor the overall activity or by a live scanning.
</b><br>
</p>

![Example](/docs/Example.PNG)
&nbsp;
&nbsp;
## How to use it:
* **By arguments**: `python scanner.py --network RANGE --live 0/1`
    * network: To scan a network range. For example `192.168.1.1/24`
    * live: To capture devices at any time (past and present) use `0` , and `1` for a realtime scanning (present). 
    
* **By running the script**:
    * Handled by basic input

## Requirements:
   * Python 3:
      * Scapy
   * Windows:
      * WinPcap
   * Linux:
      * Running the script as sudo
