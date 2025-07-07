#  Flood Shelter Recommendation System using Fuzzy Logic

This project is a fuzzy logic-based recommendation system to identify the **most suitable flood shelters** for individuals during flood emergencies. The system mimics human reasoning by considering multiple real-world factors — not just location — to compute a **suitability score** for each shelter.

---

##  Problem Statement

Traditional filtering (like listing shelters by distance or capacity) fails in crisis situations like floods. Survivors need **context-aware recommendations** that consider safety, accessibility, medical urgency, and terrain. This project uses **fuzzy logic** to manage such uncertainty and give smart, human-like suggestions.

---

##  Fuzzy Input Factors

We use six fuzzy input parameters to evaluate shelters:

| Factor               | Linguistic Terms            | Description                                                  |
|----------------------|-----------------------------|--------------------------------------------------------------|
| Distance             | Near, Medium, Far           | How far the shelter is from the user                         |
| Capacity             | Low, Medium, High           | Available capacity at the shelter                            |
| Accessibility        | Poor, Moderate, Good        | Suitability for differently-abled or elderly persons         |
| Proximity to Water   | Very Close, Close, Far      | Flood risk based on nearby water sources                     |
| Medical Help Required| Low, Medium, High           | Urgency of medical support needed by the user                |
| Elevation            | Low, Medium, High           | Terrain elevation of the shelter (higher = safer)            |

###  Membership Functions

- **Distance**: [0–20] km  
- **Capacity**: [0–100] people  
- **Accessibility**: [0–10] score  
- **Proximity to Water**: [0–10], where 0 = water-adjacent  
- **Medical Help Required**: [0–10], where 10 = critical  
- **Elevation**: [0–100] meters above flood level

---

##  Fuzzy Logic System

- **Type**: Mamdani Inference System using `skfuzzy.control`
- **Inputs**: Six fuzzy inputs defined above
- **Output**: Suitability score (0–100)
- **Defuzzification Method**: Centroid

###  Example Rules

- If **Medical Help Required** is *High* AND **Accessibility** is *Good* AND **Distance** is *Near*, THEN **Suitability** is *High*  
- If **Elevation** is *Low* OR **Proximity to Water** is *Very Close*, THEN **Suitability** is *Low*  
- If **Capacity** is *Low* AND **Medical Help Required** is *High*, THEN **Suitability** is *Very Low*

---

##  Output

- Suitability score for each shelter  
- Ranked shelter recommendations  
- Visualizations:
  - Fuzzy membership functions
  - Rule-based surfaces
  - Final suitability score chart

---

##  Technologies Used

- **Python 3**
- **NumPy**
- **Matplotlib**
- **Scikit-Fuzzy (`skfuzzy`)**

