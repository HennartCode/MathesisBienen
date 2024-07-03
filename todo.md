## TODOS
- Project cleanup
- Matplotlib
- Geburtensterberate
- Populationcount

## Bienen Verhalten

# AUSGANGSSITUATION
- Biene spawnt bei random hive mit random richtung

# STATUS Neutral                                           <<<<<<<<
- Zeit seit letzter Blume, falls zu groß ==> Biene stirbt         |
- Wird nur attracted von Blumen wo sie noch nicht waren           |
                                                                  |
# STATUS Attracted                                                |
- Falls Blume erreicht wird (Radius) ==> fliegt zum Center        |
- nimmt einen Pollen, dann neutral oder return                    |
                                                                  |
# STATUS Return                                                   |
- Zeit seit letzter Blume, falls zu groß ==> Biene stirbt         |
- Falls Biene bestimmte Anzahl an Pollen besitzt, zurück zu hive  |
- gibt Pollen ab                                           >>>>>>>>

## Blumen
- Konstanter Nektar
- Interval (z.B. 20-30, random) mit Pollen die zur Verfügung

