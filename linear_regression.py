from __future__ import division
from numpy import genfromtxt, array

# y=mx+b

def step_gradient(b_current, m_current, points, learningRate, iteration):	
	b_gradient,m_gradient = 0,0
	 
	N = float(len(points))	
	for i in range(len(points)):
		x = points[i,0]
		y = points[i,1]

		b_gradient += - (2/N) * (y - ((m_current * x) + b_current))
		m_gradient += - (2/N) * x * (y - ((m_current * x) + b_current))
	
	new_b = b_current - (learningRate * b_gradient)
	new_m = m_current - (learningRate * m_gradient)	
	return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):	
	b1,m1 = starting_b, starting_m	
	for i in range(num_iterations):
		b1, m1 = step_gradient(b1, m1, array(points), learning_rate, i)	
	return [b1, m1]


def compute_error_for_line_given_points(b, m, points):
	totalError,error = 0,0	 	
	for i in range(0, len(points)):
		x = points[i,0]
		y = points[i,1]
		
		error = ((y - (m*x + b)) ** 2) / len(points) # Error funcion f(x) = ((y_initial - y_predicted)^2) / Number of data rows
		totalError += error / len(points)
		print "At Row {0}, using b = {1} and m = {2}, Error = {3}".format(i, b, m, error)

	print "\n Total Error: {0}".format(totalError)
	return error, totalError

def beginShow():	
	points = genfromtxt("diabetes.csv", delimiter=",")	
	learning_rate = 0.001		
	initial_b,initial_m = 1,1				
	num_iterations = 100
		
	print "\n First compute Error for each row by using equation y_predicted = mx +b and error =  (y - y_predicted) ^2 / len(points) by using random b = {0}, and m = {1} \n".format(initial_b, initial_m)
	compute_error_for_line_given_points(initial_b, initial_m,points)
	
	print "\n Run gradient_descent_runner to get new m and b with learning rate of {1} and {0} iterations \n".format(num_iterations, learning_rate)	
	[b,m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
		
	compute_error_for_line_given_points(b,m,points)
	print "\n After {0}nd iterations final b = {1}, m = {2} \n".format(num_iterations,b,m)

	print "\n Enter BMI to get Blood Sugar\n"
	X_test = 27.2
	print "\n Test BMI is: {0}\n".format(X_test)
	y_test = m * X_test + b
	print "\n Sugar level is {0} \n".format(y_test)

if __name__ == '__main__':
	beginShow()
