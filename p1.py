#Author: Dhwani Patel
#This is first program of implementing neural network with 3 neurons having its 4 inputs
#inputs here are outputs from other neurons

inputs = [1,2,3, 2.5]
weights1 = [0.2,0.8,-0.5,1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bais1 = 2
bais2 = 3
bais3 = 0.5


output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + bais1,
          inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + bais2,
          inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + bais3]
print(output)
