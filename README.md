# myresample

Resample tick data from bitcoincharts csv into OHLC bars  

Installation:  

```
pip install pandas  
git clone https://github.com/spyer/myresample.git
```
Usage:  

```
Required arguments:  
  --file FILE          Path to input csv file  
  
Optional arguments:  
  --outfile [OUTFILE]  Path to output csv file (default: "resampled" + "file" + "period".csv)  
  --period [PERIOD]    Resample period (default: 15min). Pandas format   
                       (see more at: 
                       http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases )  
  --fillna [FILLNA]    How to fill N/A values (default: 0.0)  
  --sep [SEP]          Output csv separator (default: ,)  
```
