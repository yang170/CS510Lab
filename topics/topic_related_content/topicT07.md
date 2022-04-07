[techxplore.com](https://techxplore.com/news/2022-03-insight-machine-learning-error.html)

# Transfer learning offers new insight into machine-learning error estimation

Rachel Rose

---

Omar Maddouri, a doctoral student in the Department of Electrical and Computer Engineering at Texas A&M University, is working with Dr. Byung-Jun Yoon, professor, and Dr. Edward Dougherty, Robert M. Kennedy Chair Professor, to evaluate machine-learning models using transfer learning principles. Dr. Francis "Frank" Alexander with Brookhaven National Labs and Dr. Xiaoning Qian from the Department of Electrical and Computer Engineering at Texas A&M University are also involved with the project.

In data-driven machine learning, models are built to make predictions and estimations for what's to come in any given data set. One important field within machine learning is classification, which allows a data set to be assessed by an algorithm and then classified or broken down into classes or categories. When the data sets provided are very small, it can be very challenging to not only build a classification model based on this data but also to evaluate the performance of this model, ensuring its accuracy. This is where transfer learning comes into play.

"In transfer learning, we try to transfer knowledge or bring data from another domain to see whether we can enhance the task that we are doing in the domain of interest, or target domain," Maddouri explained.

The target domain is where the models are built, and their performance is evaluated. The source domain is a separate domain that is still relevant to the target domain from which knowledge is transferred to make the analysis within the target domain easier. 

Maddouri's project utilizes a joint prior density to model the relatedness between the source and target domains and offers a Bayesian approach to apply the transfer learning principles to provide an overall error estimator of the models. An error estimator will deliver an estimate of how accurate these machine-learning models are at classifying the data sets at hand.

What this means is that before any data is observed, the team creates a model using their initial inferences about the model parameters in the target and source domains and then updates this model with enhanced accuracy as more evidence or information about the data sets becomes available.

This technique of transfer learning has been used to build models in previous works; however, no one has ever before used this transfer learning technique to propose novel error estimators to evaluate the performance of these models. For an efficient utilization, the devised estimator has been implemented using advanced statistical methods that enabled a fast screening of source data sets which enhances the computational complexity of the transfer learning process by 10 to 20 times.

This technique can help serve as a benchmark for future research within academia to build upon. In addition, it can help with identifying or classifying different medical issues that would otherwise be very difficult. For example, Maddouri utilized this technique to classify patients with schizophrenia using transcriptomic data from brain tissue samples originally acquired by invasive brain biopsies. Because of the nature and the location of the brain region that can be analyzed for this disorder, the data collected is very limited. However, using a stringent feature selection procedure that comprises differential gene expression analysis and statistical testing for assumptions validity, the research team identified transcriptomic profiles of three genes from an additional brain region found to be highly relevant to the desired brain tissue as reported by independent research studies from other literature.

This knowledge allowed them to utilize the transfer learning technique to leverage samples collected from the second brain region (source domain) to help with the analysis and significantly boost the accuracy of diagnosis within the original brain region (target domain). The data gathered from the source domain can be exploratory in the absence of information from the target domain, allowing the research team to enhance the quality of their conclusion. 
