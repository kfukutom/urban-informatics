## ****Predictive Policing and Crime Forecasting 👮****
*Urban Informatics, Prof. Xiaofan Liang*

### Authors of the Project
- Ken Fukutomi (University of Michigan, Taubman)
- Ben Spilo (University of Michigan, School of Information)
  
# **Introduction 📌** 
This report provides a comprehensive analysis of all arrest types in Chicago for the year 2019-2022. The task presented a challenge in identifying a measure of criminality that is inherently subjective. Unlike burglaries, assaults, and violent crimes, which are often the result of civilian reports through 911 calls, arrests predominantly depend on the discretion of police officers. Our decision to focus on arrests was driven by the recognition of systemic bias and the disproportionate policing of communities with lower incomes and minority populations. The primary aim of this study is to develop a machine learning model capable of identifying potential hotspots for future arrests in Chicago. The initial phase of model development utilized various indicators of risk, such as unlit alleyways, potholes, the prevalence of vacant buildings, and the presence of public housing projects, which were later refined to enhance the predictive accuracy of the model.

Resource:
https://365datascience.com/tutorials/python-tutorials/predictive-model-python/

Assignment Info: https://xfliang.notion.site/Final-Proposal-e08b2c8a118d4fd19747bded1c87b7df

# **Modeling 🔨** 
in order to better understand this dataset, we will be utilizing pandas built in get_dummies() method to separate each time period as an activation key, to further utilize in our Hedonic Regression Model. Using a this regression model for predictive policing with a Chicago crime dataset involves several steps. A hedonic regression is a method used to estimate the influence of various factors on prices or values, often applied in real estate or labor economics. In the context of predictive policing, you could adapt it to estimate the influence of various factors (e.g., location, time, socio-economic indicators) on crime rates or crime types.
Hence we must:
- Clean the Data: Ensure your dataset is free from errors or inconsistencies. This includes handling missing values, correcting data types, and removing duplicates.
- Feature Engineering: Create new variables that might be relevant for your analysis. For instance, you could derive variables like the time of day (morning, afternoon, night) or categorize locations into broader areas.
- Normalization: Depending on your analysis, you may need to normalize some of your data, especially if you plan to compare the influence of variables on different scales.

![Image Alt text](/additional/model.jpg)



