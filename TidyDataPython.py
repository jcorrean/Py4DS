import pandas as pd
base_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/"
table1 = pd.read_csv("{}table1/table1.csv".format(base_url))
table2 = pd.read_csv("{}table2/table2.csv".format(base_url))
table3 = pd.read_csv("{}table3/table3.csv".format(base_url))
table4a = pd.read_csv("{}table4a/table4a.csv".format(base_url))
table4b = pd.read_csv("{}table4b/table4b.csv".format(base_url))
table5 = pd.read_csv("{}table5/table5.csv".format(base_url), dtype = 'object')


La Tabla 1 (`table1`) viene así

table1

La Tabla 2 (`table2`) tiene esta apariencia


table2

La Tabla 3 (`table3`) es algo distinta


table3

La tabla 4a (`table4a`) también es algo diferente

table4a

Y lo mismo podemos afirmar de la tabla 4b

table4b

y de la tabla 5

table5

La recomendación estándar para analizar datos estructurados es que cada variable debe ocupar una columna, cada observación debe ocupar una fila o renglón, y los valores de cada observación deben estar en cada celda, tal como aparece en la siguiente imágen.

![](tidy.png){fig-align="center"}

Estas tres reglas están interrelacionadas porque es imposible satisfacer solo dos de las tres. Esa interrelación conduce a un conjunto aún más simple de instrucciones prácticas:
  
  Coloque cada conjunto de datos en un objeto de tipo tibble.
Coloque cada variable en una columna.

En este ejemplo, solo la tabla 1 está ordenada. Es la única representación donde cada columna es una variable.

¿Por qué es importante tener los datos ordenados? 
  
  La ventaja general es tener una forma consistente de almacenar datos. Si tiene una estructura de datos consistente, es más fácil aprender las herramientas que funcionan con ella porque tienen una uniformidad subyacente. La ventaja específica en colocar variables en columnas es que permite que la naturaleza vectorizada de pandas y NumPy brille.

Las librerías "altair" y "Pandas" funcionan bien con datos ordenados. Aquí hay un par de pequeños ejemplos que muestran cómo podría trabajar con la tabla 1.

```{python}
import altair as alt
table1.assign(
  rate = lambda x: x.cases / x.population * 1000
)

(table1.
  groupby('year').
  agg(n = ('cases', 'sum')).
  reset_index())

base_chart = (alt.Chart(table1).
              encode(alt.X('year'), alt.Y('cases'), detail = 'country'))

chart = base_chart.mark_line() + base_chart.encode(color = 'country').mark_circle()

chart
