'''
*********************************************
 * Author:          AYMAN HARRAZ
 * Creation Data:   3 MAY, 2023
 * Version:         v1.0
 ********************************************
Lab 4 
Write a python code that include Arithmatic,Relational and Bitwise operators 
'''

# Take 3 Readings From User 
Sensor1 =  (input ("Please Enter Number 1 : " ))
Sensor2 =  (input ("Please Enter Number 2 : " ))
Sensor3 =  (input ("Please Enter Number 3 : " ))

# Dictionary 
Sensor_dic = {

                 "S1" :  Sensor1,
                 "S2" :  Sensor2,
                 "S3" :  Sensor3
            }

print(Sensor_dic)

# List 

Sensor_list = [Sensor1,Sensor2,Sensor3]
print (Sensor_list )


# Touple

Sensor_tuple = [Sensor1,Sensor2,Sensor3]
print(type(Sensor_tuple))
print (Sensor_tuple )



