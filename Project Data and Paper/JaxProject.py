#import gseapy as gp
#print(gp.__version__)

import gseapy as gp
hallmark = gp.get_library("MSigDB_Hallmark_2020", organism="Human")
list(hallmark.keys())
#print(len(hallmark['HALLMARK_TNFA_SIGNALING_VIA_NFKB']))  # 200


#-----Print out the entire 50 hallmarks and their genes-------
#print(hallmark)

#------See what hallmarks you have (just the names)-----------
#print(list(hallmark.keys()))

#------How many pathways and how many genes per pathway------
#print(len(hallmark), {k: len(v) for k, v in hallmark.items()})

#------Look at one pathway (first 20 genes)------
#first_key = next(iter(hallmark))
#print(first_key, hallmark[first_key][:20])


#------Pretty-print (more readable than raw print)------
#from pprint import pprint
#pprint({k: v[:40] for k, v in hallmark.items()})  # first 10 genes per pathway


#------Put it into a dataframe so it displays cleanly------
import pandas as pd

df = pd.DataFrame([
    {"Hallmark": k, "NumGenes": len(v), "First10Genes": ", ".join(v[:10])}
    for k, v in hallmark.items()
]).sort_values("NumGenes", ascending=False)

print(df)


with open("hallmark_genes.txt", "w") as f:
    for k, genes in hallmark.items():
        f.write(f"{k}\t{','.join(genes)}\n")


df.to_csv("hallmark_summary.csv", index=False)


#import os, inspect
#print("Current working directory:", os.getcwd())
#print("This code is running from:", inspect.getfile(lambda: None))  # may vary by environment
#print("hallmark type:", type(hallmark))

print("hallmark_summary.csv")