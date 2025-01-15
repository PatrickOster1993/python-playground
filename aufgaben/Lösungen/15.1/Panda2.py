import numpy as np
import pandas as pd
import tabulate


print(pd.__version__)
tempdata = {
"Tage": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
"Temperaturen": [28, 30, 31.5, 27, 26, 32, 28],
}

temp = pd.DataFrame(tempdata)
print(tabulate.tabulate(temp, headers='keys', tablefmt='grid'))
