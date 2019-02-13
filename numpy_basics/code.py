# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",",skip_header=1)
census = np.concatenate((data,new_record), axis=0)


# --------------
#Code starts here
age = census[:,0]
#print (age)
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)


# --------------
#Code starts here
race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]

len_0 = race_0.shape[0]
len_1 = race_1.shape[0]
len_2 = race_2.shape[0]
len_3 = race_3.shape[0]
len_4 = race_4.shape[0]
race = np.array([len_0,len_1,len_2,len_3,len_4])
min_num = np.min(race)
#print (min_num)
minority_race = np.where(race == min_num)[0][0]
print (minority_race)






# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]
#print (senior_citizens[:,6])
working_hours_sum = np.sum(senior_citizens[:,6])

print (working_hours_sum)
senior_citizens_len = senior_citizens.shape[0]
print (senior_citizens_len)
avg_working_hours = np.round(working_hours_sum/senior_citizens_len,2)
print (avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]> 10]
low = census[census[:,1]<= 10]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print (avg_pay_high)
print (avg_pay_low)


