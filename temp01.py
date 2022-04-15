import pandas as pd

LD = pd.read_excel('lasso.xlsx', sheet_name="Sheet1", index_col=0 )

def highlightcorrelation(greenbox):
    iscorrelated = greenbox.nlargest(1).values
    return ['background-color: lightgreen' if v in iscorrelated else '' for v in greenbox] 

# def highlightlarge(greenbox):
#     islarge = 'bold' if greenbox >0.055 else 'black'
#     return 'font-weight: %s' % islarge

# def highlightbig(greenbox):
#     isbig = greenbox['LOG'].values >0.055 
#     return ['background-color: lightgreen' if v in isbig else '' for v in greenbox]

Corr1=LD.corr().style.apply(highlightcorrelation)
# Corr1=LD.corr().style.applymap(highlightlarge)
# Corr1=LD.corr().style.apply(highlightbig)
dfi.export(Corr1,'2 CorrelationMaxtrixTable.png')
Corr1