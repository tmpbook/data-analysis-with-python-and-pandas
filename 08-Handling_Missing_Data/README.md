#### Running Results
``` python
# HPI_data['TX1yr'] = HPI_data['TX'].resample('A').mean()
# print(HPI_data[['TX', 'TX1yr']])
                    TX       TX1yr
Date
1996-09-30   80.643400         NaN
1996-10-31   80.608344         NaN
1996-11-30   80.553995         NaN
1996-12-31   80.474669   80.570102
1997-01-31   80.480457         NaN
1997-02-28   80.713488         NaN
1997-03-31   81.145650         NaN
1997-04-30   81.630518         NaN
1997-05-31   82.089654         NaN
1997-06-30   82.442786         NaN
1997-07-31   82.566763         NaN
1997-08-31   82.635798         NaN
1997-09-30   82.827637         NaN
1997-10-31   83.071904         NaN
1997-11-30   83.279273         NaN
1997-12-31   83.469709   82.196136
1998-01-31   83.689827         NaN
1998-02-28   84.036493         NaN
1998-03-31   84.603041         NaN
1998-04-30   85.252143         NaN
1998-05-31   85.908889         NaN
1998-06-30   86.465929         NaN
1998-07-31   86.954801         NaN
1998-08-31   87.356110         NaN
1998-09-30   87.514393         NaN
1998-10-31   87.629053         NaN
1998-11-30   87.945690         NaN
1998-12-31   88.210815   86.297265
1999-01-31   88.294076         NaN
1999-02-28   88.801456         NaN
...                ...         ...
2014-04-30  149.750687         NaN
2014-05-31  151.491445         NaN
2014-06-30  152.950676         NaN
2014-07-31  153.958918         NaN
2014-08-31  154.700157         NaN
2014-09-30  155.258659         NaN
2014-10-31  155.562846         NaN
2014-11-30  155.935939         NaN
2014-12-31  156.370918  152.073547
2015-01-31  156.874024         NaN
2015-02-28  158.024475         NaN
2015-03-31  159.893825         NaN
2015-04-30  161.839395         NaN
2015-05-31  163.662033         NaN
2015-06-30  165.361119         NaN
2015-07-31  166.537058         NaN
2015-08-31  166.825724         NaN
2015-09-30  166.927714         NaN
2015-10-31  167.349793         NaN
2015-11-30  167.649963         NaN
2015-12-31  167.738984  164.057009
2016-01-31  168.352857         NaN
2016-02-29  169.904181         NaN
2016-03-31  171.544114         NaN
2016-04-30  173.229875         NaN
2016-05-31  175.298871         NaN
2016-06-30  176.893272         NaN
2016-07-31  177.950783         NaN
2016-08-31  178.682159         NaN
2016-09-30  178.934070         NaN

[241 rows x 2 columns]

# HPI_data.dropna(inplace=True)
# print(HPI_data[['TX', 'TX1yr']])
                    TX       TX1yr
Date
1996-12-31   80.474669   80.570102
1997-12-31   83.469709   82.196136
1998-12-31   88.210815   86.297265
1999-12-31   94.058753   91.686902
2000-12-31  100.000000   97.836797
2001-12-31  103.647005  103.030212
2002-12-31  107.808260  106.747049
2003-12-31  110.032379  109.523127
2004-12-31  113.615275  112.762041
2005-12-31  120.229806  117.870057
2006-12-31  126.623597  124.786527
2007-12-31  129.353549  130.044761
2008-12-31  126.972736  129.744470
2009-12-31  127.995770  128.145987
2010-12-31  124.721944  127.846182
2011-12-31  125.186681  125.786520
2012-12-31  133.124616  130.481424
2013-12-31  144.661971  140.461587
2014-12-31  156.370918  152.073547
2015-12-31  167.738984  164.057009

# HPI_data.fillna(method='bfill', inplace=True)
# print(HPI_data[['TX', 'TX1yr']])
                    TX       TX1yr
Date
1996-09-30   80.643400   80.570102
1996-10-31   80.608344   80.570102
1996-11-30   80.553995   80.570102
1996-12-31   80.474669   80.570102
1997-01-31   80.480457   82.196136
1997-02-28   80.713488   82.196136
1997-03-31   81.145650   82.196136
1997-04-30   81.630518   82.196136
1997-05-31   82.089654   82.196136
1997-06-30   82.442786   82.196136
1997-07-31   82.566763   82.196136
1997-08-31   82.635798   82.196136
1997-09-30   82.827637   82.196136
1997-10-31   83.071904   82.196136
1997-11-30   83.279273   82.196136
1997-12-31   83.469709   82.196136
1998-01-31   83.689827   86.297265
1998-02-28   84.036493   86.297265
1998-03-31   84.603041   86.297265
1998-04-30   85.252143   86.297265
1998-05-31   85.908889   86.297265
1998-06-30   86.465929   86.297265
1998-07-31   86.954801   86.297265
1998-08-31   87.356110   86.297265
1998-09-30   87.514393   86.297265
1998-10-31   87.629053   86.297265
1998-11-30   87.945690   86.297265
1998-12-31   88.210815   86.297265
1999-01-31   88.294076   91.686902
1999-02-28   88.801456   91.686902
...                ...         ...
2014-04-30  149.750687  152.073547
2014-05-31  151.491445  152.073547
2014-06-30  152.950676  152.073547
2014-07-31  153.958918  152.073547
2014-08-31  154.700157  152.073547
2014-09-30  155.258659  152.073547
2014-10-31  155.562846  152.073547
2014-11-30  155.935939  152.073547
2014-12-31  156.370918  152.073547
2015-01-31  156.874024  164.057009
2015-02-28  158.024475  164.057009
2015-03-31  159.893825  164.057009
2015-04-30  161.839395  164.057009
2015-05-31  163.662033  164.057009
2015-06-30  165.361119  164.057009
2015-07-31  166.537058  164.057009
2015-08-31  166.825724  164.057009
2015-09-30  166.927714  164.057009
2015-10-31  167.349793  164.057009
2015-11-30  167.649963  164.057009
2015-12-31  167.738984  164.057009
2016-01-31  168.352857         NaN
2016-02-29  169.904181         NaN
2016-03-31  171.544114         NaN
2016-04-30  173.229875         NaN
2016-05-31  175.298871         NaN
2016-06-30  176.893272         NaN
2016-07-31  177.950783         NaN
2016-08-31  178.682159         NaN
2016-09-30  178.934070         NaN

[241 rows x 2 columns]

# HPI_data.fillna(value=-99999, limit=10, inplace=True)
# print(HPI_data[['TX', 'TX1yr']])
                    TX         TX1yr
Date
1996-09-30   80.643400 -99999.000000
1996-10-31   80.608344 -99999.000000
1996-11-30   80.553995 -99999.000000
1996-12-31   80.474669     80.570102
1997-01-31   80.480457 -99999.000000
1997-02-28   80.713488 -99999.000000
1997-03-31   81.145650 -99999.000000
1997-04-30   81.630518 -99999.000000
1997-05-31   82.089654 -99999.000000
1997-06-30   82.442786 -99999.000000
1997-07-31   82.566763 -99999.000000
1997-08-31   82.635798           NaN
1997-09-30   82.827637           NaN
1997-10-31   83.071904           NaN
1997-11-30   83.279273           NaN
1997-12-31   83.469709     82.196136
1998-01-31   83.689827           NaN
1998-02-28   84.036493           NaN
1998-03-31   84.603041           NaN
1998-04-30   85.252143           NaN
1998-05-31   85.908889           NaN
1998-06-30   86.465929           NaN
1998-07-31   86.954801           NaN
1998-08-31   87.356110           NaN
1998-09-30   87.514393           NaN
1998-10-31   87.629053           NaN
1998-11-30   87.945690           NaN
1998-12-31   88.210815     86.297265
1999-01-31   88.294076           NaN
1999-02-28   88.801456           NaN
...                ...           ...
2014-04-30  149.750687           NaN
2014-05-31  151.491445           NaN
2014-06-30  152.950676           NaN
2014-07-31  153.958918           NaN
2014-08-31  154.700157           NaN
2014-09-30  155.258659           NaN
2014-10-31  155.562846           NaN
2014-11-30  155.935939           NaN
2014-12-31  156.370918    152.073547
2015-01-31  156.874024           NaN
2015-02-28  158.024475           NaN
2015-03-31  159.893825           NaN
2015-04-30  161.839395           NaN
2015-05-31  163.662033           NaN
2015-06-30  165.361119           NaN
2015-07-31  166.537058           NaN
2015-08-31  166.825724           NaN
2015-09-30  166.927714           NaN
2015-10-31  167.349793           NaN
2015-11-30  167.649963           NaN
2015-12-31  167.738984    164.057009
2016-01-31  168.352857           NaN
2016-02-29  169.904181           NaN
2016-03-31  171.544114           NaN
2016-04-30  173.229875           NaN
2016-05-31  175.298871           NaN
2016-06-30  176.893272           NaN
2016-07-31  177.950783           NaN
2016-08-31  178.682159           NaN
2016-09-30  178.934070           NaN

[241 rows x 2 columns]

# print(HPI_data.head(20).isnull().values.sum())
8

```

