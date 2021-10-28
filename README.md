# k-colorable-graph-
# Generates CNF format for checking if graph is k-colorable


# Jak funguje program:

Funkce create_dictionary() vytvoří slovník pro všechna kódování názvu literálů (vrcholu a 1_k barev). Klíčem je string ve tvaru: {číslo vrcholu},{1_k barva}.

Funkce generate_cnf() generuje pole v CNF tvaru, které potom jde použit ke kontrole splnitelnosti. 

V prvním cyklu jsem vytvořila klauzule pro každou proměnu s každou možnou z k barev.

V druhem cyklu jsem vytvořila klauzulí, co kontrolují jestli vrcholy na koncích hran nemají stejnou barvu. 

# Odpovědi na otázky: 

 1. Graph není 3-obarvitelný. Graph není 5-obarvitelný. Graph je 10-obarvitelný.
 2. Odhady pro 4.graph jsou: dolní: 9, horní: 12. Odhady pro 5.graph jsou dolní: 9, horní: 42. 

# Spouštění: 
  python3 k-colorable_sat.py {název souboru}.graph {k}
