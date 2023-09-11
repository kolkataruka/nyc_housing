**Stats component:** 
Hypothesis 1 (tested in stats_test.py using Chi Squared Independence test):
We used a Chi-Squared Independence Test for this, to check if there is a relationship between whether a housing violation case is open or closed (the case’s status) and the income classification (high income vs low income) of the zipcode the violation was recorded in.
Results:
T-statistics:  0.4105944685363506
p-value:  0.5216679307487839
p-value < 0.05 False
We thus reject the null hypothesis that a housing violation case is open or closed (the case’s status) and the income classification (high income vs low income) of the zipcode the violation was recorded in are independent from each other. They in fact do seem to have a relationship according to the current samples. We used the chi-square test for this as we are comparing the relationship between two categorical variables, instead of two numerical ones. This seemed like the obvious choice, so we didn’t consider any other variables. It was not difficult to employ this test. For this test, we classified the income levels to be below and above statewide median income level in that year, with a dummy variable, where 1 corresponds to above state median income level. 
This means that there is a relationship between whether a housing violation case is open or closed and the median income classification (high income vs low income) of the zipcode. 

Hypothesis 2 (tested in stats_test.py using One-Sample T-Test):
We test whether the median income across the zipcodes where housing violations, i.e., the zipcodes in our dataset, is the same as the median income in New York in 2021.
Results: 
T-statistics:  -3.452201496862518
p-value:  0.0005724654894218303
p-value < 0.05 True
These results show that median income across households which have gotten housing violations is in fact not similar/equal to the median income in New York in 2021. We thus reject the null hypothesis, which is mean of median income across those with housing violations is not equal to median income in New York in 2021. We used the one-sample T-test for this, as we are only looking at the distribution of one numerical variable, and as we wanted to determine the distribution of median income across housing violations, and see if the mean of distribution would be similar to overall median income in New York.  This seemed like the obvious choice, so we didn’t consider any other variables. It was not difficult to employ this test. For this test, we had to normalize our median income data to all be expressed in 2021 dollars using the consumer price indices from 2011 to 2021.
These results means that the mean of the distribution of median income of zip codes with housing violations is not the same as the median income of the state (population mean). 

Hypothesis 3 (tested in stats_test.py using Two-Sample T-Test):
Tests if the average number of violations every year in high income vs. low income zip codes is statistically different or not.
Results:
T-statistics:  -14.093458834185617
p-value:  7.553601644920016e-12
p-value < 0.05 True
These results show that the average number of violations per year in higher income zipcodes vs lower income zipcodes is in fact statistically different. We thus reject the null hypothesis.  We used the two sample t-test for this as we are comparing the relationship between two numerical variables, instead of two numerical ones. This seemed like the obvious choice, so we didn’t consider any other variables. It was not difficult to employ this test. For this test, we divided the dataset into data points in high income zipcodes and those in low income zipcodes. We then calculated the total number of violations for each subdataset per year to compare the average number of violations per year between the two subdatasets.
This means that there is a statistically significant difference between high income zipcodes and low income zipcodes in the average number of violations per year. 


**Machine learning component:** 
ML component 1 (K Nearest Neighbors): Input latitude, longitude, median income, and year as features in order to predict the binary classification of violation status (open/closed)

**Validation or regularization: the results of your machine learning-based analysis should be validated using cross validation or k-fold validation. Projects that apply regularization methods will receive extra recognition.** 
When implementing K nearest neighbors, we validated using cross validation. Cross validation allows us to evaluate the performance of the model on unseen data. We split the data into a training set and a validation set, and the model is trained on the training set before being tested on the validation set. The process is repeated with different subsets used for training and validation each time. The printed cross validation average represents an estimate of the model’s performance. 


