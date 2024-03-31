## ****Predictive Policing and Crime Forecasting 👮****
*Urban Informatics, Prof. Xiaofan Liang*

### Authors of the Project
- Ken Fukutomi (University of Michigan, Taubman College)
- Benjamin Spilo (University of Michigan, School of Information)
  
# **Abstract** 
This report provides a comprehensive analysis of all arrest types in Chicago for the year 2019-2022. The task presented a challenge in identifying a measure of criminality that is inherently subjective. Unlike burglaries, assaults, and violent crimes, which are often the result of civilian reports through 911 calls, arrests predominantly depend on the discretion of police officers. Our decision to focus on arrests was driven by the recognition of systemic bias and the disproportionate policing of communities with lower incomes and minority populations. The primary aim of this study is to develop a machine learning model capable of identifying potential hotspots for future arrests in Chicago. 

Resource:
https://365datascience.com/tutorials/python-tutorials/predictive-model-python/

Assignment Info: https://xfliang.notion.site/Final-Proposal-e08b2c8a118d4fd19747bded1c87b7df

# **Modeling** 

![Image Alt text](/additional/kNearNeigh.gif)

⭐ The first step involves collecting and preparing a dataset that includes historical crime data for different neighborhoods in Chicago. This dataset would also include features such as the walkability score of each neighborhood (which reflects how easy it is to accomplish daily errands on foot), transit accessibility (how easily residents can access public transportation), and various socioeconomic factors (like income levels, employment rates, educational attainment, etc.) Before applying the k-NN algorithm, it's crucial to select relevant features that are likely to influence crime rates. In this case, the features mentioned (walkability score, time, transit accessibility, and socioeconomic factors) are chosen because they are believed to have a significant impact on neighborhood safety and crime rates. For example, neighborhoods with high walkability and good transit accessibility might see different crime patterns than less accessible areas. Similarly, socioeconomic factors can significantly influence crime rates, with areas facing economic hardships often experiencing higher rates of crime.

Q: *"What exactly does k-NN algorithm do?"* : So, the k-nearest neighbor algorithm works by classifying a data point based on how its neighbors are classified. In the context of crime prediction, the "data point" could be a specific neighborhood or a set of conditions within a neighborhood at a certain time. The algorithm looks at 'k' other neighborhoods that are most similar to the one in question, based on the features selected (like walkability, transit accessibility, etc.). Similarity is usually measured using distance metrics, such as Euclidean distance. The idea is that neighborhoods with similar features are likely to have similar crime rates.

Final > Once the k nearest neighbors are identified, the algorithm predicts the crime rate for the neighborhood in question by aggregating the crime rates of these neighbors. This aggregation could be a simple average or a weighted average, where more similar neighbors have a greater influence on the prediction. Time is also such a crucial factor in predicting crime rates, as crime patterns can vary significantly by season, month, or even time of day. The model might include time as a feature by categorizing data points into time slots (e.g., night, day, weekend) and considering the historical crime rates for these periods. Other dynamic factors, like changes in socioeconomic conditions or transit options, can also be periodically updated in the dataset to improve prediction accuracy.
