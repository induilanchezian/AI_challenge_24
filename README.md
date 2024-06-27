# Time series forecasting of number of accidents in Munich

Visualizing the time series trends of different types of accidents:

## **Alcohol related accidents**
<p align="center">
  <img src="images/Alkoholunfälle_timeseries.png" />
</p>

## **Escape accidents**
<p align="center">
  <img src="images/Fluchtunfälle_timeseries.png" />
</p>

## **Road accidents**
<p align="center">
  <img src="images/Verkehrsunfälle_timeseries.png" />
</p>



## **Predictions of alcohol related accidents for the year 2021**

Using 2 different kinds of autoregressive models, namely Autoregressive Moving Average (ARMA) and 
Autoregressive Integrated Moving Average (ARIMA), we can forecast the number of accidents for the year 2021 from 
data collected during all the previous years. The ARIMA model (green) performed better at predicting the values
than the ARMA model (blue). Ground truth is shown in red.

<p align="center">
  <img src="images/predictions_timeseries_2021.png" />
</p>

RMSE of ARMA model: 19.075  
RMSE of ARIMA model: 9.167



