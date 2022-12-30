import pandas as pd
import numpy as np
import scheduling_repo.example_jobs as example_jobs
from scheduling_repo.efd import efd

df = example_jobs.return_example()
result = efd(df)
print(result)