**For both components you are required to provide a description of the result and adequate complementary information describing and motivating your process:**
**Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?**
When considering which ML algorithms we should use on our data, we considered numerous options. We tried both running logistic and linear regressions. We initially ran a logistic regression using latitude, longitude, violation status, and year as attributes to predict whether the area in which a violation occurred had a median income above/below the city average. We were getting an accuracy rate of 63%, but a precision and recall score 0.0. Looking at our data, we realized that 930 of our 1482 data points were categorized as above average median income, which meant that our data for this classification was so skewed that the model had a better chance of always guessing above average than attempting to classify. Knowing this, we realized that a logistic regression would not be a good fit for the data that we have. Then, we tried running a logistic regression that took latitude, longitude, violation status, and year in order to predict median income, however the accuracy of this model was quite low (30%). We predict that this is due to the use of numerous categorical variables to predict a continuous one, so there is not a strong enough relationship with the input data and the output to create an accurate model. 


Then, we decided to use K nearest neighbors because we had adequate labelled data as well as a categorical attribute of the data that could be fairly well described as a classification, that is whether a violation was resolved or not. We believed that location, income, and years could all be reasonably justified to have a relationship to whether a violation was resolved or not, and therefore saw the combination of these factors to be a satisfactory justification for running K nearest neighbors. 


To measure the accuracy of the model, we split the dataset into a 60/20/20 ratio of training/validation/test data respectively. Running the model several times, our training accuracy is generally in the 90-92% range while our testing accuracy is in a 88-90% range. When running cross validation, we receive 10 cv scores of [0.84507042, 0.9084507, 0.87943262, 0.85106383, 0.85106383, 0.82269504, 0.85106383, 0.87234043, 0.85106383, 0.87234043] with an average 0.8604584956547796. This success metric is standard practice for testing the success of a KNN model. We faced challenges in deciding the parameters to use for the model in terms of proportions to split the dataset on as well as determining the best k to use. While k=2 modelled the best training and test accuracy the first time we ran the model, we determined that k=2 was ultimately leading to overfitting, so we changed our k value to 4 to strike a better balance between complexity and bias in the model. We did not have to restructure our data too much in order to use this model, we simply converted our categorical status variable (open/closed) to a binary 0/1 to run the model. 
 
**What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?**
Our results demonstrate that there is a strong enough relationship between the location, income, and year of occurrence with whether or not the violation was resolved or not. Because of our fairly high accuracy (high 80s and low 90s), we can conclude that the model had a consistently good success rate of predicting the status of the violation. Intuitively, it makes sense that income has a correlation with whether or not the violation is open or closed. In lower income areas, it is possible that the violation will remain open for longer if an owner does not have the financial resources to resolve the issue. Similarly, location (lat and long) has a relationship with wealthier/poorer areas, in addition to indicating varying amounts of resources to resolve the violation. Year has a clear connection to the status of the violation, the oldest having the highest chance of being resolved. The results make sense given our data and we are confident in the prediction made with KNN. 



ML component 2 (Decision Tree): Input latitude, longitude, year_of_violation, status, zipcode, and median income as features in order to predict the severity of the housing violation (A, B, or C)
**Validation or regularization: the results of your machine learning-based analysis should be validated using cross validation or k-fold validation. Projects that apply regularization methods will receive extra recognition.** 
Like with K nearest neighbors, we used cross validation scores to validate our results. To do so, we used sk.learn’s cross validation score, passing in the model and our X and y. The result of the mean of our cv scores gives us a fuller understanding of the accuracy across the training and validation sets.

**For both components you are required to provide a description of the result and adequate complementary information describing and motivating your process:**
**Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?**
We chose to use a decision tree to try to predict the severity of the housing violation. We considered using logistic regression to predict this because the violation class was categorized into A, B, and C. We ultimately chose to use decision tree because it is well suited for non-linearity as well as handling categorical variables. Our data has two columns with categorical variables and will likely not have a linear relationship between the predictors and the outcomes. To measure the accuracy, we used sklear.metrics accuracy score, precision score, recall score, f1 score, as well as a cross validation score. We thought that the wide range of different ways to look at accuracy (i.e. not just the accuracy but the recall) would give us a fuller picture of whether or not our model was accurate. The biggest challenge we faced was coming to the conclusion that there was no tenable relationship between our input columns and the class values. The variability in our data was too high, and unable to accurately predict the housing violation’s class. Before using our data, we had to clean it for only the rows that contained the violation class information. Because we joined three datasets, and only the housing violation dataset had class violation information, there were many NaN values in that column. To isolate the housing violation rows, we dropped every row with NaN in the dataframe’s class column. 
 
