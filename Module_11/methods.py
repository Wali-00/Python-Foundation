import pandas as pd
df = pd.read_csv('student_data.csv')
#first er kichu value 
df.head(3)

#last er kichu value 
df.tail(5)

#column 
import numpy as np
col = np.array(df.columns)
print(col)
print(type(col.dtype))

#index 
ind = np.array(df.index)
print(ind)

# info 
df.info()

# randomize sample 
df.sample(10)

#statistical values 
df.describe()

