## ****Predictive Policing and Crime Forecasting 👮****
*Urban Informatics, Prof. Xiaofan Liang*

### Authors of the Project
- Ken Fukutomi (University of Michigan, Taubman College)
- Benjamin Spilo (University of Michigan, School of Information)
  
# ** Abstract** 
This report provides a comprehensive analysis of all arrest types in Chicago for the year 2019-2022. The task presented a challenge in identifying a measure of criminality that is inherently subjective. Unlike burglaries, assaults, and violent crimes, which are often the result of civilian reports through 911 calls, arrests predominantly depend on the discretion of police officers. Our decision to focus on arrests was driven by the recognition of systemic bias and the disproportionate policing of communities with lower incomes and minority populations. The primary aim of this study is to develop a machine learning model capable of identifying potential hotspots for future arrests in Chicago. 

Resource:
https://365datascience.com/tutorials/python-tutorials/predictive-model-python/

Assignment Info: https://xfliang.notion.site/Final-Proposal-e08b2c8a118d4fd19747bded1c87b7df

# **Modeling** 

![Image Alt text](/additional/model.jpg)

⭐ For Real Estate Properties ONLY: By incorporating time dummies (categorized as 0 or 1), we create a model that adopts the format of the 'repeated sales method,' commonly used in the real estate sector, for analyzing crime data. This approach is particularly useful when forecasting is challenging due to numerous variables, such as crime category, time, period, and season. Employing the rolling method and the hedonic model enables more accurate predictions based on unique characteristics and specific time periods. For each period, we run a statistical analysis using the statsmodels.api formula. This method enhances our ability to explore the data more exploratively.

