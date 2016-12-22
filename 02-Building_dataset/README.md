### Data Source - Quandl
#### install
```
pip install quandl
```
> this package need network

#### quandl api key
```
df = quandl.get("FMAC/HPI_AK", authtoken=your_api_key)
```
You need sigh up a quandl account to get a api key for yourself. :>

---
### Data Source - WIKI
```
import pandas sa pd
pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
```

---
### Running Results
```
                 Value
Date
2015-09-30  176.422094
2015-10-31  176.037791
2015-11-30  175.707531
2015-12-31  175.458560
2016-01-31  175.217552
0     Abbreviation
1               AL
2               AK
3               AZ
4               AR
5               CA
6               CO
7               CT
8               DE
9               FL
10              GA
11              HI
12              ID
13              IL
14              IN
15              IA
16              KS
17              KY
18              LA
19              ME
20              MD
21              MA
22              MI
23              MN
24              MS
25              MO
26              MT
27              NE
28              NV
29              NH
30              NJ
31              NM
32              NY
33              NC
34              ND
35              OH
36              OK
37              OR
38              PA
39              RI
40              SC
41              SD
42              TN
43              TX
44              UT
45              VT
46              VA
47              WA
48              WV
49              WI
50              WY
Name: 0, dtype: object
FMAC/HPI_AL
FMAC/HPI_AK
FMAC/HPI_AZ
FMAC/HPI_AR
FMAC/HPI_CA
FMAC/HPI_CO
FMAC/HPI_CT
FMAC/HPI_DE
FMAC/HPI_FL
FMAC/HPI_GA
FMAC/HPI_HI
FMAC/HPI_ID
FMAC/HPI_IL
FMAC/HPI_IN
FMAC/HPI_IA
FMAC/HPI_KS
FMAC/HPI_KY
FMAC/HPI_LA
FMAC/HPI_ME
FMAC/HPI_MD
FMAC/HPI_MA
FMAC/HPI_MI
FMAC/HPI_MN
FMAC/HPI_MS
FMAC/HPI_MO
FMAC/HPI_MT
FMAC/HPI_NE
FMAC/HPI_NV
FMAC/HPI_NH
FMAC/HPI_NJ
FMAC/HPI_NM
FMAC/HPI_NY
FMAC/HPI_NC
FMAC/HPI_ND
FMAC/HPI_OH
FMAC/HPI_OK
FMAC/HPI_OR
FMAC/HPI_PA
FMAC/HPI_RI
FMAC/HPI_SC
FMAC/HPI_SD
FMAC/HPI_TN
FMAC/HPI_TX
FMAC/HPI_UT
FMAC/HPI_VT
FMAC/HPI_VA
FMAC/HPI_WA
FMAC/HPI_WV
FMAC/HPI_WI
FMAC/HPI_WY
```
