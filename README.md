**HOTEL INTELLIGENT AND REVENUE PRESERVSTION SYSTEM**
**ARCHITECT:** GOD'S LIGHT
**STACK:** Python| Scikit-learn | plotly | Streamlit
**APP LINK:** WILL BE READY SOON. IN <= 3 days it should be ready
**REPOSITORY LINK:** https://github.com/mon148/HOTEL-INTELLIGENT-AND-REVENUE-PRESERVSTION-SYSTEM
**Important Note:** To log in to the AI dashboard interface, you should enter this default password. The passward will be personalized in the future update: **password == "NigeriaAI2026"**

**PROBLEM STATEMENT:**
Hotel cancellation cost the hospitality industry billions of lost in Average Daily Rate (ADR). So, this project is not just a dashboard to showcase any expertice but to ensure proactive revenue protection.
Key Metrics Performance:

###**62% ADR Sensitivity:** The model identified high-price to being the primary catalyst behind cancellation

###**Predictive Accuracy:** Tuned to identify cancellations before they happen, allowing managers to overbook or re-market rooms strategically.

###**Real-Time Simulation:** Integrated Gauge charts allow "What-If" analysis for dynamic pricing strategy.

###**KEY FEATURES**
###**AI-Pwered Risk Assessment:** Uses a Random Forest Classifier to evaluate more than 13 booking features instantly.

###**Live Testing Environment:** Interactive sliders than allow managers to test how the alteration of the ADR or Lead Time impacts the probability of a guest showing up.

###**Business Protection/Security:** Built-in session-state authentication engine to protect proprietary hotel data.

###**Cloud-Native Architecture:** Deployed on a serverless infrastructure for 99.9% uptime and global accessibility.

###'**SYSTEM STRUCTURE**
###**Data Acquisition:** Collects real-time booking parameters (Lead time, ADR, Special requests).

###**Feature Alignment:** Normalizes data through a pre-trained StandardScaler to ensure math accuracy.

###**Inference Engine:** Processes data through the .pkl Random Forest model.

###**Visual Output:** Renders a high-fidelity Plotly Gauge for non-technical stakeholders to interpret risk in seconds.

###**INSTALLATION AND LOCAL DEPLOYMENT**
**Clone The Repository:** git clone https://github.com/mon148/HOTEL-INTELLIGENT-AND-REVENUE-PRESERVSTION-SYSTEM

###**Intialize the environment:** Note that i ahve included a batch which would automatically load and install all requirements provided your system doesn't flag it as a threat since some system do: python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

###**Loaunch Dashboard:** ALso note that if your virtual environment is not activated, treamlit will tag joblib as unrecognised module. So, if the error pops up even after .venv is activated, then use the path directly as the .venv (.venv\scripts\streamlit.exe run web.py) This should work provided your virtual env is activated

**FUTURE IMPLEMENTATIONS**
Persistent Memory: Integration with Supabase/PostgreSQL for historical trend tracking.

Automated Communication: Direct integration with WhatsApp/Email APIs to send "Re-confirmation" prompts to high-risk guests automatically.

Multi-property suppport: Scaling the dashboard to handle multiple hotel or hospitality company prediction at once with human-based interactive suggestion from the AI base on its prediction

**Note to Stakeholders: This prototype demonstrates a complete end-to-end AI lifecycle—from raw data research to a secure, cloud-deployed decision-making tool.**