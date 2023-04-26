#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load libraries
import pandas as pd


# In[2]:


# Importing Datasets
ridedata_202204 = pd.read_csv('./202204-divvy-tripdata.csv')
ridedata_202205 = pd.read_csv('./202205-divvy-tripdata.csv')
ridedata_202206 = pd.read_csv('./202206-divvy-tripdata.csv')
ridedata_202207 = pd.read_csv('./202207-divvy-tripdata.csv')
ridedata_202208 = pd.read_csv('./202208-divvy-tripdata.csv')
ridedata_202209 = pd.read_csv('./202209-divvy-publictripdata.csv')
ridedata_202210 = pd.read_csv('./202210-divvy-tripdata.csv')
ridedata_202211 = pd.read_csv('./202211-divvy-tripdata.csv')
ridedata_202212 = pd.read_csv('./202212-divvy-tripdata.csv')
ridedata_202301 = pd.read_csv('./202301-divvy-tripdata.csv')
ridedata_202302 = pd.read_csv('./202302-divvy-tripdata.csv')
ridedata_202303 = pd.read_csv('./202303-divvy-tripdata.csv')


# In[3]:


# Combining all the datasets into one single dataframe
all_ridedata = [ridedata_202204,ridedata_202205,ridedata_202206,ridedata_202207,ridedata_202208,ridedata_202209,ridedata_202210,ridedata_202211,ridedata_202212,ridedata_202301,ridedata_202302,ridedata_202303]
rides = pd.concat(all_ridedata)


# In[4]:


print(rides.info())


# In[5]:


# find missing data points per column
missing_values_count = rides.isnull().sum()
print(missing_values_count)


# In[6]:


rides = rides.dropna()


# In[7]:


rides.isnull().sum()


# In[8]:


# Change data type to datetime 
rides['started_at'] = pd.to_datetime(rides['started_at'])
rides['ended_at'] = pd.to_datetime(rides['ended_at'])


# In[9]:


# Insert useful columns 

#Time of trip started
rides['time'] = rides['started_at'].dt.strftime('%H:%M')

#Day of the week of trip started
rides['day_of_the_week'] = rides['started_at'].dt.day_name()

#Month of the trip started
rides['month'] = rides['started_at'].dt.month_name()

#Year of the trip started
rides['year'] = rides['started_at'].dt.year

#Combining 'month' & 'year' column
rides['month_year'] = pd.to_datetime(rides['month'].astype(str)+rides['year'].astype(str),format='%B%Y').dt.strftime('%b-%Y')

#Trip duration in min
rides['trip_duration_in_min'] = (rides['ended_at'] - rides['started_at']).dt.total_seconds().div(60).astype(float)


# In[12]:


rides.info()


# In[13]:


# Romove unnecessary column 
rides.drop(['start_lat', 'start_lng','end_lat','end_lng'], axis=1,inplace=True)


# In[14]:


rides.info()


# In[15]:


rides.drop(['month', 'year'], axis=1,inplace=True)


# In[16]:


# Check invalid trip duration 
print(len(rides[rides['trip_duration_in_min']<0]))


# In[17]:


# Remove rows of invalid trip duration
indices = rides[rides['trip_duration_in_min']<0].index
rides = rides.drop(indices)


# In[20]:


rides.describe()


# In[18]:


# Export data into a csv file 
rides.to_csv('bike_share_rides.csv',index=False,header=True)


# In[ ]:




