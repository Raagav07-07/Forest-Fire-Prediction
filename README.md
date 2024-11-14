
# Forest Fire Prediction Project

This project focuses on predicting forest fires using machine learning techniques, specifically Support Vector Machines (SVM). The model is designed to assess the risk of forest fires by analyzing environmental and meteorological data, with the goal of aiding early detection and prevention to mitigate potential damage.

## Project Overview

Forest fires are significant natural events with impacts on ecosystems, biodiversity, and human life. This project leverages machine learning to predict the likelihood of forest fires based on a set of critical parameters that influence fire risks. By using an SVM classifier, the project provides accurate predictions that support proactive fire prevention measures.

### Key Features

- **Data Simulation**: Generates realistic datasets reflecting historical trends and ranges for relevant variables.
- **Feature Engineering**: Uses essential predictors, such as temperature, humidity, wind speed, drought conditions, and fine fuel moisture.
- **Classification Model**: Implements a Support Vector Machine (SVM) classifier for binary prediction (fire or no fire).
- **Flask Web Application**: Deploys the model with a simple web interface for inputting data and receiving predictions.
- **SMS Notifications**: Integrates Twilio API to send alerts for high fire-risk predictions.

## Dataset

The dataset includes the following key features:
- **Temperature**: Measured in degrees Celsius.
- **Relative Humidity (RH)**: Measured as a percentage.
- **Wind Speed (Ws)**: Measured in km/h.
- **Rain**: Recorded in mm.
- **FFMC (Fine Fuel Moisture Code)**: Indicator of surface moisture.
- **DMC (Duff Moisture Code)**: Deeper-layer moisture content.

Other features such as **ISI (Initial Spread Index)**, **BUI (Build-Up Index)**, **FWI (Fire Weather Index)**, and **Classes** (indicating fire occurrence) may also be included to improve prediction accuracy.

## Technology Stack

- **Machine Learning**: Python (NumPy, Pandas, scikit-learn for SVM)
- **Web Framework**: Flask for deploying the application
- **Notification**: Twilio API for SMS alerts

## How to Use

1. Clone the repository.
2. Install the required packages from `requirements.txt`.
3. Run `app.py` to start the Flask server.
4. Input relevant data through the web interface and receive predictions.
5. Set up Twilio credentials in the `.env` file if SMS notifications are required.

## Future Work

Future improvements may include:
- Integrating real-time weather data APIs for up-to-date predictions.
- Extending the model to use ensemble methods for enhanced accuracy.
- Developing a mobile application interface for easy accessibility.

## Contributing

Contributions are welcome! Please submit a pull request for review.

## License

This project is licensed under the MIT License.
