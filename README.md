# DaSSA_Hackathon_ClinsightAI


## Introduction
This dataset contains sentiment-labeled reviews collected from Google Maps for various hospitals in Bengaluru, India. The feedback includes textual reviews from patients and their families, providing insights into their experiences with medical staff, facilities, and overall hospital services.

**Data Source:** https://www.kaggle.com/datasets/junaid6731/hospital-reviews-dataset

### Data Dictionary

| Variable            | Description                                                                     | Data Type         |
| ------------------- | ------------------------------------------------------------------------------- | ----------------- |
| **Feedback**        | Contains customer reviews about hospital services                               | Text (String)     |
| **Sentiment Label** | Indicates the sentiment associated with the review (0 = negative, 1 = positive) | Integer (Binary)  |
| **Rating**          | Numerical score between 1 and 5 representing overall customer satisfaction      | Integer (Ordinal) |


## Problem Statement
Multi-location healthcare groups rely heavily on patient reviews to understand performance. However, review data is often:

- Unstructured and noisy  
- Difficult to quantify operational impact  
- Hard to translate into actionable insights  

As a result, healthcare operators struggle to:

- Identify which operational themes most affect ratings  
- Distinguish between systemic vs. isolated issues  
- Quantify the impact of recurring problems on patient satisfaction  
- Prioritize improvements that drive retention and service quality  

Patient review datasets contain high-signal operational intelligence — but only when analyzed deeply and systematically.


## Objective
<p>ClinsightAI aims to transform unstructured hospital review data into actionable operational insights for healthcare providers. The system goes beyond basic sentiment analysis by identifying recurring service themes, quantifying their impact on patient satisfaction, and prioritizing improvement areas based on severity and influence on ratings.</p>

<p>By converting patient feedback into actionable intelligence, we enable healthcare organisations to make data-driven decisions that improve patient care, service quality, and facilitate meaningful operational improvements.</p>

## Methodology

ClinsightAI transforms unstructured hospital review data into actionable operational insights through a structured NLP-driven pipeline.

### Step 1: Data Cleaning & Text Preprocessing

Raw review text was standardized to improve consistency and analytical reliability.

This included:

- Text normalization (lowercasing and formatting)
- Noise removal (punctuation, special characters, non-informative terms)
- Lemmatization to reduce words to their base form

This ensured semantically similar feedback (e.g., *waiting*, *waited*, *wait*) was treated consistently.

### Step 2: Theme Extraction

Processed reviews were analyzed to identify recurring operational themes present in patient feedback.

Examples of themes include:

- Wait time
- Staff interaction
- Communication
- Cleanliness
- Administrative processes

This step converted unstructured text into structured thematic categories.

### Step 3: Theme-Based Quantification

Each extracted theme was evaluated to understand its relationship with patient satisfaction.

This involved:

- Measuring theme frequency
- Linking themes to associated review ratings
- Comparing occurrence in low vs. high rating reviews

This allowed qualitative feedback to be interpreted as measurable service indicators.

### Step 4: Operational Prioritization

Themes were evaluated using a prioritization framework based on:

- Frequency of occurrence
- Severity of impact on ratings
- Associated satisfaction levels

This enabled identification of:

- High-impact operational weaknesses
- Key drivers of patient dissatisfaction
- Priority targets for improvement

### Step 5: Insight Reporting

Insights were compiled into an automated static report summarizing:

- Key operational drivers of satisfaction
- Recurring problem areas
- Recommended improvement priorities

This step translated patient feedback into decision-support intelligence for healthcare operators.