#### Pandas - [dropna()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html)
```
Parameters:	

    axis : {0 or ‘index’, 1 or ‘columns’}, or tuple/list thereof

        Pass tuple or list to drop on multiple axes

    how : {‘any’, ‘all’}

            any : if any NA values are present, drop that label
            all : if all values are NA, drop that label

    thresh : int, default None

        int value : require that many non-NA values

    subset : array-like

        Labels along other axis to consider, e.g. if you are dropping rows these would be a list of columns to include

    inplace : boolean, default False

        If True, do operation inplace and return None.

Returns:	

    dropped : DataFrame
```

#### Pandas - [fillna()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html)
```
Parameters:	

    value : scalar, dict, Series, or DataFrame

        Value to use to fill holes (e.g. 0), alternately a dict/Series/DataFrame of values specifying which value to use for each index (for a Series) or column (for a DataFrame). (values not in the dict/Series/DataFrame will not be filled). This value cannot be a list.

    method : {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, default None

        Method to use for filling holes in reindexed Series pad / ffill: propagate last valid observation forward to next valid backfill / bfill: use NEXT valid observation to fill gap

    axis : {0 or ‘index’, 1 or ‘columns’}

    inplace : boolean, default False

        If True, fill in place. Note: this will modify any other views on this object, (e.g. a no-copy slice for a column in a DataFrame).

    limit : int, default None

        If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled.

    downcast : dict, default is None

        a dict of item->dtype of what to downcast if possible, or the string ‘infer’ which will try to downcast to an appropriate equal type (e.g. float64 to int64 if possible)

Returns:	

    filled : DataFrame
```