**What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?**
Our results conclude that there is no meaningful connection between our violations’ location, income, open status, and year with the violation class. We had an accuracy of 0.47079037800687284, precision of 0.45792644643172037, recall of 0.47079037800687284, f1 score of 0.42617891987545636, and an average accuracy using cross validation of 0.4577319587628866. In short, the low accuracy across the board showed inconclusive results. While intuitively there is a connection between factors like the income of the area and how severe the violation is categorized, our data and test was not sufficient enough to prove it. We believe that with a fuller dataset we could prove that there is a correlation and be able to more accurately predict the class of the violations. However, with the data we had, because the data is skewed (some categories are so much more represented, i.e. the number of high income vs low income zipcodes represented) we are unable to make “successful” predictions. I am confident in the results that demonstrate the issues in our data, and the need for a fuller dataset to predict the class violations. 


**Provide comments and an interpretation of the results you obtained:**
**Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?**
The statistical results did correspond with our belief of the data. Median income in a zipcode is statistically related with how high/low average number of housing violations per year in that zipcode are and whether a violation case was still open or closed. We had theorized that there would be differences in outcomes between high income and low income zipcodes. The one-sample t-test also confirmed that our data did not reflect the full income distribution of New York, which either means our data was tilted towards higher income or lower income zipcodes, or there simply are more violations in certain kinds of zipcodes. 
The fairly accurate results of KNN supported again our belief that there would be a difference in the outcomes of violations depending on the median income, year, and location in which the violation occurred. We believe the accuracy of the ML models could have been improved with more precise data given that we were working with many binary/categorical variables as well as data about broader areas rather than something more specific such as property values. 
**Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?**
The statistical tools we chose seemed appropriate, especially to confirm with what our initial theories about the data overall. I guess a multivariate regression analysis would be able to further our understanding of the relationship between different variables in the data, but our data has several categorical variables which prevents us from doing such an analysis. 
Similarly with the ML models, we believe that we had to reach the models we ended up choosing through trial and error so we were able to find out that using regressions were not a good fit for our data. 


**Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?**
Since we are basing income levels on zip code, there is an immediate assumption that our results could be biased. Because of the variability in characteristics per each zip code, especially in New York where entire buildings have their own zip codes. Thus, relying on zip code as a geographical standard for which then to base median income off of, presents us with the possibility of discrepancies as not all zip codes are consistent for a given demographic characteristic (population). In addition, 
From an article discussing the pitfalls of using zip codes for geospatial analysis (https://carto.com/blog/zip-codes-spatial-analysis), zip codes are problematic in that they do not accurate represent human behavior or real boundaries. The article also pointed out how zip codes tend to be less representative of income disparity in large metropolitan areas. As such, these findings skew our analysis as we are assuming some sort of standardization for which to base our geographical assay of certain zip codes as higher income and lower income (based on the media NYC data).
A possible remedy for this would be to base the location on census tract or census block — which are standardized geographical clusterings determined by the United States Census. This would allow us a more balanced measure for which to base median income on. A possible methodology for going about this — finding a more equally distributed geographical unit for which to compare housing violations based on income:
Use the Census Geocoder API to find the census tract or block information for each address 
Download the data from the census for median household income per census tract
Do the same binary classification of higher income or lower income per each address compared to the City median.
Additionally, we could only find data on median household income, not per capita. This could also have an effect on our statistical analysis since we don’t necessarily know how a household median income metric differs from a per capita one and what biases this could create. However, it may be that median household income is a better measure of human behavior since it includes non-salary-related income such as social security, interest, dividends, and other sources. 


